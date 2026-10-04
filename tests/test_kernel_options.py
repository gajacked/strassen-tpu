"""Kernel correctness and option-interaction tests, all in interpret mode.

These run on CPU without a TPU, which is the point: a suite that needs
scarce hardware does not get run, and the defects it should catch are
exactly the ones that hide between an option and a code path nobody
crossed.  Every epilogue here had been validated on its own; none had been
validated against a panel policy, and product_aware_residual was silently
ignoring classical_panels as a result -- executing 14 products where the
policy asked for 15, with no error.

Two behavioural invariants do most of the work:

* An option that is supposed to change nothing must produce a bitwise
  identical result (product-aware finalization reorders work only).
* An option that is supposed to change something must move the result.
  "Silently ignored" is the failure mode that inspection misses and this
  catches.
"""

from __future__ import annotations

import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import strassen_pallas as sp  # noqa: E402

HEAD_DIM = 128
EPS = 1e-6


def operands(m=64, k=512, n=256, seed=0):
    a = jax.random.normal(jax.random.PRNGKey(seed), (m, k), jnp.float32)
    b = jax.random.normal(jax.random.PRNGKey(seed + 1), (k, n), jnp.float32)
    return a.astype(jnp.bfloat16), b.astype(jnp.bfloat16)


def relative(got, want):
    got = jnp.asarray(got, jnp.float32)
    want = jnp.asarray(want, jnp.float32)
    return float(jnp.linalg.norm(got - want) / jnp.linalg.norm(want))


def reference_matmul(a, b):
    return a.astype(jnp.float32) @ b.astype(jnp.float32)


# --------------------------------------------------------------------------
# Each epilogue against its own reference.
# --------------------------------------------------------------------------

def test_plain_matmul_matches_reference():
    a, b = operands()
    got = sp.strassen_matmul(a, b, bm=32, bn=256, bk=256,
                             interleave_products=True, interpret=True)
    assert relative(got, reference_matmul(a, b)) < 0.03


@pytest.mark.parametrize("epilogue,activation", [
    ("swiglu", jax.nn.silu),
    ("geglu", lambda v: jax.nn.gelu(v, approximate=True)),
])
def test_gated_activation_epilogues(epilogue, activation):
    a, b = operands(n=512)
    laid = sp.swiglu_weight_layout(b, 256)
    got = sp.strassen_matmul(a, laid, bm=32, bn=256, bk=256,
                             epilogue=epilogue, interleave_products=True,
                             product_aware_swiglu=True, interpret=True)
    gate, up = jnp.split(reference_matmul(a, b), 2, axis=-1)
    assert relative(got, activation(gate) * up) < 0.03


def test_residual_add_epilogue():
    a, b = operands()
    residual = jax.random.normal(
        jax.random.PRNGKey(7), (64, 256), jnp.float32).astype(jnp.bfloat16)
    got = sp.strassen_matmul(a, b, bm=32, bn=256, bk=256,
                             epilogue="residual_add", residual=residual,
                             interleave_products=True, interpret=True)
    want = reference_matmul(a, b) + residual.astype(jnp.float32)
    assert relative(got, want) < 0.03


def test_norm_residual_add_epilogue():
    a, b = operands()
    residual = jax.random.normal(
        jax.random.PRNGKey(7), (64, 256), jnp.float32).astype(jnp.bfloat16)
    scale = jax.random.normal(jax.random.PRNGKey(8), (256,), jnp.float32)
    got = sp.strassen_matmul(
        a, b, bm=32, bn=256, bk=256, epilogue="norm_residual_add",
        residual=residual, norm_scale=scale.astype(jnp.bfloat16),
        norm_eps=EPS, interleave_products=True, interpret=True)
    y = reference_matmul(a, b)
    y = y * jax.lax.rsqrt(jnp.mean(y * y, -1, keepdims=True) + EPS) * scale
    assert relative(got, y + residual.astype(jnp.float32)) < 0.05


def test_qk_norm_rope_epilogue():
    heads, width = 2, 2 * HEAD_DIM
    a, b = operands(n=width)
    scale = jax.random.normal(jax.random.PRNGKey(9), (HEAD_DIM,), jnp.float32)
    inv = jax.random.uniform(jax.random.PRNGKey(10), (64, HEAD_DIM // 2)) * 3
    cos = jnp.concatenate([jnp.cos(inv)] * 2, -1).astype(jnp.bfloat16)
    sin = jnp.concatenate([jnp.sin(inv)] * 2, -1).astype(jnp.bfloat16)
    bn = 2 * HEAD_DIM
    laid = sp.rope_weight_layout(b, bn, HEAD_DIM)
    table_cos, table_sin = sp.rope_layout_tables(cos, sin, bn // 2, HEAD_DIM)
    got = sp.strassen_matmul(
        a, laid, bm=32, bn=bn, bk=256, epilogue="qk_norm_rope",
        rope_cos=table_cos, rope_sin=table_sin,
        rope_scale=sp.rope_scale_layout(scale, bn, HEAD_DIM),
        rope_head_dim=HEAD_DIM, rope_eps=EPS,
        interleave_products=True, interpret=True)

    q = reference_matmul(a, b).reshape(64, heads, HEAD_DIM)
    q = q * jax.lax.rsqrt(jnp.mean(q * q, -1, keepdims=True) + EPS) * scale
    first, second = jnp.split(q, 2, -1)
    rotated = jnp.concatenate((-second, first), -1)
    want = (q * cos[:, None, :] + rotated * sin[:, None, :]).reshape(64, width)
    order = sp.rope_weight_layout(
        jnp.arange(width, dtype=jnp.float32)[None, :], bn, HEAD_DIM)[0]
    restored = jnp.zeros_like(jnp.asarray(got)).at[
        :, order.astype(int)].set(jnp.asarray(got))
    assert relative(restored, want) < 0.05


# --------------------------------------------------------------------------
# Options that must change nothing.
# --------------------------------------------------------------------------

@pytest.mark.parametrize("epilogue,extra", [
    ("swiglu", {"product_aware_swiglu": True}),
    ("residual_add", {"product_aware_residual": True}),
])
def test_product_aware_is_bitwise_identical(epilogue, extra):
    """Product-aware finalization reorders work; it must not change output."""
    a, b = operands(n=512 if epilogue == "swiglu" else 256)
    kwargs = dict(bm=32, bn=256, bk=256, interleave_products=True,
                  epilogue=epilogue, interpret=True)
    if epilogue == "swiglu":
        b = sp.swiglu_weight_layout(b, 256)
    else:
        kwargs["residual"] = jax.random.normal(
            jax.random.PRNGKey(7), (64, 256), jnp.float32).astype(jnp.bfloat16)
    plain = sp.strassen_matmul(a, b, **kwargs)
    aware = sp.strassen_matmul(a, b, **kwargs, **extra)
    assert jnp.array_equal(jnp.asarray(plain), jnp.asarray(aware)), (
        f"{epilogue}: product-aware changed the result")


# --------------------------------------------------------------------------
# Options that must change something.  This is the regression test for
# product_aware_residual silently ignoring classical_panels.
# --------------------------------------------------------------------------

@pytest.mark.parametrize("extra", [
    {},
    {"product_aware_swiglu": True, "epilogue": "swiglu"},
    {"product_aware_residual": True, "epilogue": "residual_add"},
])
def test_classical_panels_take_effect(extra):
    """An exact panel must alter the result, whatever else is enabled.

    Equality here means the panel policy was accepted and ignored, which is
    how product_aware_residual shipped: it ran seven products on a panel the
    caller had asked to be exact.
    """
    extra = dict(extra)
    epilogue = extra.pop("epilogue", None)
    a, b = operands(n=512 if epilogue == "swiglu" else 256)
    kwargs = dict(bm=32, bn=256, bk=256, interleave_products=True,
                  interpret=True)
    if epilogue == "swiglu":
        b = sp.swiglu_weight_layout(b, 256)
        kwargs["epilogue"] = "swiglu"
    elif epilogue == "residual_add":
        kwargs["epilogue"] = "residual_add"
        kwargs["residual"] = jax.random.normal(
            jax.random.PRNGKey(7), (64, 256), jnp.float32).astype(jnp.bfloat16)
    # bk=256 over k=512 gives two panels; panel 0 is exact, panel 1 is not.
    without = sp.strassen_matmul(a, b, classical_panels=(), **kwargs, **extra)
    with_exact = sp.strassen_matmul(
        a, b, classical_panels=(0,), **kwargs, **extra)
    assert not jnp.array_equal(
        jnp.asarray(without), jnp.asarray(with_exact)), (
        "classical_panels was accepted and ignored")


# --------------------------------------------------------------------------
# Guards must reject what they claim to reject.
# --------------------------------------------------------------------------

def test_norm_residual_add_requires_full_width_tile():
    a, b = operands()
    with pytest.raises(ValueError, match="must equal n"):
        sp.strassen_matmul(
            a, b, bm=32, bn=128, bk=256, epilogue="norm_residual_add",
            residual=jnp.zeros((64, 256), jnp.bfloat16),
            norm_scale=jnp.ones((256,), jnp.bfloat16), interpret=True)


def test_qk_norm_rope_requires_whole_heads_per_half():
    a, b = operands(n=256)
    with pytest.raises(ValueError, match="2\\*head_dim"):
        sp.strassen_matmul(
            a, b, bm=32, bn=128, bk=256, epilogue="qk_norm_rope",
            rope_cos=jnp.ones((64, 64), jnp.bfloat16),
            rope_sin=jnp.ones((64, 64), jnp.bfloat16),
            rope_scale=jnp.ones((128,), jnp.bfloat16),
            rope_head_dim=HEAD_DIM, interpret=True)


def test_rope_arguments_rejected_without_the_epilogue():
    a, b = operands()
    with pytest.raises(ValueError, match="only used by"):
        sp.strassen_matmul(a, b, bm=32, bn=256, bk=256,
                           rope_cos=jnp.ones((64, 128), jnp.bfloat16),
                           interpret=True)


# --------------------------------------------------------------------------
# The free relayouts must be exactly that: free and reversible.
# --------------------------------------------------------------------------

def test_rope_layout_regroups_to_head_contiguous():
    width, bn = 8 * HEAD_DIM, 2 * HEAD_DIM
    ident = jnp.arange(width, dtype=jnp.float32)[None, :]
    order = sp.rope_weight_layout(ident, bn, HEAD_DIM)[0].astype(int)
    half_head, per_half = HEAD_DIM // 2, (bn // 2) // (HEAD_DIM // 2)
    blocks = width // bn
    regrouped = (order.reshape(blocks, 2, per_half, half_head)
                 .transpose(0, 2, 1, 3).reshape(width // HEAD_DIM, HEAD_DIM))
    assert jnp.array_equal(
        regrouped, jnp.arange(width).reshape(width // HEAD_DIM, HEAD_DIM))


def test_rope_scale_layout_is_linear():
    """Gemma's (1 + w) convention may be folded in before or after."""
    weight = jax.random.normal(jax.random.PRNGKey(3), (HEAD_DIM,), jnp.float32)
    before = sp.rope_scale_layout(1.0 + weight, 512, HEAD_DIM)
    after = 1.0 + sp.rope_scale_layout(weight, 512, HEAD_DIM)
    assert jnp.allclose(before, after)


def test_swiglu_layout_pairs_gate_with_up():
    width, bn = 1024, 256
    ident = jnp.arange(width, dtype=jnp.float32)[None, :]
    order = sp.swiglu_weight_layout(ident, bn)[0].astype(int)
    half = bn // 2
    for block in range(width // bn):
        lo = block * bn
        gate = order[lo:lo + half]
        up = order[lo + half:lo + bn]
        assert jnp.array_equal(up - gate, jnp.full((half,), width // 2))

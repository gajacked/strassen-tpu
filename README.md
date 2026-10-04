# Strassen GEMM on TPU

Public research snapshot of one-level, tile-local Strassen GEMM in JAX Pallas
(Mosaic), on a single TPU v5e or v6e (Trillium). The kernel replaces eight
quadrant multiplies with seven and folds the surrounding elementwise work —
SwiGLU, GeGLU, residual adds, per-head RMSNorm, RoPE — into the same kernel,
so the intermediate never reaches HBM.

Measured on two model families: Qwen3 (8B/14B/32B) establishes the result and
Gemma 3 27B tests whether it generalises.

All timings are same-run measurements on one Colab chip. Compilation and
checkpoint transfer are excluded. Every artifact is indexed with its SHA-256
in `evidence/qwen3/README.md` and `evidence/gemma3/README.md`;
`tools/verify_evidence.py` checks all 48 of them.

## Main result

Qwen3-32B, batch 8 x 1024 tokens, real weights:

| Workload | v5e | v6e |
|---|---:|---:|
| **Streamed, all 64 layers (registered gate)** | `1.0544x` | **`1.2950x`** |
| Single transformer block, layer 0 | `1.1566x` | `1.2093x` |
| Pure GEMM, no epilogue, vs XLA | `1.1312x` | `1.1117x` |
| Pure GEMM, vs matched cubic at the same tile | — | `1.0896x` |

The last row is the algorithm by itself. **Rank-7 is worth about 9%**, below
the `8/7 = 1.1429x` ceiling as a genuine Strassen saving should be. Everything
above that comes from fusion and tile selection, not from the multiply count.
That makes this a scheduling and fusion-boundary result rather than a
fast-matmul one.

Quality passes the registered gates at every width (8B/14B/32B): streamed
top-1 agreement `0.99963`, mean KL `1.374e-4` nats, WikiText-2 perplexity
delta under `4e-4`, HellaSwag choice agreement `1.000`, LAMBADA `0.991`.

## Generalisation to a second family

Gemma 3 27B is deliberately awkward for this kernel: four norms per block
instead of two, `(1 + w)` RMSNorm, GeGLU, and a 5:1 sliding/global attention
pattern with two RoPE bases.

| Workload | v5e | v6e |
|---|---:|---:|
| Layer-0 block, fused q/k | `1.1577x` | `1.1299x` |
| Layer-0 block, gate/up + GeGLU only | `1.0781x` | — |

The fused `q_norm`+RoPE epilogue is worth the same 8 points here as on Qwen3,
so that finding is a property of where the per-head norm sits, not of Qwen3.
The block result lands within a tenth of a point of Qwen3's `1.1566x` — which
contradicted our own prediction that Gemma would finish lower because its
norms block the `o`/`down` fusion.

## Scoring under the published harness

Every other quality number here is produced by our own scoring code, which
cannot detect a defect both arms share. `experiments/lm_eval/` registers the
streamed model with lm-evaluation-harness so the reference harness drives
scoring. HellaSwag, `--limit 200`, 256-token contexts, Gemma 3 27B:

| Arm | acc | acc_norm |
|---|---:|---:|
| Native XLA | `0.580` | `0.745` |
| Strassen | `0.580` | `0.745` |

**Zero delta on both metrics.** Routing the projections through the kernel
changes no answer on the task, measured under code that is not ours.

Getting there found a defect nothing else could see. The first run scored
`acc_norm 0.460`; the cause was a missing BOS token, worth **+28.5 points**.
Both arms had omitted it identically, so it cancelled exactly in every
agreement metric this project had — and two gates were *failing* because of
the handicap rather than the kernel. Self-consistency gates catch kernel
defects; only an external anchor catches protocol defects.

## What actually produced the speedup

Four findings, each measured on both chips:

1. **Fuse the epilogue or don't route the site.** Every projection wins in
   isolation — `k` most of all, at `1.175x` — yet routing `q`/`k`/`v` through
   the kernel *loses* inside a real block, because it breaks fusion XLA would
   otherwise do. `down` and `o` carry a fusable residual and win. Fusing
   `q_norm`+RoPE into the q/k kernel converts them from losing sites into the
   single biggest win here: **+8% of the block on both chips**.
2. **Never raise the XLA scoped-vmem flag to give the kernel a bigger budget.**
   The two are independent. On one chip at one tile the 128 MiB flag costs
   native XLA `37%` at the layer — but only `4.1%` on a bare GEMM, so the cost
   lands on the surrounding layer work, not the matmul.
3. **Tile heuristics do not port across generations.** A `bk=512` heuristic
   tuned for v5e is near-optimal there and `4.4%` off on v6e, whose 256x256
   MXU wants the whole contraction depth in one panel (`bk=5120`, no K loop).
4. **Product-aware quadrant finalization is v5e-specific.** Worth `-0.62 ms`
   there and `+0.05` to `+0.21 ms` on v6e across eight measurements: the MXU
   got roughly 4.7x faster while the VPU did not, so the epilogue no longer
   has room to hide behind the products.

5. **A fusable unit that does not fit the tile is not worth fusing.** In
   Gemma a norm separates each projection from its residual add, so we built
   a `norm_residual_add` epilogue for norm+residual+add. It **loses 7.3
   points** (`1.0841x` against `1.1568x`): its reduction spans the output
   width, forcing `bn == n`, and the surrendered tile freedom costs more than
   the saved traffic. The ceiling was about 1% of the block and we did not
   compute it before building. Both artifacts are published.

**Measure in a full transformer block, never in isolation.** Isolated screens
misled in both directions — they said all five projection sites advance, and
they scored the q/k fusion at `3.05x` against a baseline that materialises
work XLA fuses away.

## Layout

| | |
|---|---|
| `strassen_pallas.py` | the kernel: 7 products, 4 FP32 quadrant accumulators, the `swiglu` / `geglu` / `residual_add` / `bias_add` / `qk_norm_rope` / `norm_residual_add` epilogues, and the free weight relayouts they need |
| `experiments/qwen3/` | block, streamed, tile-selection and pure-GEMM harnesses |
| `experiments/gemma3/` | the generalisation arm: block, streamed and downstream |
| `experiments/lm_eval/` | lm-evaluation-harness adapter; the external anchor |
| `evidence/qwen3/`, `evidence/gemma3/` | raw JSONL for every claim above, hashed and indexed |
| `suite.py` | every stage per platform, with a `--dry-run` preflight |
| `tests/` | kernel and option-interaction tests; CPU, interpret mode, ~4s |
| `tools/reference_fidelity.py` | one real decoder layer vs `transformers` |
| `docs/RESULTS.md` | per-experiment protocol and numbers |
| `docs/COLAB_RUNBOOK.md` | how the runs are driven |
| `tools/verify_evidence.py` | re-hashes every artifact against the index |

## Limitations

- One chip, free-tier Colab; no multi-chip and no serving-stack integration.
- BF16 only. The v5e/v6e MXU also offers INT8; there is no FP8 story here.
- Two-level Strassen is closed: VMEM on v5e, and on v6e a second halving puts
  K at 128 inside a 256-wide MXU.
- The matched cubic control runs at about `93%` of XLA's GEMM efficiency while
  the Strassen substrate reaches `99%`, so "vs cubic" ratios carry a few
  points of substrate artifact and overstate the algorithm.
- The XLA baseline is measured with the scoped-vmem flag set to 48 MiB, which
  beat 128 MiB. XLA has not been measured at its own unset default, so the
  baseline may not be at its optimum.
- The streamed `1.2950x` sits above the single-block `1.2093x` under the same
  policy. The harnesses differ in protocol and the gap is not yet explained;
  it should not be read as the fusion improving with depth.
- Gemma and Qwen3 are **not measured at the same kernel budget** on v5e. Qwen3
  runs at the registered 47 MiB; Gemma's promoted tile uses the full 5376
  contraction depth, which does not fit, so its v5e numbers use 104 MiB. The
  two v5e block results are therefore not like-for-like. `suite.py` carries
  the per-model budgets so this is visible rather than implied.
- Gemma's streamed WikiText-2 gate and downstream agreement gate are published
  **failing**, and both predate the BOS fix. They are pending re-run and are
  not evidence that Gemma fails quality; the lm-eval measurement that replaced
  them shows zero delta.
- lm-eval coverage is Gemma-only and HellaSwag-only at `--limit 200`. Qwen3 has
  not been scored under the published harness, and against a published `~0.85`
  the Gemma residual is `~1.7` sigma plus two uncorrected systematics (the
  `-it` checkpoint rather than base, and 256-token contexts).

## Environment

JAX `0.7.2`, libtpu `0.0.21.1`, with the Mosaic IR-v7 compatibility override
in `mosaic_compat.py`. Upgrading either breaks the override.

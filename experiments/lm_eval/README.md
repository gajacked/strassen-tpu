# Scoring under the published harness

Every other quality number in this repository is produced by our own
scoring code, and comparing our arms against each other cannot detect a
defect both arms share. This directory exists because one did.

`lm_eval_strassen.py` registers the streamed model with
[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
as the model type `strassen`, so the reference harness drives scoring and
we supply only a forward pass.

```bash
pip install lm-eval
python experiments/lm_eval/run_lm_eval_strassen.py \
    --arm gated_strassen --tasks hellaswag --limit 200
python experiments/lm_eval/run_lm_eval_strassen.py \
    --arm regular_xla --tasks hellaswag --limit 200
```

## Result

HellaSwag, `--limit 200`, 256-token contexts, Gemma 3 27B:

| Arm | acc | acc_norm |
|---|---:|---:|
| Native XLA | `0.580` | `0.745` |
| Strassen | `0.580` | `0.745` |

Zero delta on both metrics. This is a stronger statement than any
agreement number elsewhere in the repository, because the protocol is not
ours: it measures answers under the same code the published tables use.

Against a published `~0.85` the residual is about `1.7` sigma at n=200
(one sigma is `0.031`), plus two systematics we do not correct for: this is
the `-it` checkpoint rather than the base model, and contexts are truncated
to 256 tokens to keep the streamed forward pass affordable.

## Why this directory earns its place

The first run scored `acc_norm 0.460`. The cause was a missing BOS token:
Gemma is trained with a leading `<bos>` and collapses toward a flat
output distribution without one. Adding it moved the score to `0.745`,
**+28.5 points**.

That defect was invisible to every gate this project had. Both arms omitted
the token identically, so it cancelled exactly in every agreement metric --
WikiText-2 top-1, downstream choice agreement, per-layer divergence, block
error norms. All of them were structurally incapable of seeing it, and two
of them were *failing* for reasons that turned out to be the handicap
rather than the kernel.

Self-consistency gates catch kernel defects. Only an external anchor
catches protocol defects. Both are needed, and the external one found more.

## Deliberate limits

`loglikelihood_rolling` and `generate_until` raise `NotImplementedError`
rather than returning something plausible. Rolling scoring needs windowed
evaluation across documents longer than the pinned sequence, and generation
needs a decode path the streamed harness does not have. Tasks requiring
either will fail loudly instead of reporting a wrong number.

Memory is the binding constraint. The model streams 54 GB of weights layer
by layer, so all requests are packed into `(BATCH, SEQUENCE)` blocks and
carried through each layer together -- the checkpoint streams once per
call, not once per request. Each block holds `BATCH*SEQUENCE*model_dim`
BF16 values, about 22 MB at 8x256, which puts a few hundred blocks at the
practical ceiling on one chip. Always report `--limit`: a subsample scored
under the real protocol is worth more than the full set scored under ours.

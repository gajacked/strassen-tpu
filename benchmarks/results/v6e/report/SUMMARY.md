# Interim v6e results

Verified 113/168 shapes at 2026-09-29T21:05:15.000100+00:00.

Results use three fresh inputs and 90 paired timing rounds per arm. Wins/losses require the paired pointwise 95% interval to lie entirely above/below 1; intervals crossing 1 are unresolved. No multiple-comparison adjustment. All shapes and Gaussian inputs are development data.

The execution order is not a random sample of the grid. These counts are not an estimate of the final 168-shape win rate. v5e has a separate study.

| Output | Method | Wins vs tuned Native | Losses | Unresolved | Unavailable/ineligible |
|---|---|---:|---:|---:|---:|
| float32 | cubic | 6 | 63 | 44 | 0 |
| float32 | s1 | 20 | 53 | 40 | 0 |
| float32 | s2 | 3 | 86 | 24 | 0 |
| bfloat16 | cubic | 16 | 57 | 40 | 0 |
| bfloat16 | s1 | 22 | 49 | 42 | 0 |
| bfloat16 | s2 | 4 | 84 | 25 | 0 |

## Numerical error

Relative L2 values below are the median and maximum across shapes of each shape’s worst of three seeds. Only eligible headline arms are summarized. Reference is FP64 on exact BF16 operands, either full output or 128 × 128 sampled output entries across all K; output finiteness is checked in full.

| Output | Method | Median relative L2 % | Maximum relative L2 % |
|---|---|---:|---:|
| float32 | native_default | 0.000009 | 0.000044 |
| float32 | native | 0.000009 | 0.000042 |
| float32 | cubic | 0.000009 | 0.000023 |
| float32 | s1 | 0.439399 | 0.453157 |
| float32 | s2 | 0.978082 | 1.017440 |
| bfloat16 | native_default | 0.166999 | 0.278719 |
| bfloat16 | native | 0.166999 | 0.278719 |
| bfloat16 | cubic | 0.166999 | 0.278719 |
| bfloat16 | s1 | 0.470116 | 0.483375 |
| bfloat16 | s2 | 0.991840 | 1.019354 |

The full five-method timings, frozen tuner decisions and counterfactual comparisons are in RESULTS.md. All confirmation arms and error metrics are retained in results.json; all screening decisions are in candidate_decisions.json. This snapshot does not change the running campaign or its selection rules.

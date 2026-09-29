# Project progress

While working in this project, follow `status/PROGRESS_WORKFLOW_v002.md` to keep
the user's live progress view current with concise actions, results, blockers,
and next steps. Append status updates at the start, at material milestones,
and before ending a turn. Report actual execution counts; do not substitute
preparation or an unrelated campaign for the requested experiment's progress.

Preserve executed source versions and experiment results. Archive validation
and experiment runs with scoped commits that exclude unrelated active work.

# Active experiment scope

Per the user's 2026-09-23 instruction, future MM tuning and LLM comparisons use
Native and Strassen depths 1 and 2 only. Exclude depths 3 and 4 unless the user
explicitly requests them again. Preserve their historical sources and results.

Per the user's 2026-09-24 instruction, future MM studies must treat FP32 output
and BF16 output as separate comparisons. Match input, accumulation and output
precision across Native, S1 and S2 within each comparison. Include any final
output conversion in timing and numerical error; do not pool results across
output dtypes. Broader BF16 comparisons follow the current full-contraction
probe, whose limited parent-kernel BF16 reproduction remains a separate group.

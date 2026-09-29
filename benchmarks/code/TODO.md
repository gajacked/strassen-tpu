# Project to-do list

## Deferred — probe consistency and the 4096³ crossover

Return to this after the other experiments are finished and the user resumes this work.

- [ ] **Compare the 12 shapes repeated across both probes.** Check whether the native slowdown at 4096³ also appears elsewhere. Compare each algorithm's absolute times, selected configuration and relative advantage, keeping the two allocations separate.
- [ ] **Audit timing variability and outliers.** Compare means, medians, spread and chronological samples for the repeated shapes. Retain every recorded measurement and explain how unusual samples affect the reported averages.
- [ ] **Design a controlled 4096³ repeat.** Freeze the protocol before launching: compare both previously selected Strassen tiles, the cubic configuration and native presets on the same allocation, with interleaved timings and a predefined repetition policy. Separate complete-call and prepared-kernel measurements. Keep execution deferred until this work is resumed.

Context to preserve: Strassen's mean was approximately 1.0014 ms in both probes, while the selected native mean changed from 0.9661 ms to 1.0371 ms. Both native runs used the 32 MiB preset. The previous Strassen run contained a 1.7021 ms sample. The measurements identify the reversal but do not establish its cause.

Use a new versioned run for any repeat. Preserve existing results, report each allocation separately and keep reserved holdouts untouched. Revisit the conservative large-shape rule after these checks.

Evidence: [Current probe table](outputs/01a0bf32-5290-7bb0-af6f-d1a7718dbb47/probe-comparison-v001/current_probe.csv), [previous probe table](outputs/01a0bf32-5290-7bb0-af6f-d1a7718dbb47/probe-comparison-v001/previous_probe.csv), [joined table](outputs/01a0bf32-5290-7bb0-af6f-d1a7718dbb47/probe-comparison-v001/joined_by_shape.csv), and [candidate Strassen region](reports/strassen_sufficient_region_v001/REGION_RULE.md).

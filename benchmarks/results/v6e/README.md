# v6e checkpoint: paused at 113/168 shapes

Start with [the summary](report/SUMMARY.md), [timings and decisions](report/RESULTS.md), and [tuner design](report/TUNER_DESIGN.md). Both output contracts have 113 completed geometries.

The report is an immutable export from the last completed analysis. Its dated heading saying "still running" describes report generation, not current status: the study is **paused**. See [checkpoint.json](../../checkpoint.json). `ORIGINAL_README.md` is historical.

`phases/` retains canonical raw evidence with member hashes in `phase-index.json`. `report/results.json.gz` and `report/candidate_decisions.json.gz` decompress to the original JSON bytes. Recovery evidence is excluded from statistics unless its whole comparison was verified. Only one copy of each phase's artifacts is kept; cohort source archives remain in `provenance/`.

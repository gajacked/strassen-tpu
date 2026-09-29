# Publication verification

All checks passed on September 29, 2026. No TPU was used.

- 113 complete screen/confirm pairs, 226 separate output comparisons.
- 1,255 original export files and 118,273 canonical v6e archive members verified.
- Rebuilt scientific fields and paired confidence intervals exactly match the saved report.
- Candidate ledger and frozen tuning policy are byte-identical after replay.
- Targeted credential-pattern scan found no matches across 127,120 payloads, including nested archives (4.42 GB uncompressed). This is not a proof that arbitrary data is secret-free.

Replay used NumPy 2.3.5. The report can be rebuilt with `python replay.py` from the benchmarks root.

`checked-content-MANIFEST.json` is the exact original export manifest checked by the recorded validation. `validation.json` records its SHA-256. The current root manifest additionally covers these validation receipts and this note; the scientific files are unchanged. Historical source paths/commits in the validation source manifest identify the original local validation execution.

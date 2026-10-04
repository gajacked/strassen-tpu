"""Verify every promoted artifact against its published SHA-256.

Each family under ``evidence/`` owns a ``README.md`` that indexes its own
artifacts.  The check is deliberately two-sided: a digest mismatch is a
corrupted or edited artifact, but an artifact present on disk and *absent
from the index* is the more common failure -- a result quietly added
without being claimed, or claimed under a name that no longer exists.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_ROOT = REPOSITORY_ROOT / "evidence"
SUFFIXES = (".jsonl", ".json")
ROW = re.compile(
    r"`(?P<name>strassen_[^`]+\.jsonl?)`\s*\|\s*"
    r"`(?P<digest>[0-9a-f]{64})`"
)


def verify(directory: Path) -> tuple[int, list[str]]:
    index = directory / "README.md"
    if not index.is_file():
        return 0, [f"{directory.name}: no README.md index"]

    entries = ROW.findall(index.read_text(encoding="utf-8"))
    documented = {name for name, _ in entries}
    actual = {
        path.name for path in directory.iterdir()
        if path.suffix in SUFFIXES
    }
    failures = []

    if len(documented) != len(entries):
        failures.append(f"{directory.name}: duplicate artifact names in index")
    for name, expected in entries:
        path = directory / name
        if not path.is_file():
            failures.append(f"{directory.name}: missing: {name}")
            continue
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            failures.append(
                f"{directory.name}: hash mismatch: {name}: "
                f"expected {expected}, got {observed}"
            )
    for name in sorted(actual - documented):
        failures.append(f"{directory.name}: unindexed: {name}")
    for name in sorted(documented - actual):
        failures.append(f"{directory.name}: indexed but absent: {name}")
    return len(entries), failures


def main() -> int:
    directories = sorted(
        path for path in EVIDENCE_ROOT.iterdir() if path.is_dir()
    )
    if not directories:
        print("no evidence families found")
        return 1

    total = 0
    failures: list[str] = []
    for directory in directories:
        count, problems = verify(directory)
        total += count
        failures.extend(problems)
        if not problems:
            print(f"{directory.name}: {count} artifacts verified")

    if failures:
        print("\n".join(failures))
        return 1
    print(f"{total} artifacts verified across {len(directories)} families")
    return 0


if __name__ == "__main__":
    sys.exit(main())

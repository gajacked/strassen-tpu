"""One place listing every benchmark stage, per platform, with a preflight.

Two problems this exists to solve.

The stages were scattered across dozens of run_*.py wrappers, so no single
place said what the promoted configuration for a platform actually is, and
the public runner drifted to a stale tile without anything noticing.

More expensively: illegal tiles were repeatedly discovered *on the chip*.
A tile that does not divide the geometry, or that exceeds the budget, costs
a whole session to find out.  ``--dry-run`` checks divisibility, alignment
and the VMEM estimate for every stage before anything is scheduled.

The VMEM check is a screen, not a decision.  The analytic estimate
under-predicts the Strassen arm, and by a shape-dependent amount: a 0.80
derating fitted on Qwen shapes still admitted two Gemma tiles that OOMed at
0.59 and 0.64 of the declared limit.  Feasibility is settled by compiling.

Usage:
    python3 suite.py --device v5e --dry-run
    python3 suite.py --device v6e --list
"""

from __future__ import annotations

import argparse
import json

# Model geometries, from the pinned checkpoints.
MODELS = {
    "qwen3-32b": dict(tokens=8192, model=5120, ffn=25600, heads=64,
                      kv_heads=8, head_dim=128, layers=64),
    "gemma3-27b": dict(tokens=8192, model=5376, ffn=21504, heads=32,
                       kv_heads=16, head_dim=128, layers=62),
}

# Promoted configuration per platform.  These are the numbers a reproduction
# needs, and the reason a single hardcoded tile could not serve both.
PROFILES = {
    "v5e": {
        "scoped_vmem_kib": 49152,
        # Per model, because they are not the same contract.  Qwen runs at
        # the registered 47 MiB.  Gemma cannot: its promoted tile uses the
        # full 5376 contraction depth, which does not fit 47 MiB, so its
        # v5e numbers are measured at a raised budget.  The two v5e block
        # results, 1.1566x for Qwen and 1.1577x for Gemma, are therefore not
        # a like-for-like comparison, and this table is where that shows.
        "strassen_limit_mib": {"qwen3-32b": 47, "gemma3-27b": 104},
        "qwen3-32b": {"gate_up": (2048, 2048, 512), "qk": (2048, 1024, 512),
                      "o": (1024, 2560, 512), "down": (2048, 1024, 1024)},
        "gemma3-27b": {"gate_up": (1024, 768, 5376), "qk": (1024, 1024, 5376)},
    },
    "v6e": {
        "scoped_vmem_kib": 49152,     # XLA's preference; raising it costs 37%
        "strassen_limit_mib": {"qwen3-32b": 120, "gemma3-27b": 104},
        "qwen3-32b": {"gate_up": (2048, 1024, 5120), "qk": (2048, 1024, 5120),
                      "o": (2048, 512, 8192), "down": (2048, 2560, 1024)},
        "gemma3-27b": {"gate_up": (1024, 768, 5376), "qk": (1024, 1024, 5376)},
    },
}

# stage -> (module, model, which tiles it uses, what it establishes)
STAGES = [
    ("pure_gemm", "benchmark_qwen3_v6e_pure_gemm", "qwen3-32b", ("gate_up",),
     "rank-7 alone, no epilogue: the algorithm's own contribution"),
    ("tile_tune", "benchmark_qwen3_scaling_tile_tune", "qwen3-32b",
     ("gate_up",), "equal-budget tile search"),
    ("site_tune", "benchmark_qwen3_site_tile_tune", "qwen3-32b",
     ("qk", "o", "down"), "per-site tiles for the routed projections"),
    ("block", "benchmark_qwen3_32b_full_layer_product_inference", "qwen3-32b",
     ("gate_up", "qk", "o", "down"), "one real-weight transformer block"),
    ("streamed", "benchmark_qwen3_32b_streamed_inference", "qwen3-32b",
     ("gate_up", "qk", "o", "down"), "all layers streamed: the registered gate"),
    ("quality", "benchmark_qwen3_streamed_natural_gate", "qwen3-32b",
     ("gate_up",), "WikiText-2 logit agreement"),
    ("downstream", "benchmark_qwen3_downstream_tasks", "qwen3-32b",
     ("gate_up",), "HellaSwag and LAMBADA answer agreement"),
    ("gemma_block", "benchmark_gemma3_block", "gemma3-27b",
     ("gate_up", "qk"), "Gemma block: generalisation to a second family"),
    ("gemma_streamed", "benchmark_gemma3_streamed", "gemma3-27b",
     ("gate_up",), "Gemma all layers with a task gate"),
    ("gemma_downstream", "benchmark_gemma3_downstream", "gemma3-27b",
     ("gate_up",), "Gemma answer agreement"),
]

DERATING = 0.80          # screen only; see the module docstring
LANE = 256               # v6e MXU edge, the stricter of the two


# The harnesses keep their research filenames so a published artifact traces
# to the code that emitted it; that means a stage name does not imply a path.
SEARCH_ROOTS = ("experiments/qwen3", "experiments/gemma3", ".")


def module_path(module):
    """Resolve a stage's module to its file, or None if it is missing."""
    import pathlib
    root = pathlib.Path(__file__).resolve().parent
    for directory in SEARCH_ROOTS:
        candidate = root / directory / f"{module}.py"
        if candidate.is_file():
            return str((pathlib.Path(directory) / f"{module}.py"))
    return None


def site_shape(model, site):
    g = MODELS[model]
    return {
        "gate_up": (g["model"], 2 * g["ffn"]),
        "qk": (g["model"], g["heads"] * g["head_dim"]),
        "o": (g["heads"] * g["head_dim"], g["model"]),
        "down": (g["ffn"], g["model"]),
    }[site]


def vmem_estimate(bm, bn, bk, halved_output=False):
    output = 3 * bm * bn if halved_output else 6 * bm * bn
    return 4 * (bm * bk + bk * bn) + output


def check(model, site, tile, limit_mib):
    bm, bn, bk = tile
    k, n = site_shape(model, site)
    tokens = MODELS[model]["tokens"]
    problems = []
    if tokens % bm:
        problems.append(f"tokens {tokens} % bm={bm}")
    if n % bn:
        problems.append(f"width {n} % bn={bn}")
    if k % bk:
        problems.append(f"depth {k} % bk={bk}")
    if bn % LANE or bk % LANE:
        problems.append(f"bn/bk not multiples of {LANE}")
    estimate = vmem_estimate(bm, bn, bk, halved_output=(site == "gate_up"))
    budget = limit_mib * 1024 * 1024
    if estimate > DERATING * budget:
        problems.append(
            f"estimate {estimate / 2**20:.1f} MiB over {DERATING:.0%} "
            f"of {limit_mib} MiB")
    return estimate, problems


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=tuple(PROFILES), required=True)
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    profile = PROFILES[args.device]

    if args.list:
        for name, module, model, sites, purpose in STAGES:
            print(f"{name:18s} {model:11s} {module_path(module) or module}")
            print(f"{'':18s} {purpose}")
        print(f"\n{'lm_eval':18s} {'gemma3-27b':11s} "
              f"experiments/lm_eval/run_lm_eval_strassen.py")
        print(f"{'':18s} HellaSwag under lm-evaluation-harness; "
              f"the only external anchor")
        return

    failures = 0
    print(f"preflight: {args.device}  "
          f"scoped_vmem={profile['scoped_vmem_kib']} KiB  "
          f"kernel_limit={profile['strassen_limit_mib']} MiB")
    for name, _module, model, sites, _purpose in STAGES:
        tiles = profile.get(model, {})
        if module_path(_module) is None:
            print(f"  {name:18s} module missing: {_module}")
            failures += 1
        for site in sites:
            tile = tiles.get(site)
            if tile is None:
                print(f"  {name:18s} {site:8s} no promoted tile — skipped")
                continue
            limit = profile["strassen_limit_mib"][model]
            estimate, problems = check(model, site, tile, limit)
            status = "ok" if not problems else "; ".join(problems)
            if problems:
                failures += 1
            print(f"  {name:18s} {site:8s} {str(tile):20s} "
                  f"{estimate / 2**20:6.1f} MiB  {status}")
    print(f"\n{failures} problem(s); VMEM is a screen, compiling decides")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()

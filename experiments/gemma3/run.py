"""Run one stage of the Gemma 3 generalisation experiment.

Gemma exists in this repository to answer one question the Qwen3 result
cannot: is the kernel's advantage a property of the method, or of Qwen3's
particular block?  Gemma 3 27B is a deliberately awkward second family --
four norms per block instead of two, `(1 + w)` RMSNorm, GeGLU instead of
SwiGLU, and a 5:1 sliding/global attention pattern with two RoPE bases.

The harnesses import the Qwen3 modules by flat name (`benchmark_common`,
`benchmark_qwen3_32b_layer`, `benchmark_cubic_control`), because the model
geometry table and the checkpoint reader are shared.  That is why this
runner puts `experiments/qwen3` on the path rather than duplicating them.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
REPOSITORY_ROOT = (
    HERE.parent.parent
    if HERE.name == "gemma3" and HERE.parent.name == "experiments"
    else HERE
)
# The Qwen3 directory carries the shared checkpoint reader and geometry table.
for path in (REPOSITORY_ROOT, REPOSITORY_ROOT / "experiments" / "qwen3", HERE):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))


# Gemma's promoted tile uses the full 5376 contraction depth in a single K
# panel.  That does not fit the 47 MiB budget Qwen3 runs at, so Gemma's
# numbers are measured at a raised *kernel* budget of 104 MiB.  The XLA
# scoped-vmem flag stays at the value XLA prefers either way -- raising it
# to match costs native XLA 37% at the layer and only 4% on a bare GEMM.
PROFILES = {
    "v5e": {
        "product_tile": "1024,768,5376",
        "cubic_tile": "1024,768,5376",
        "qk_tile": "1024,1024,5376",
        "o_tile": "1024,5376,512",
        "down_tile": "1024,5376,512",
        "strassen_limit_mib": "104",
        "cubic_limit_mib": "104",
        "scoped_vmem_kib": "49152",
    },
    "v6e": {
        "product_tile": "1024,768,5376",
        "cubic_tile": "1024,768,5376",
        "qk_tile": "1024,1024,5376",
        "o_tile": "1024,5376,512",
        "down_tile": "1024,5376,512",
        "strassen_limit_mib": "104",
        "cubic_limit_mib": "104",
        "scoped_vmem_kib": "49152",
    },
}

STAGES = {
    "block": "benchmark_gemma3_block",
    "streamed": "benchmark_gemma3_streamed",
    "downstream": "benchmark_gemma3_downstream",
}


def default_output_dir() -> str:
    return "/content/runs" if Path("/content").is_dir() else "runs"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=tuple(STAGES))
    parser.add_argument("--device", choices=tuple(PROFILES), default=None,
                        help="platform profile; selects the promoted tiles")
    parser.add_argument("--tile", help="override the gate/up tile, bm,bn,bk")
    parser.add_argument("--fused-qk", action="store_true",
                        help="route q and k through the qk_norm_rope epilogue")
    parser.add_argument(
        "--norm-residual", action="store_true",
        help="route o and down through norm_residual_add; measured at "
             "1.0841x against 1.1568x without it, and kept only so the "
             "refutation can be reproduced")
    parser.add_argument("--corpus", choices=("repeated", "wikitext2"),
                        default=None, help="streamed-gate corpus")
    parser.add_argument("--layers", type=int, default=None)
    parser.add_argument("--output-dir")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config_path = args.config
    if config_path is None:
        config_path = Path("/content/job.json")
        if not config_path.is_file():
            config_path = Path("job.json")
    config = {}
    if config_path.is_file():
        config = json.loads(config_path.read_text(encoding="utf-8"))

    stage = args.stage or config.get("stage")
    output_dir = args.output_dir or config.get("output_dir") or default_output_dir()
    device = args.device or config.get("device") or "v5e"
    if device not in PROFILES:
        parser.error(f"unknown device {device!r}; choose {tuple(PROFILES)}")
    profile = dict(PROFILES[device])
    if args.tile or config.get("tile"):
        profile["product_tile"] = args.tile or config["tile"]
    fused_qk = bool(args.fused_qk or config.get("fused_qk"))
    norm_residual = bool(args.norm_residual or config.get("norm_residual"))
    corpus = args.corpus or config.get("corpus") or "repeated"
    if stage not in STAGES:
        parser.error("set --stage or provide stage in job.json")

    os.environ["QWEN3_MODEL"] = "gemma3-27b"
    os.environ["GEMMA_PRODUCT_TILE"] = profile["product_tile"]
    os.environ["GEMMA_CUBIC_TILE"] = profile["cubic_tile"]
    os.environ["GEMMA_QK_TILE"] = profile["qk_tile"]
    os.environ["GEMMA_O_TILE"] = profile["o_tile"]
    os.environ["GEMMA_DOWN_TILE"] = profile["down_tile"]
    os.environ["QWEN3_STRASSEN_LIMIT_MIB"] = profile["strassen_limit_mib"]
    os.environ["QWEN3_CUBIC_LIMIT_MIB"] = profile["cubic_limit_mib"]
    os.environ["QWEN3_SCOPED_VMEM_KIB"] = profile["scoped_vmem_kib"]
    os.environ["GEMMA_FUSED_QK"] = "1" if fused_qk else "0"
    os.environ["GEMMA_NORM_RESIDUAL"] = "1" if norm_residual else "0"
    os.environ["GEMMA_CORPUS"] = corpus
    os.environ["QWEN3_OUTPUT_SUFFIX"] = ""
    os.environ["STRASSEN_OUTPUT_DIR"] = output_dir
    if args.layers or config.get("layers"):
        os.environ["GEMMA_LAYERS"] = str(args.layers or config["layers"])

    if args.dry_run:
        print(json.dumps({
            "model": "gemma3-27b",
            "stage": stage,
            "module": STAGES[stage],
            "output_dir": output_dir,
            "device": device,
            "fused_qk": fused_qk,
            "norm_residual": norm_residual,
            "corpus": corpus,
            **{k: v for k, v in profile.items()},
        }, sort_keys=True))
        return

    module = importlib.import_module(STAGES[stage])
    module.main()


if __name__ == "__main__":
    main()

"""Score one arm with the real lm-evaluation-harness.

Runs the reference harness against our streamed model so the protocol,
metrics and prompts are theirs rather than ours.  One arm per invocation:
each arm streams the whole checkpoint once, so running them together would
triple the transfer with nothing gained.

--limit is not optional in practice.  Every scored sequence must stay
resident while the model streams, so a few hundred blocks is the ceiling on
one chip.  A subsample under the published protocol beats the full set under
a protocol of our own.
"""
import json
import os
import types


def main():
    # Configuration comes from the environment, not argparse: colab exec runs
    # the script inside a Jupyter kernel whose own argv carries
    # "-f kernel-<id>.json", which argparse rejects outright.  Every other
    # wrapper here uses env vars for the same reason.
    args = types.SimpleNamespace(
        arm=os.environ.get("LMEVAL_ARM", "gated_strassen"),
        model=os.environ.get("QWEN3_MODEL", "gemma3-27b"),
        tasks=os.environ.get("LMEVAL_TASKS", "hellaswag"),
        limit=int(os.environ.get("LMEVAL_LIMIT", "200")),
        sequence=os.environ.get("QWEN3_SEQUENCE", "256"),
    )
    os.environ["QWEN3_MODEL"] = args.model
    os.environ.setdefault("QWEN3_SEQUENCE", args.sequence)
    os.environ.setdefault("QWEN3_SCOPED_VMEM_KIB", "49152")
    os.environ.setdefault("QWEN3_STRASSEN_LIMIT_MIB", "104")
    os.environ.setdefault("QWEN3_CUBIC_LIMIT_MIB", "104")
    if args.model.startswith("gemma"):
        os.environ.setdefault("GEMMA_PRODUCT_TILE", "1024,768,5376")
        os.environ.setdefault("GEMMA_CUBIC_TILE", "1024,768,5376")
        os.environ.setdefault("GEMMA_QK_TILE", "1024,1024,5376")
        os.environ.setdefault("GEMMA_FUSED_QK", "1")

    import lm_eval
    from lm_eval_strassen import StrassenLM

    model = StrassenLM(arm=args.arm)
    results = lm_eval.simple_evaluate(
        model=model, tasks=args.tasks.split(","), limit=args.limit,
        bootstrap_iters=0)
    summary = {
        "arm": args.arm, "model": args.model, "limit": args.limit,
        "sequence": int(os.environ["QWEN3_SEQUENCE"]),
        "results": results["results"],
    }
    path = (f"/content/results/strassen_lmeval_{args.model}_{args.arm}"
            f"_{args.tasks.replace(',', '_')}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)
    print("LMEVAL_JSON " + json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()

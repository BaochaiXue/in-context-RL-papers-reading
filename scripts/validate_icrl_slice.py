from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate the minimum ICRL slice artifacts.")
    parser.add_argument("--artifact-dir", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    required = [
        args.artifact_dir / "summary.json",
        args.artifact_dir / "per_seed_metrics.json",
        args.artifact_dir / "transitions.jsonl",
        args.artifact_dir / "calibration.csv",
        args.artifact_dir / "memory_contents.jsonl",
        args.artifact_dir / "revision_events.jsonl",
        args.artifact_dir / "smoke_check.txt",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"missing artifacts: {missing}")

    summary = json.loads((args.artifact_dir / "summary.json").read_text())
    aggregate = summary.get("aggregate", {})
    for agent_name in ("explicit_state", "opaque_history", "filtered_history", "retrieval_proxy", "compiled_memory"):
        if agent_name not in aggregate:
            raise SystemExit(f"missing aggregate entry for {agent_name}")

    explicit = aggregate["explicit_state"]
    compiled = aggregate["compiled_memory"]
    if explicit.get("belief_brier_score") is None:
        raise SystemExit("explicit_state is missing belief_brier_score")
    if compiled.get("memory_event_count") in (None, 0):
        raise SystemExit("compiled_memory is missing memory_event_count")

    print("artifact_dir:", args.artifact_dir)
    print("config:", summary.get("config", {}))
    print("scope:", summary.get("scope", {}))
    print("explicit_state cumulative_regret:", explicit["cumulative_regret"])
    print("opaque_history cumulative_regret:", aggregate["opaque_history"]["cumulative_regret"])
    print("compiled_memory cumulative_regret:", compiled["cumulative_regret"])
    print("explicit_state better on regret:", summary["comparison"]["explicit_state_better_on_regret"])
    print("explicit_state better on reward:", summary["comparison"]["explicit_state_better_on_reward"])
    print("explicit_state belief_brier_score:", explicit["belief_brier_score"])
    print("compiled_memory better than raw_history on regret:", summary["comparison"]["compiled_memory_better_than_raw_history_on_regret"])
    print("compiled_memory better than filtered_history on regret:", summary["comparison"]["compiled_memory_better_than_filtered_history_on_regret"])
    print("compiled_memory better than retrieval_proxy on regret:", summary["comparison"]["compiled_memory_better_than_retrieval_proxy_on_regret"])
    if not summary["aggregate"]["compiled_memory"]["revision_count"]:
        raise SystemExit("compiled_memory did not record any revision events")


if __name__ == "__main__":
    main()

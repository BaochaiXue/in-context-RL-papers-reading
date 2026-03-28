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
        args.artifact_dir / "smoke_check.txt",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"missing artifacts: {missing}")

    summary = json.loads((args.artifact_dir / "summary.json").read_text())
    aggregate = summary.get("aggregate", {})
    for agent_name in ("explicit_state", "opaque_history"):
        if agent_name not in aggregate:
            raise SystemExit(f"missing aggregate entry for {agent_name}")

    explicit = aggregate["explicit_state"]
    if explicit.get("belief_brier_score") is None:
        raise SystemExit("explicit_state is missing belief_brier_score")

    print("artifact_dir:", args.artifact_dir)
    print("config:", summary.get("config", {}))
    print("scope:", summary.get("scope", {}))
    print("explicit_state cumulative_regret:", explicit["cumulative_regret"])
    print("opaque_history cumulative_regret:", aggregate["opaque_history"]["cumulative_regret"])
    print("explicit_state better on regret:", summary["comparison"]["explicit_state_better_on_regret"])
    print("explicit_state better on reward:", summary["comparison"]["explicit_state_better_on_reward"])
    print("explicit_state belief_brier_score:", explicit["belief_brier_score"])
    if not summary["comparison"]["explicit_state_better_on_regret"]:
        raise SystemExit("explicit_state did not outperform opaque_history on cumulative regret for this run")


if __name__ == "__main__":
    main()

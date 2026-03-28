from __future__ import annotations

import json
import math
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List


def belief_brier_score(transitions: List[dict], num_tasks: int) -> float | None:
    rows = [t for t in transitions if t["belief"] is not None]
    if not rows:
        return None
    scores = []
    for row in rows:
        target = [0.0 for _ in range(num_tasks)]
        target[row["task_id"]] = 1.0
        belief = row["belief"]
        scores.append(sum((b - y) ** 2 for b, y in zip(belief, target)) / num_tasks)
    return mean(scores)


def shift_recovery_steps(transitions: List[dict]) -> int | None:
    shifted = [row for row in transitions if row["shifted"]]
    if not shifted:
        return None
    run = 0
    start_step = shifted[0]["global_step"]
    for row in shifted:
        run = run + 1 if row["action"] == row["optimal_arm"] else 0
        if run >= 3:
            return row["global_step"] - start_step - 2
    return None


def summarize_agent(transitions: List[dict], num_tasks: int) -> Dict[str, float | int | None]:
    rewards = [row["reward"] for row in transitions]
    regrets = [row["regret"] for row in transitions]
    optimal_rate = mean([1.0 if row["action"] == row["optimal_arm"] else 0.0 for row in transitions])
    unc = [row["selected_arm_uncertainty"] for row in transitions if row["selected_arm_uncertainty"] is not None]
    return {
        "cumulative_regret": sum(regrets),
        "average_reward": mean(rewards),
        "optimal_action_rate": optimal_rate,
        "belief_brier_score": belief_brier_score(transitions, num_tasks),
        "mean_selected_arm_uncertainty": mean(unc) if unc else None,
        "shift_recovery_steps": shift_recovery_steps(transitions),
    }


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True))


def is_finite_metric(value: object) -> bool:
    return value is None or (isinstance(value, (int, float)) and math.isfinite(value))


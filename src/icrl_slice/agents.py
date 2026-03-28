from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional


def normalize(values: List[float]) -> List[float]:
    total = sum(values)
    if total <= 0:
        return [1.0 / len(values) for _ in values]
    return [v / total for v in values]


@dataclass
class OpaqueHistoryAgent:
    recency: float = 0.97
    optimism: float = 0.10
    values: List[float] = field(default_factory=list)
    counts: List[int] = field(default_factory=list)

    def reset(self, num_arms: int) -> None:
        self.values = [0.5 for _ in range(num_arms)]
        self.counts = [0 for _ in range(num_arms)]

    def act(self) -> int:
        scores = []
        for idx, value in enumerate(self.values):
            bonus = self.optimism / math.sqrt(self.counts[idx] + 1)
            scores.append(value + bonus)
        return max(range(len(scores)), key=lambda i: scores[i])

    def update(self, action: int, reward: float) -> None:
        self.counts[action] += 1
        self.values[action] = self.recency * self.values[action] + (1.0 - self.recency) * reward

    def snapshot(self) -> Dict[str, Optional[float]]:
        last_uncertainty = 1.0 / math.sqrt(self.counts[self.act()] + 1)
        return {
            "belief": None,
            "belief_top_task": None,
            "belief_top_prob": None,
            "selected_arm_uncertainty": last_uncertainty,
        }


@dataclass
class ExplicitStateAgent:
    task_means: List[List[float]]
    exploration_scale: float = 0.05
    change_sensitivity: float = 0.35
    posterior: List[float] = field(default_factory=list)

    def reset(self, num_arms: int, num_tasks: int) -> None:
        del num_arms
        self.posterior = [1.0 / num_tasks for _ in range(num_tasks)]

    def _arm_mean(self, arm: int) -> float:
        return sum(p * self.task_means[t][arm] for t, p in enumerate(self.posterior))

    def _arm_uncertainty(self, arm: int) -> float:
        mean = self._arm_mean(arm)
        variance = sum(p * (self.task_means[t][arm] - mean) ** 2 for t, p in enumerate(self.posterior))
        return math.sqrt(max(variance, 1e-9))

    def act(self) -> int:
        scores = []
        num_arms = len(self.task_means[0])
        for arm in range(num_arms):
            scores.append(self._arm_mean(arm) + self.exploration_scale * self._arm_uncertainty(arm))
        return max(range(num_arms), key=lambda a: scores[a])

    def update(self, action: int, reward: float) -> None:
        likelihoods = []
        for task_id in range(len(self.posterior)):
            p = self.task_means[task_id][action]
            likelihoods.append(max(1e-6, p if reward >= 0.5 else 1.0 - p))
        predicted = sum(prior * like for prior, like in zip(self.posterior, likelihoods))
        surprise = 1.0 - max(0.0, min(1.0, predicted))
        updated = normalize([prior * like for prior, like in zip(self.posterior, likelihoods)])
        uniform = [1.0 / len(updated) for _ in updated]
        mix = self.change_sensitivity * surprise
        self.posterior = normalize([(1.0 - mix) * u + mix * q for u, q in zip(updated, uniform)])

    def snapshot(self) -> Dict[str, object]:
        belief_top_task = max(range(len(self.posterior)), key=lambda t: self.posterior[t])
        belief_top_prob = self.posterior[belief_top_task]
        arm = self.act()
        return {
            "belief": self.posterior[:],
            "belief_top_task": belief_top_task,
            "belief_top_prob": belief_top_prob,
            "selected_arm_uncertainty": self._arm_uncertainty(arm),
            "arm_value_estimates": [self._arm_mean(a) for a in range(len(self.task_means[0]))],
        }

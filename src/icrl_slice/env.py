from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import List, Optional


@dataclass
class StepInfo:
    task_id: int
    optimal_arm: int
    optimal_mean: float
    chosen_mean: float

    def as_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "optimal_arm": self.optimal_arm,
            "optimal_mean": self.optimal_mean,
            "chosen_mean": self.chosen_mean,
        }


def default_task_means(num_tasks: int, num_arms: int) -> List[List[float]]:
    """Generate a simple task family with a rotating optimal arm."""
    means: List[List[float]] = []
    for task_id in range(num_tasks):
        row = [0.15 for _ in range(num_arms)]
        best = task_id % num_arms
        row[best] = 0.90
        means.append(row)
    return means


class HiddenTaskBandit:
    def __init__(
        self,
        num_arms: int = 5,
        num_tasks: int = 3,
        horizon: int = 20,
        task_means: Optional[List[List[float]]] = None,
        seed: int = 0,
    ) -> None:
        self.num_arms = num_arms
        self.num_tasks = num_tasks
        self.horizon = horizon
        self.task_means = task_means or default_task_means(num_tasks, num_arms)
        self.rng = Random(seed)
        self.current_task = 0
        self.timestep = 0

    def reset(self, task_id: Optional[int] = None) -> dict:
        if task_id is None:
            task_id = self.rng.randrange(self.num_tasks)
        self.current_task = task_id
        self.timestep = 0
        return {"num_arms": self.num_arms, "task_id_hidden": None}

    def intervene(self, task_id: int) -> None:
        self.current_task = task_id

    def step(self, action: int) -> tuple[float, dict]:
        chosen_mean = self.task_means[self.current_task][action]
        reward = 1.0 if self.rng.random() < chosen_mean else 0.0
        optimal_mean = max(self.task_means[self.current_task])
        optimal_arm = self.task_means[self.current_task].index(optimal_mean)
        self.timestep += 1
        return reward, StepInfo(
            task_id=self.current_task,
            optimal_arm=optimal_arm,
            optimal_mean=optimal_mean,
            chosen_mean=chosen_mean,
        ).as_dict()

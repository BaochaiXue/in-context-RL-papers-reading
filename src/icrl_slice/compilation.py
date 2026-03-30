from __future__ import annotations

import math
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, List


def normalize(values: List[float]) -> List[float]:
    total = sum(values)
    if total <= 0:
        return [1.0 / len(values) for _ in values]
    return [v / total for v in values]


def softmax(scores: List[float]) -> List[float]:
    maximum = max(scores)
    exps = [math.exp(score - maximum) for score in scores]
    return normalize(exps)


@dataclass
class Event:
    kind: str
    action: int
    reward: float
    surprise: float
    active_task_before: int
    support_task: int
    contradicted_active: bool
    likelihoods: List[float]


@dataclass
class RevisionEvent:
    global_step: int
    episode: int
    timestep: int
    from_task: int
    to_task: int
    surprise: float
    reason: str


@dataclass
class ExperienceCompiler:
    contradiction_threshold: float = 0.55

    def extract(
        self,
        action: int,
        reward: float,
        task_means: List[List[float]],
        posterior: List[float],
        active_task: int,
    ) -> Event:
        likelihoods = []
        for task_id in range(len(task_means)):
            p = task_means[task_id][action]
            likelihoods.append(max(1e-6, p if reward >= 0.5 else 1.0 - p))
        expected = task_means[active_task][action]
        observed_prob = expected if reward >= 0.5 else 1.0 - expected
        surprise = 1.0 - max(0.0, min(1.0, observed_prob))
        contradicted_active = reward < 0.5 and expected >= self.contradiction_threshold
        support_task = max(range(len(likelihoods)), key=lambda idx: likelihoods[idx])
        return Event(
            kind="positive" if reward >= 0.5 else "negative",
            action=action,
            reward=reward,
            surprise=surprise,
            active_task_before=active_task,
            support_task=support_task,
            contradicted_active=contradicted_active,
            likelihoods=likelihoods,
        )


@dataclass
class RevisableMemory:
    num_tasks: int
    revision_threshold: float = 0.40
    invalidation_penalty: float = 1.25
    event_buffer_size: int = 12
    task_scores: List[float] = field(default_factory=list)
    active_task: int = 0
    revision_count: int = 0
    event_buffer: Deque[dict] = field(default_factory=deque)
    pending_revisions: List[dict] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.task_scores:
            self.task_scores = [0.0 for _ in range(self.num_tasks)]

    def posterior(self) -> List[float]:
        return normalize(self.task_scores)

    def ingest(self, event: Event, *, global_step: int, episode: int, timestep: int) -> None:
        posterior = self.posterior()
        updated = normalize([prior * like for prior, like in zip(posterior, event.likelihoods)])

        reason = None
        if event.contradicted_active and event.surprise >= self.revision_threshold:
            updated[event.active_task_before] *= max(1e-6, 1.0 - self.invalidation_penalty * event.surprise)
            updated = normalize(updated)
            reason = "negative_high_surprise"

        self.task_scores = updated
        new_active = max(range(self.num_tasks), key=lambda idx: self.task_scores[idx])
        if reason is not None and new_active != event.active_task_before:
            self.revision_count += 1
            self.pending_revisions.append(
                {
                    "global_step": global_step,
                    "episode": episode,
                    "timestep": timestep,
                    "from_task": event.active_task_before,
                    "to_task": new_active,
                    "surprise": event.surprise,
                    "reason": reason,
                }
            )
        self.active_task = new_active
        self.event_buffer.append(
            {
                "global_step": global_step,
                "episode": episode,
                "timestep": timestep,
                "kind": event.kind,
                "action": event.action,
                "reward": event.reward,
                "support_task": event.support_task,
                "active_task_before": event.active_task_before,
                "active_task_after": self.active_task,
                "surprise": event.surprise,
                "contradicted_active": event.contradicted_active,
            }
        )
        while len(self.event_buffer) > self.event_buffer_size:
            self.event_buffer.popleft()

    def arm_mean(self, task_means: List[List[float]], arm: int) -> float:
        posterior = self.posterior()
        return sum(posterior[t] * task_means[t][arm] for t in range(self.num_tasks))

    def arm_uncertainty(self, task_means: List[List[float]], arm: int) -> float:
        posterior = self.posterior()
        mean = self.arm_mean(task_means, arm)
        variance = sum(posterior[t] * (task_means[t][arm] - mean) ** 2 for t in range(self.num_tasks))
        return math.sqrt(max(variance, 1e-9))

    def snapshot(self, task_means: List[List[float]]) -> dict:
        posterior = self.posterior()
        return {
            "posterior": posterior,
            "active_task": self.active_task,
            "task_scores": self.task_scores[:],
            "event_count": len(self.event_buffer),
            "revision_count": self.revision_count,
            "recent_events": list(self.event_buffer),
            "arm_value_estimates": [self.arm_mean(task_means, arm) for arm in range(len(task_means[0]))],
            "arm_uncertainties": [self.arm_uncertainty(task_means, arm) for arm in range(len(task_means[0]))],
        }

    def drain_revision_events(self) -> List[dict]:
        items = self.pending_revisions[:]
        self.pending_revisions.clear()
        return items

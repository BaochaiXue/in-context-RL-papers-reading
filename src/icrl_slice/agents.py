from __future__ import annotations

import math
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List, Optional

from .compilation import ExperienceCompiler, RevisableMemory, normalize


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
class FilteredHistoryAgent:
    recency: float = 0.95
    optimism: float = 0.08
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
        if reward >= 0.5:
            self.counts[action] += 1
            self.values[action] = self.recency * self.values[action] + (1.0 - self.recency) * reward

    def snapshot(self) -> Dict[str, Optional[float]]:
        return {
            "belief": None,
            "belief_top_task": None,
            "belief_top_prob": None,
            "selected_arm_uncertainty": 1.0 / math.sqrt(self.counts[self.act()] + 1),
        }


@dataclass
class RetrievalProxyAgent:
    window: int = 6
    optimism: float = 0.06
    buffers: Dict[int, Deque[float]] = field(default_factory=dict)
    num_arms: int = 0

    def reset(self, num_arms: int) -> None:
        self.num_arms = num_arms
        self.buffers = {arm: deque(maxlen=self.window) for arm in range(num_arms)}

    def act(self) -> int:
        scores = []
        for arm in range(self.num_arms):
            retrieved = list(self.buffers[arm])
            mean = sum(retrieved) / len(retrieved) if retrieved else 0.5
            bonus = self.optimism / math.sqrt(len(retrieved) + 1)
            scores.append(mean + bonus)
        return max(range(self.num_arms), key=lambda arm: scores[arm])

    def update(self, action: int, reward: float) -> None:
        self.buffers[action].append(reward)

    def snapshot(self) -> Dict[str, Optional[float]]:
        retrieved = list(self.buffers[self.act()])
        uncertainty = 1.0 / math.sqrt(len(retrieved) + 1)
        return {
            "belief": None,
            "belief_top_task": None,
            "belief_top_prob": None,
            "selected_arm_uncertainty": uncertainty,
            "retrieval_size": len(retrieved),
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


@dataclass
class CompiledMemoryAgent:
    task_means: List[List[float]]
    exploration_scale: float = 0.05
    compiler: ExperienceCompiler = field(default_factory=ExperienceCompiler)
    memory: RevisableMemory | None = None
    global_step: int = 0
    episode: int = 0
    timestep: int = 0

    def reset(self, num_arms: int, num_tasks: int) -> None:
        del num_arms
        self.memory = RevisableMemory(num_tasks=num_tasks)
        self.global_step = 0
        self.episode = 0
        self.timestep = 0

    def set_step_context(self, episode: int, timestep: int, global_step: int) -> None:
        self.episode = episode
        self.timestep = timestep
        self.global_step = global_step

    def _arm_mean(self, arm: int) -> float:
        assert self.memory is not None
        return self.memory.arm_mean(self.task_means, arm)

    def _arm_uncertainty(self, arm: int) -> float:
        assert self.memory is not None
        return self.memory.arm_uncertainty(self.task_means, arm)

    def act(self) -> int:
        num_arms = len(self.task_means[0])
        scores = [self._arm_mean(arm) + self.exploration_scale * self._arm_uncertainty(arm) for arm in range(num_arms)]
        return max(range(num_arms), key=lambda arm: scores[arm])

    def update(self, action: int, reward: float) -> None:
        assert self.memory is not None
        posterior = self.memory.posterior()
        event = self.compiler.extract(
            action=action,
            reward=reward,
            task_means=self.task_means,
            posterior=posterior,
            active_task=self.memory.active_task,
        )
        self.memory.ingest(event, global_step=self.global_step, episode=self.episode, timestep=self.timestep)

    def snapshot(self) -> Dict[str, object]:
        assert self.memory is not None
        snapshot = self.memory.snapshot(self.task_means)
        belief = snapshot["posterior"]
        belief_top_task = max(range(len(belief)), key=lambda idx: belief[idx])
        arm = self.act()
        return {
            "belief": belief,
            "belief_top_task": belief_top_task,
            "belief_top_prob": belief[belief_top_task],
            "selected_arm_uncertainty": self._arm_uncertainty(arm),
            "arm_value_estimates": snapshot["arm_value_estimates"],
            "memory_active_task": snapshot["active_task"],
            "memory_event_count": snapshot["event_count"],
            "memory_revision_count": snapshot["revision_count"],
            "compiled_memory": snapshot,
        }

    def drain_revision_events(self) -> List[dict]:
        assert self.memory is not None
        return self.memory.drain_revision_events()


@dataclass
class UncertaintyGatedAgent:
    """Wraps any belief-producing agent with uncertainty-gated abstention.

    When the selected arm's uncertainty exceeds `abstention_threshold`,
    the agent falls back to the arm with lowest uncertainty (safest known action).
    This operationalizes the calibration signals that were previously observational-only.
    """

    inner: object  # Any agent with act(), update(), snapshot()
    abstention_threshold: float = 0.25
    abstention_count: int = 0
    total_decisions: int = 0
    _gated: bool = False  # whether last action was gated

    def reset(self, num_arms: int, num_tasks: int = 0) -> None:
        self.abstention_count = 0
        self.total_decisions = 0
        self._gated = False
        if hasattr(self.inner, 'reset'):
            if num_tasks > 0 and hasattr(self.inner, 'task_means'):
                self.inner.reset(num_arms, num_tasks)
            else:
                self.inner.reset(num_arms)

    def _arm_uncertainties(self) -> List[float]:
        """Get per-arm uncertainties from the inner agent."""
        if hasattr(self.inner, '_arm_uncertainty'):
            num_arms = len(self.inner.task_means[0])
            return [self.inner._arm_uncertainty(arm) for arm in range(num_arms)]
        return []

    def act(self) -> int:
        self.total_decisions += 1
        greedy_action = self.inner.act()

        # Check uncertainty of the greedy arm
        snap = self.inner.snapshot()
        unc = snap.get("selected_arm_uncertainty")

        if unc is not None and unc > self.abstention_threshold:
            # Fall back: pick the arm with LOWEST uncertainty (safest known action)
            arm_uncs = self._arm_uncertainties()
            if arm_uncs:
                safest_arm = min(range(len(arm_uncs)), key=lambda a: arm_uncs[a])
                self.abstention_count += 1
                self._gated = True
                return safest_arm

        self._gated = False
        return greedy_action

    def update(self, action: int, reward: float) -> None:
        self.inner.update(action, reward)

    def set_step_context(self, **kwargs) -> None:
        if hasattr(self.inner, 'set_step_context'):
            self.inner.set_step_context(**kwargs)

    def snapshot(self) -> Dict[str, object]:
        snap = self.inner.snapshot()
        snap["gated"] = self._gated
        snap["abstention_count"] = self.abstention_count
        snap["abstention_rate"] = (
            self.abstention_count / self.total_decisions
            if self.total_decisions > 0
            else 0.0
        )
        return snap

    def drain_revision_events(self) -> List[dict]:
        if hasattr(self.inner, 'drain_revision_events'):
            return self.inner.drain_revision_events()
        return []

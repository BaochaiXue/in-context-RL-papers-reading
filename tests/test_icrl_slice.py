from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from src.icrl_slice.agents import CompiledMemoryAgent, ExplicitStateAgent, OpaqueHistoryAgent
from src.icrl_slice.env import HiddenTaskBandit, default_task_means


class HiddenTaskBanditTests(unittest.TestCase):
    def test_intervention_changes_hidden_task(self) -> None:
        env = HiddenTaskBandit(seed=7)
        env.reset(task_id=0)
        env.intervene(1)
        _, info = env.step(0)
        self.assertEqual(info["task_id"], 1)

    def test_default_task_means_rotate_best_arm(self) -> None:
        means = default_task_means(3, 5)
        bests = [row.index(max(row)) for row in means]
        self.assertEqual(bests, [0, 1, 2])


class AgentTests(unittest.TestCase):
    def test_explicit_agent_emits_belief_fields(self) -> None:
        means = default_task_means(3, 5)
        agent = ExplicitStateAgent(task_means=means)
        agent.reset(num_arms=5, num_tasks=3)
        snapshot = agent.snapshot()
        self.assertIn("belief", snapshot)
        self.assertIsNotNone(snapshot["belief_top_prob"])

    def test_opaque_agent_updates_counts(self) -> None:
        agent = OpaqueHistoryAgent()
        agent.reset(num_arms=5)
        action = agent.act()
        agent.update(action, 1.0)
        self.assertGreater(agent.counts[action], 0)

    def test_compiled_memory_agent_emits_memory_fields(self) -> None:
        means = default_task_means(3, 3)
        agent = CompiledMemoryAgent(task_means=means)
        agent.reset(num_arms=3, num_tasks=3)
        agent.set_step_context(episode=0, timestep=0, global_step=0)
        agent.update(action=0, reward=0.0)
        snapshot = agent.snapshot()
        self.assertIn("compiled_memory", snapshot)
        self.assertIn("memory_revision_count", snapshot)
        self.assertIn("memory_event_count", snapshot)

    def test_compiled_memory_agent_records_revision_event(self) -> None:
        means = default_task_means(3, 3)
        agent = CompiledMemoryAgent(task_means=means)
        agent.reset(num_arms=3, num_tasks=3)
        agent.set_step_context(episode=0, timestep=0, global_step=0)
        agent.update(action=0, reward=0.0)
        revisions = agent.drain_revision_events()
        self.assertTrue(revisions)


class EndToEndTests(unittest.TestCase):
    def test_smoke_run_writes_required_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            outdir = Path(tmpdir) / "artifacts"
            cmd = [
                sys.executable,
                "-m",
                "icrl_slice.run",
                "--seeds",
                "4",
                "--episodes",
                "8",
                "--horizon",
                "8",
                "--output-dir",
                str(outdir),
            ]
            env = {"PYTHONPATH": "src"}
            subprocess.run(cmd, cwd=Path(__file__).resolve().parents[1], check=True, env=env)
            required = [
                outdir / "summary.json",
                outdir / "per_seed_metrics.json",
                outdir / "transitions.jsonl",
                outdir / "calibration.csv",
                outdir / "memory_contents.jsonl",
                outdir / "revision_events.jsonl",
                outdir / "smoke_check.txt",
            ]
            for path in required:
                self.assertTrue(path.exists(), path)
            summary = json.loads((outdir / "summary.json").read_text())
            self.assertIn("explicit_state", summary["aggregate"])
            self.assertIn("opaque_history", summary["aggregate"])
            self.assertIn("compiled_memory", summary["aggregate"])
            self.assertIn("scope", summary)
            self.assertTrue(summary["scope"]["default_config_is_narrowed"])
            self.assertTrue(summary["scope"]["compiled_memory_is_bounded_proxy"])


if __name__ == "__main__":
    unittest.main()

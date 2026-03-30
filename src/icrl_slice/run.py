from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path

from .agents import CompiledMemoryAgent, ExplicitStateAgent, FilteredHistoryAgent, OpaqueHistoryAgent, RetrievalProxyAgent
from .env import HiddenTaskBandit, default_task_means
from .metrics import is_finite_metric, summarize_agent, write_json


LOGGER = logging.getLogger("icrl_slice")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the bounded experience-compilation slice.")
    parser.add_argument("--seeds", type=int, default=16)
    parser.add_argument("--episodes", type=int, default=24)
    parser.add_argument("--horizon", type=int, default=20)
    parser.add_argument("--arms", type=int, default=3)
    parser.add_argument("--shift-episode", type=int, default=12)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--log-level", default="INFO")
    return parser


def task_schedule(episodes: int, shift_episode: int, num_tasks: int) -> list[int]:
    first = 0
    second = 1 % num_tasks
    return [first if e < shift_episode else second for e in range(episodes)]


def run_agent(agent_name: str, agent, args, task_means, seed: int) -> tuple[list[dict], dict]:
    num_tasks = len(task_means)
    env = HiddenTaskBandit(
        num_arms=args.arms,
        num_tasks=num_tasks,
        horizon=args.horizon,
        task_means=task_means,
        seed=seed,
    )
    if agent_name == "explicit_state":
        agent.reset(args.arms, num_tasks)
    elif agent_name == "compiled_memory":
        agent.reset(args.arms, num_tasks)
    else:
        agent.reset(args.arms)

    schedule = task_schedule(args.episodes, args.shift_episode, num_tasks)
    transitions: list[dict] = []
    memory_rows: list[dict] = []
    revision_rows: list[dict] = []
    global_step = 0
    for episode in range(args.episodes):
        task_id = schedule[episode]
        env.reset(task_id=task_id)
        shifted = episode >= args.shift_episode
        for timestep in range(args.horizon):
            if hasattr(agent, "set_step_context"):
                agent.set_step_context(episode=episode, timestep=timestep, global_step=global_step)
            action = agent.act()
            reward, info = env.step(action)
            agent.update(action, reward)
            snap = agent.snapshot()
            belief = snap.get("belief")
            transitions.append(
                {
                    "seed": seed,
                    "agent": agent_name,
                    "episode": episode,
                    "timestep": timestep,
                    "global_step": global_step,
                    "task_id": info["task_id"],
                    "shifted": shifted,
                    "action": action,
                    "reward": reward,
                    "optimal_arm": info["optimal_arm"],
                    "regret": info["optimal_mean"] - info["chosen_mean"],
                    "belief": belief,
                    "belief_top_task": snap.get("belief_top_task"),
                    "belief_top_prob": snap.get("belief_top_prob"),
                    "selected_arm_uncertainty": snap.get("selected_arm_uncertainty"),
                    "memory_active_task": snap.get("memory_active_task"),
                    "memory_event_count": snap.get("memory_event_count"),
                    "memory_revision_count": snap.get("memory_revision_count"),
                }
            )
            if "compiled_memory" in snap:
                memory_rows.append(
                    {
                        "seed": seed,
                        "agent": agent_name,
                        "episode": episode,
                        "timestep": timestep,
                        "global_step": global_step,
                        **snap["compiled_memory"],
                    }
                )
            if hasattr(agent, "drain_revision_events"):
                for item in agent.drain_revision_events():
                    revision_rows.append({"seed": seed, "agent": agent_name, **item})
            global_step += 1
    metrics = summarize_agent(transitions, num_tasks)
    metrics["memory_rows"] = len(memory_rows)
    metrics["revision_rows"] = len(revision_rows)
    return transitions, memory_rows, revision_rows, metrics


def write_transitions(path: Path, rows: list[dict]) -> None:
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def write_calibration_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["seed", "agent", "global_step", "task_id", "belief_top_task", "belief_top_prob", "belief_correct"],
        )
        writer.writeheader()
        for row in rows:
            if row["belief_top_prob"] is None:
                continue
            writer.writerow(
                {
                    "seed": row["seed"],
                    "agent": row["agent"],
                    "global_step": row["global_step"],
                    "task_id": row["task_id"],
                    "belief_top_task": row["belief_top_task"],
                    "belief_top_prob": row["belief_top_prob"],
                    "belief_correct": int(row["belief_top_task"] == row["task_id"]),
                }
            )


def write_smoke_check(path: Path, summary: dict) -> None:
    required_agents = {"explicit_state", "opaque_history", "filtered_history", "retrieval_proxy", "compiled_memory"}
    present_agents = set(summary["aggregate"])
    finite = all(is_finite_metric(v) for metrics in summary["aggregate"].values() for v in metrics.values())
    explicit_has_belief = summary["aggregate"]["explicit_state"]["belief_brier_score"] is not None
    compiled_has_memory = summary["aggregate"]["compiled_memory"]["memory_event_count"] > 0
    compiled_has_revisions = summary["aggregate"]["compiled_memory"]["revision_count"] > 0
    lines = [
        f"agents_present={present_agents == required_agents}",
        f"metrics_finite={finite}",
        f"explicit_has_belief_metric={explicit_has_belief}",
        f"compiled_has_memory={compiled_has_memory}",
        f"compiled_has_revisions={compiled_has_revisions}",
        f"compiled_better_than_raw_history={summary['comparison']['compiled_memory_better_than_raw_history_on_regret']}",
    ]
    path.write_text("\n".join(lines) + "\n")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    task_means = default_task_means(args.arms, args.arms)
    LOGGER.info("Running bounded experience-compilation slice with task means: %s", task_means)

    per_seed_metrics = []
    all_rows: list[dict] = []
    all_memory_rows: list[dict] = []
    all_revision_rows: list[dict] = []
    for seed in range(args.seeds):
        explicit_agent = ExplicitStateAgent(task_means=task_means)
        opaque_agent = OpaqueHistoryAgent()
        filtered_agent = FilteredHistoryAgent()
        retrieval_agent = RetrievalProxyAgent()
        compiled_agent = CompiledMemoryAgent(task_means=task_means)
        for agent_name, agent in [
            ("explicit_state", explicit_agent),
            ("opaque_history", opaque_agent),
            ("filtered_history", filtered_agent),
            ("retrieval_proxy", retrieval_agent),
            ("compiled_memory", compiled_agent),
        ]:
            rows, memory_rows, revision_rows, metrics = run_agent(agent_name, agent, args, task_means, seed)
            per_seed_metrics.append({"seed": seed, "agent": agent_name, **metrics})
            all_rows.extend(rows)
            all_memory_rows.extend(memory_rows)
            all_revision_rows.extend(revision_rows)

    aggregate = {}
    for agent_name in ["explicit_state", "opaque_history", "filtered_history", "retrieval_proxy", "compiled_memory"]:
        rows = [row for row in per_seed_metrics if row["agent"] == agent_name]
        aggregate[agent_name] = {
            key: sum(float(r[key]) for r in rows if r[key] is not None) / len([r for r in rows if r[key] is not None])
            if any(r[key] is not None for r in rows)
            else None
            for key in [
                "cumulative_regret",
                "average_reward",
                "optimal_action_rate",
                "belief_brier_score",
                "mean_selected_arm_uncertainty",
                "shift_recovery_steps",
                "revision_count",
                "memory_event_count",
                "memory_rows",
                "revision_rows",
            ]
        }

    summary = {
        "config": {
            "seeds": args.seeds,
            "episodes": args.episodes,
            "horizon": args.horizon,
            "arms": args.arms,
                "tasks": len(task_means),
                "shift_episode": args.shift_episode,
            },
        "scope": {
            "covers": ["aim1_explicit_state", "aim2_bounded_experience_compilation_proxy", "aim3_partial_calibration_proxy"],
            "does_not_cover": ["universal_context_compiler", "safe_action_policy", "embodied_validation"],
            "default_config_is_narrowed": True,
            "explicit_state_knows_task_family": True,
            "baseline_is_simple_history_heuristic": True,
            "compiled_memory_is_bounded_proxy": True,
            "retrieval_proxy_is_simple": True,
        },
        "aggregate": aggregate,
        "comparison": {
            "explicit_state_better_on_regret": aggregate["explicit_state"]["cumulative_regret"]
            < aggregate["opaque_history"]["cumulative_regret"],
            "explicit_state_better_on_reward": aggregate["explicit_state"]["average_reward"]
            > aggregate["opaque_history"]["average_reward"],
            "compiled_memory_better_than_raw_history_on_regret": aggregate["compiled_memory"]["cumulative_regret"]
            < aggregate["opaque_history"]["cumulative_regret"],
            "compiled_memory_better_than_filtered_history_on_regret": aggregate["compiled_memory"]["cumulative_regret"]
            < aggregate["filtered_history"]["cumulative_regret"],
            "compiled_memory_better_than_retrieval_proxy_on_regret": aggregate["compiled_memory"]["cumulative_regret"]
            < aggregate["retrieval_proxy"]["cumulative_regret"],
        },
        "limitations": [
            "compiled_memory is a bounded event-driven proxy, not a universal context compiler",
            "compiled_memory and explicit_state both know the candidate task family in advance",
            "uncertainty remains observational only and does not gate actions",
        ],
    }

    write_json(args.output_dir / "summary.json", summary)
    write_json(args.output_dir / "per_seed_metrics.json", per_seed_metrics)
    write_transitions(args.output_dir / "transitions.jsonl", all_rows)
    write_calibration_csv(args.output_dir / "calibration.csv", all_rows)
    write_jsonl(args.output_dir / "memory_contents.jsonl", all_memory_rows)
    write_jsonl(args.output_dir / "revision_events.jsonl", all_revision_rows)
    write_smoke_check(args.output_dir / "smoke_check.txt", summary)
    LOGGER.info("Artifacts written to %s", args.output_dir)


if __name__ == "__main__":
    main()

# Generalization to New Sequential Decision Making Tasks with In-Context Learning

- Paper folder: `papers/Generalization to New Sequential Decision Making Tasks with In-Context Learning`
- Note slug: `generalization-to-new-sequential-decision-making-tasks-with-in-context-learning`

## Full citation
Sharath Chandra Raparthy, Eric Hambro, Robert Kirk, Mikael Henaff, Roberta Raileanu. Generalization to New Sequential Decision Making Tasks with In-Context Learning. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/Generalization to New Sequential Decision Making Tasks with In-Context Learning/paper.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: Training autonomous agents that can learn new tasks from only a handful of demonstrations is a long-standing problem in machine learning. Recently, transformers have been shown to learn new language or vision tasks without any weight updates from only a few examples, also referred to as in-context learning.
- Core mechanism: 提出用 bursty multi-trajectory expert sequences 训练 Transformer，实现跨任务 few-shot imitation。
- Primary bottleneck: 关键依赖是 trajectory burstiness、任务多样性与大规模 expert 数据；顺序决策对单次错误容忍度很低。
- Evaluated on: 在 MiniHack 与 Procgen 上，对比 single-trajectory Transformer 与 hashmap baseline，指标是 held-out task 表现。
- Key failure mode: 作者明确指出环境随机性和低容错是主要失败源；一旦进入 unseen 且不可恢复状态，纯上下文方法容易崩。

## Problem setting
Training autonomous agents that can learn new tasks from only a handful of demonstrations is a long-standing problem in machine learning. Recently, transformers have been shown to learn new language or vision tasks without any weight updates from only a few examples, also referred to as in-context learning. However, the sequential decision making setting poses additional challenges having a lower tolerance for errors since the environment's stochasticity or the agent's actions can lead to unseen, and sometimes unrecoverable, states.

## Method summary
提出用 bursty multi-trajectory expert sequences 训练 Transformer，实现跨任务 few-shot imitation。 figure [t] figures/setup.png Experimental Setup: We create a dataset of expert trajectories by rolling out expert policies on tasks. Given these expert trajectories, we construct multi-trajectory sequences with trajectory burstiness . A sequence is bursty when there are at least two trajectories in the sequence from the same level. However, note that these trajectories are typically different due to the environment's stochasticity.

## Datasets / tasks / benchmarks
在 MiniHack 与 Procgen 上，对比 single-trajectory Transformer 与 hashmap baseline，指标是 held-out task 表现。

## Strongest results
We next illustrate the in-context learning abilities of the multi-trajectory transformer on unseen MiniHack and Procgen tasks, and compare against single-trajectory and hashmap-based baselines. While many previous works have studied generalization to new levels, to our knowledge we are the first to study generalization to completely different tasks, and we demonstrate promising results. Baselines : We compare against two baselines. Hashmap (HM): employs a hashmap over states in order to take the action corresponding to the same state from context (i.e., the expert action).

## Failure modes or limitations
作者明确指出环境随机性和低容错是主要失败源；一旦进入 unseen 且不可恢复状态，纯上下文方法容易崩。

## Evidence anchors
- Introduction
- Background
- Methodology
- Training Data
- Model Training and Evaluation
- Motivating Experiment
- Experiments
- Main Results
- MiniHack
- Procgen
- Detailed Analysis on MiniHack
- Effect of Trajectory Burstiness
- Effect of Environment Stochasticity
- Effect of Dataset Size
- Effect of Model Size
- Effect of Task Diversity
- Investigating Failure Modes
- Related Work
- Conclusion and Future Work
- Experimental Setup
- Model Details
- Compute
- Environment Details
- MiniHack
- Procgen
- Dataset Details
- Additional Results
- Impact of Reward Tokens
- Training Results
- MiniHack
- Procgen
- Task Diversity Results
- Procgen Sticky Action Results
- Broader Impact
- Hyperparameters

## Tags
`benchmark` `transformers` `meta-rl` `memory` `action-models` `sequence-modeling`

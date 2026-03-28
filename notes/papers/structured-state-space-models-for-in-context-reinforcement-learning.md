# Structured State Space Models for In-Context Reinforcement Learning

- Paper folder: `papers/Structured State Space Models for In-Context Reinforcement Learning`
- Note slug: `structured-state-space-models-for-in-context-reinforcement-learning`

## Full citation
Chris Lu, Yannick Schroecker, Albert Gu, Emilio Parisotto, Jakob Foerster, Satinder Singh, Feryal Behbahani. Structured State Space Models for In-Context Reinforcement Learning. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Structured State Space Models for In-Context Reinforcement Learning/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Structured state space sequence (S4) models have recently achieved state-of-the-art performance on long-range sequence modeling tasks. These models also have fast inference speeds and parallelisable training, making them potentially useful in many reinforcement learning settings.
- Core mechanism: 把可重置的 S5 状态空间模型接入 RL，获得长序列更快的推理和并行训练。
- Primary bottleneck: 关键难点在于如何把 state-space hidden state reset/parallelize 到 RL 训练管线中。
- Evaluated on: 在 bsuite/T-maze、POPGym 和 random-projection meta-learning 环境上，与 RNN 和 Transformer 比速度与表现。
- Key failure mode: 若任务本身不需要长程记忆，S5 相对 attention 的优势会缩小；工程集成成本也不低。

## Problem setting
Structured state space sequence (S4) models have recently achieved state-of-the-art performance on long-range sequence modeling tasks. These models also have fast inference speeds and parallelisable training, making them potentially useful in many reinforcement learning settings. We propose a modification to a variant of S4 that enables us to initialise and reset the hidden state in parallel, allowing us to tackle reinforcement learning tasks.

## Method summary
把可重置的 S5 状态空间模型接入 RL，获得长序列更快的推理和并行训练。 algorithm [t] Pseudocode for the Multi-Environment Meta-Learning environment step. algorithmic [1] Distribution of environments , a fixed output observation dimension size , and a fixed action dimension size . Agent action and Environment termination StepEnvironment( , ) the environment terminated ( ) Sample random environment Initialise random observation projection matrix where is 's observation size Initialise random action projection matrix where is 's action size Reset to receive an initial observation Apply the random observation projection matrix to the observation Append and to to get Return Apply the projection matrix Step using to receive the next observation , reward , and done signal . Apply the projection matrix Append and to to get Return , , and algorithmic algorithm We first modify to S5 to handle variable-length sequences, which makes the architecture more suitable for tackling POMDPs.

## Datasets / tasks / benchmarks
在 bsuite/T-maze、POPGym 和 random-projection meta-learning 环境上，与 RNN 和 Transformer 比速度与表现。

## Strongest results
Memory Length Environment First, we demonstrate our modified S5's improved training speeds in performance in the extremely simple memory length environment proposed in bsuite~ . The environment is based on the well-known `t-maze` environment~ in which the agent receives a cue on the first timestep, which corresponds to the action the agent should take some number of steps in the future to receive a reward. We run our experiments using bsuite's actor-critic baseline while swapping out the LSTM for Transformer self-attention blocks or S5 blocks~ and using Gymnax for faster environment rollouts~ . We show the results in Figure REF.

## Failure modes or limitations
若任务本身不需要长程记忆，S5 相对 attention 的优势会缩小；工程集成成本也不低。

## Evidence anchors
- Introduction
- Background
- Structured State Space Sequence Models
- Reinforcement Learning
- Method
- Resettable S5
- Multi-Environment Meta-Learning with Random Projections
- Experiments
- Memory Length Environment
- POPGym Environments
- Randomly-Projected CartPole In-Context
- Multi-Environment Meta-Reinforcement Learning
- Related Work
- Conclusion and Limitations
- Proof of Associativity of Binary Operator
- Hyperparameters
- POPGym Discussion

## Tags
`benchmark` `transformers` `sequence-models` `meta-rl` `memory` `action-models` `icrl` `systems`

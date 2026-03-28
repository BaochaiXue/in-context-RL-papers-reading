# Vintix Action Model Via In Context Reinforcement Learning

- Paper folder: `papers/Vintix Action Model via In-Context Reinforcement Learning`
- Note slug: `vintix-action-model-via-in-context-reinforcement-learning`

## Full citation
Authors could not be extracted reliably from the local source. Vintix Action Model Via In Context Reinforcement Learning. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Vintix Action Model via In-Context Reinforcement Learning/example_paper.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: In-Context Reinforcement Learning (ICRL) represents a promising paradigm for developing generalist agents that learn at inference time through trial-and-error interactions, analogous to how large language models adapt contextually, but with a focus on reward maximization. However, the scalability of ICRL beyond toy tasks and single-domain settings remains an open challenge.
- Core mechanism: 把 Algorithm Distillation 推到跨域 action model，上面再加 continuous noise distillation 降低数据采集成本。
- Primary bottleneck: 跨域统一表示与数据质量是核心瓶颈；方法仍只是把 ICRL 扩展到少数域的第一步。
- Evaluated on: 在 Meta-World ML45、Bi-DexHands、Industrial Benchmark 上，与 demonstrator/expert distillation 风格 action model 对比。
- Key failure mode: 目前最强的自我修正仍集中在训练样式接近的域；更广泛 generalist transfer 仍是开放问题。

## Problem setting
In-Context Reinforcement Learning (ICRL) represents a promising paradigm for developing generalist agents that learn at inference time through trial-and-error interactions, analogous to how large language models adapt contextually, but with a focus on reward maximization. However, the scalability of ICRL beyond toy tasks and single-domain settings remains an open challenge. In this work, we present the first steps toward scaling ICRL by introducing a fixed, cross-domain model capable of learning behaviors through in-context reinforcement learning.

## Method summary
把 Algorithm Distillation 推到跨域 action model，上面再加 continuous noise distillation 降低数据采集成本。 At the core of our approach ( fig:method-verview ) is Algorithm Distillation , a two-step Offline Meta-RL algorithm. The first step involves collecting ordered training histories from base reinforcement learning (RL) algorithms, while the second step involves a decoder-only transformer trained solely for the next-action prediction. This approach facilitates in-context learning by effectively distilling the policy improvement operator into a causal sequence model. We further propose two augmentations to this technique: (1) democratizing the data collection process by introducing a continuous extension of the noise-distillation procedure by ; (2) conducting generalist agent-style cross-domain training on the acquired dataset.

## Datasets / tasks / benchmarks
在 Meta-World ML45、Bi-DexHands、Industrial Benchmark 上，与 demonstrator/expert distillation 风格 action model 对比。

## Strongest results
Inference-Time Self-Correction on Training Tasks First, we aim to verify whether the Vintix model has the capability for context-based inference-time adaptation through self-correction. To achieve this, we deploy the model on training tasks (ML45 split for Meta-World, ML20 split for Bi-DexHands and setpoints for Industrial-Benchmark) by iteratively unrolling its actions in a cold-start manner, beginning with an empty initial context. fig:expertise illustrates that the model progressively improves its policy in each domain as the number of shots (episodes played) increases. The agent starts with a suboptimal performance and gradually self-corrects by inferring task-related information from the accumulated context, ultimately reaching near-demonstrator-level performance.

## Failure modes or limitations
目前最强的自我修正仍集中在训练样式接近的域；更广泛 generalist transfer 仍是开放问题。

## Evidence anchors
- Introduction
- Approach
- Continuous Noise Distillation
- Cross-Domain Dataset
- Training and Inference Pipeline
- Model architecture
- Training
- Inference
- Results
- Inference-Time Self-Correction on Training Tasks
- Comparison to Related Action Models
- Generalization Analysis
- Related Work
- Conclusion and Future Work
- Impact Statement
- Dataset Details
- General Information
- Train vs. Test Tasks Split
- MuJoCo
- Meta-World
- Bi-DexHands
- Industrial-Benchmark
- Epsilon Decay Functions
- Demonstrators
- Training
- Additional Experiments
- Is Algorithm Distillation More Effective Than Expert Distillation?
- Does Vintix Performs In-Context Reinforcement Learning?
- Hyperparameters
- Task-Level Dataset Visualization
- Inference Time Performance Graphs
- Dataset Size and Metadata
- Task-Level Performance
- Comparison with other cross-domain agents

## Tags
`benchmark` `llm` `transformers` `meta-rl` `offline-rl` `memory` `action-models` `icrl`

# Towards Large-Scale In-Context Reinforcement Learning by Meta-Training in Randomized Worlds

- Paper folder: `papers/OmniRL In-Context Reinforcement Learning by Large-Scale Meta-Training in Randomized Worlds`
- Note slug: `omnirl-in-context-reinforcement-learning-by-large-scale-meta-training-in-randomized-worlds`

## Full citation
Fan Wang, Pengtao Shao, Yiming Zhang, Shaoshan Liu, Ning Ding, Yang Cao, Yu Kang, Haifeng Wang. Towards Large-Scale In-Context Reinforcement Learning by Meta-Training in Randomized Worlds. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/OmniRL In-Context Reinforcement Learning by Large-Scale Meta-Training in Randomized Worlds/neurips_final.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: In-Context Reinforcement Learning (ICRL) enables agents to learn automatically and on-the-fly from their interactive experiences. However, a major challenge in scaling up ICRL is the lack of scalable task collections.
- Core mechanism: 提出 AnyMDP 和 decoupled policy distillation，在大规模随机 MDP 上做可扩展 supervised ICRL。
- Primary bottleneck: 训练-推理轨迹分布差异仍是根问题；增加任务多样性会换来更慢的适应过程。
- Evaluated on: 在 AnyMDP、Garnet、Gymnasium、DarkRoom、bandits 上，对比 tuned PPO、Q-learning/UCB 等基线。
- Key failure mode: 摘要就指出泛化可能以“更长适应期”为代价；few-shot 反而可能因任务多样性提高而变差。

## Problem setting
In-Context Reinforcement Learning (ICRL) enables agents to learn automatically and on-the-fly from their interactive experiences. However, a major challenge in scaling up ICRL is the lack of scalable task collections. To address this, we propose the procedurally generated tabular Markov Decision Processes, named AnyMDP .

## Method summary
提出 AnyMDP 和 decoupled policy distillation，在大规模随机 MDP 上做可扩展 supervised ICRL。

## Datasets / tasks / benchmarks
在 AnyMDP、Garnet、Gymnasium、DarkRoom、bandits 上，对比 tuned PPO、Q-learning/UCB 等基线。

## Strongest results
Demonstration of Generalization and Scalability table [t] Comparison of best average episodic performance within 10,000 episodes for each learner. The episode performances are normalized to a scale of (uniform random policy) to (oracle policy). The minimum steps and episodes required to achieve within at least of the best episodic performances are also listed. The hyper-parameters for Q-Learning and PPO are optimized under the evaluated task or task set.

## Failure modes or limitations
摘要就指出泛化可能以“更长适应期”为代价；few-shot 反而可能因任务多样性提高而变差。

## Evidence anchors
- Introduction
- Related Work
- Emergence of In-Context Learning
- In-Context Reinforcement Learning
- Procedurally Generated Tasks
- AnyMDP: Procedural Generation of High-Quality MDP Tasks
- Problem Setting and Definitions
- Motivations of AnyMDP
- Comparison with Other Procedural MDPs and Empirical Validation
- The Scalable ICRL Framework of OmniRL
- Experiments
- Demonstration of Generalization and Scalability
- OmniRL Performs Both Offline and Online Learning Better
- Emergence of General-Purpose ICRL by Increasing Task Number
- Conclusions and Discussions
- NeurIPS Paper Checklist
- Notations
- Additional Information on AnyMDP
- Proof of ; cref theory:mc
- Details of Procedural Generation
- Additional Properties of AnyMDP
- Additional Information on Experiment Settings
- Data Synthesis
- Meta-Training Details
- Evaluation Details
- Additional Empirical Results
- AnyMDP as a long-context benchmark for procedural memory
- OmniRL achieves automatic trade-off between exploration and exploitation
- Additional Evaluation on Gymnasium
- Memory states in ICRL implicitly encode the task structure
- Comparison with Pre-trained LLMs

## Tags
`benchmark` `llm` `meta-rl` `exploration` `bandits` `offline-rl` `memory` `theory`

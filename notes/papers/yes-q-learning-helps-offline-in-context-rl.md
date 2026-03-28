# Yes, Q-learning Helps Offline In-Context RL

- Paper folder: `papers/Yes, Q-learning Helps Offline In-Context RL`
- Note slug: `yes-q-learning-helps-offline-in-context-rl`

## Full citation
Denis Tarasov, Alexander Nikulin, Ilya Zisman, Albina Klepach, Andrei Polubarov, Nikita Lyubaykin, Alexander Derevyagin, Igor Kiselev, Vladislav Kurenkov. Yes, Q-learning Helps Offline In-Context RL. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Yes, Q-learning Helps Offline In-Context RL/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Existing offline in-context reinforcement learning (ICRL) methods have predominantly relied on supervised training objectives, which are known to have limitations in offline RL settings. In this study, we explore the integration of RL objectives within an offline ICRL framework.
- Core mechanism: 在 AD backbone 上加入 offline RL 目标（IC-DQN/CQL/IQL 等），证明 value learning 比纯 imitation 更合适。
- Primary bottleneck: 仍然受离线数据覆盖度和超参数敏感性约束，无法绕开 offline RL 的根本问题。
- Evaluated on: 在 150+ GridWorld/MuJoCo 派生数据集和 XLand-MiniGrid 上，与 AD、DQN、CQL、IQL 等比较 NAUC、最终分数与性能曲线。
- Key failure mode: 论文专门分析了 coverage、history 可得性和 OOD dynamics；覆盖差或缺少多 history 时依然很难。

## Problem setting
Existing offline in-context reinforcement learning (ICRL) methods have predominantly relied on supervised training objectives, which are known to have limitations in offline RL settings. In this study, we explore the integration of RL objectives within an offline ICRL framework. Through experiments on more than 150 GridWorld and MuJoCo environment-derived datasets, we demonstrate that optimizing RL objectives directly improves performance by approximately 30\% on average compared to widely adopted Algorithm Distillation (AD), across various dataset coverages, structures, expertise levels, and environmental complexities.

## Method summary
在 AD backbone 上加入 offline RL 目标（IC-DQN/CQL/IQL 等），证明 value learning 比纯 imitation 更合适。 RL Incorporation figure* subfigure [b] 0.8 imgs/schema_v4.pdf subfigure Overview of the proposed approach. As the input, our model takes a sequence of trajectories (without hard requirements on their structure) where each transition is represented with a tuple consisting of previous action, previous reward, previous episode's done flag, current episode timestep and other sequence elements marked by different timestep subscripts ( and ) to indicate their potential origin from distinct trajectories. Then the resulting context embedding is used to predict both value functions and the policy output . The V-head is employed only in IQL, while the head is used exclusively for continuous actions.

## Datasets / tasks / benchmarks
在 150+ GridWorld/MuJoCo 派生数据集和 XLand-MiniGrid 上，与 AD、DQN、CQL、IQL 等比较 NAUC、最终分数与性能曲线。

## Strongest results
We begin this section by comparing the overall performance of the selected methods using discrete environments, demonstrating the suitability of the newly introduced NAUC metric for evaluation. Subsequently, we analyze the performance of these methods across critical offline RL dimensions, including data quality and coverage. Further, we investigate the impact of removing the assumption of access to learning histories, which may not always hold in real-world scenarios . In addition, we conduct the experiment in a challenging XLand-MiniGrid environment.

## Failure modes or limitations
论文专门分析了 coverage、history 可得性和 OOD dynamics；覆盖差或缺少多 history 时依然很难。

## Evidence anchors
- Introduction
- Preliminaries
- Offline In-Context Reinforcement Learning
- Algorithm Distillation
- Methodology
- RL Incorporation
- Environments and Datasets
- Evaluation
- Experimental Results
- Overall performance
- Various Coverage
- Various Expertise
- Absence of the Learning History Structure
- Evaluation on the XLand-Minigrid Environment
- Continuous State and Action Spaces
- Conclusion and Limitations
- Related Work
- Offline Reinforcement Learning
- In-Context Reinforcement Learning
- Additional Experiments with Mixture of Dynamics
- Future Work
- Additional Experimental Details
- Implementation Details
- Hyperparameters Choice
- Datasets details
- Data Collection
- Learning Curves
- Datasets Statistics
- Hyperparameters
- Additional Plots and Metrics
- Overall Performance
- Various Expertise Performance
- No Learning Histories Structure
- Tabular Results
- Discrete Train NAUC
- Discrete Test NAUC
- Discrete Train Final Scores
- Discrete Test Final Scores
- Continuous Test NAUC
- Continuous Test 0-shot
- Continuous Test Final Scores
- Janus Test NAUC Tables

## Tags
`benchmark` `meta-rl` `exploration` `offline-rl` `memory` `action-models` `icrl` `sequence-modeling`

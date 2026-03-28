# A Survey of In-Context Reinforcement Learning

- Paper folder: `papers/A Survey of In-Context Reinforcement Learning`
- Note slug: `a-survey-of-in-context-reinforcement-learning`

## Full citation
Amir Moeini, Jiuqi Wang, Jacob Beck, Shimon Whiteson, Rohan Chandra, Shangtong Zhang. A Survey of In-Context Reinforcement Learning. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/A Survey of In-Context Reinforcement Learning/ijcai25.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.
- Inventory status: This paper folder contains no local PDF files, so it has no rows in `notes/tables/paper_inventory.csv`; the note is source-only.

## 5-bullet thesis
- Addresses: Reinforcement learning (RL) agents typically optimize their policies by performing expensive backward passes to update their network parameters. However, some agents can solve new tasks without updating any parameters by simply conditioning on additional context such as their action-observation histories.
- Core mechanism: 建立 ICRL 的统一综述框架，按预训练方式、测试时上下文、理论与架构系统梳理整个方向。
- Primary bottleneck: 不是新算法；它指出领域缺少统一理论、统一大规模 benchmark，以及 memory 与 meta-learning 的清晰分离。
- Evaluated on: 综述论文，不提出新数据集；总结常用 benchmark 包括 bandit、DarkRoom、MiniWorld、XLand 等，核心对比对象是 AD、DPT、meta-RL 与长上下文架构。
- Key failure mode: 指出现有结果多停留在 toy benchmark，复杂真实环境、OOD 泛化、安全性和机制解释仍明显不足。

## Problem setting
Reinforcement learning (RL) agents typically optimize their policies by performing expensive backward passes to update their network parameters. However, some agents can solve new tasks without updating any parameters by simply conditioning on additional context such as their action-observation histories. This paper surveys work on such behavior, known as in-context reinforcement learning.

## Method summary
建立 ICRL 的统一综述框架，按预训练方式、测试时上下文、理论与架构系统梳理整个方向。

## Datasets / tasks / benchmarks
综述论文，不提出新数据集；总结常用 benchmark 包括 bandit、DarkRoom、MiniWorld、XLand 等，核心对比对象是 AD、DPT、meta-RL 与长上下文架构。

## Strongest results
This paper presented the first comprehensive survey of ICRL, an emerging and flourishing area. We surveyed ICRL from different aspects, including both pretraining and testing, both empirical and theoretical analyses. We hope this survey will stimulate the growth of the ICRL community.

## Failure modes or limitations
指出现有结果多停留在 toy benchmark，复杂真实环境、OOD 泛化、安全性和机制解释仍明显不足。

## Evidence anchors
- Introduction
- Background
- Supervised Pretraining
- Reinforcement Pretraining
- Test Time Context
- Test Time Performance
- Theory
- Architectures
- Open Problems and Opportunities
- Conclusion
- Acknowledgements

## Tags
`survey` `benchmark` `meta-rl` `bandits` `memory` `theory` `action-models` `icrl`

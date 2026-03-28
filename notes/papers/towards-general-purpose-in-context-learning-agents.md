# Towards General Purpose In Context Learning Agents

- Paper folder: `papers/Towards General-Purpose In-Context Learning Agents`
- Note slug: `towards-general-purpose-in-context-learning-agents`

## Full citation
Authors could not be extracted reliably from the local source. Towards General Purpose In Context Learning Agents. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `pdf-only`
- Metadata source: `cache/papers/Towards General-Purpose In-Context Learning Agents.txt`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: Reinforcement Learning (RL) algorithms are usually hand-crafted, driven by the research and engineering of humans. An alternative approach is to automate this research process via meta-learning.
- Core mechanism: GLA 试图从丰富任务分布的离线经验里，直接发现可跨域泛化的 in-context RL 算法。
- Primary bottleneck: 核心限制是环境分布必须足够丰富，而且训练数据需要包含逐步改进的行为历史。
- Evaluated on: 在多类 RL 环境和随机投影任务上，对比先前 memory-based/meta-RL 方法的泛化。
- Key failure mode: 如果任务分布不够广，学到的“算法”就只是 domain-specific heuristic，跨域泛化会崩。

## Problem setting
Reinforcement Learning (RL) algorithms are usually hand-crafted, driven by the research and engineering of humans. An alternative approach is to automate this research process via meta-learning. A particularly ambitious objective is to automatically discover new RL algorithms from scratch that use in-context learning to learn-how-to-learn entirely from data while also generalizing to a wide range of environments.

## Method summary
GLA 试图从丰富任务分布的离线经验里，直接发现可跨域泛化的 in-context RL 算法。

## Datasets / tasks / benchmarks
在多类 RL 环境和随机投影任务上，对比先前 memory-based/meta-RL 方法的泛化。

## Strongest results
In-context Learning can be sped-up when the gap is increased How can the speed of learning be controlled? In Figure 3 (left), we demonstrate how an increased gap g can speed up learning at meta-test time. We also test the limiting case of a maximally large gap g that corresponds to the action targets taken by the optimal policy in the dataset. We find that in the case of a single task, the network simply learns the optimal policy.

## Failure modes or limitations
如果任务分布不够广，学到的“算法”就只是 domain-specific heuristic，跨域泛化会崩。

## Evidence anchors
- Abstract / first-page parse
- Method/Results inferred from cached text or source text

## Tags
`benchmark` `meta-rl` `memory` `action-models`

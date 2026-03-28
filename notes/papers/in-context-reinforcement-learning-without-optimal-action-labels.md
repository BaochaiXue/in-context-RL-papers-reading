# In Context Reinforcement Learning Without Optimal Action Labels

- Paper folder: `papers/In-Context Reinforcement Learning Without Optimal Action Labels`
- Note slug: `in-context-reinforcement-learning-without-optimal-action-labels`

## Full citation
Authors could not be extracted reliably from the local source. In Context Reinforcement Learning Without Optimal Action Labels. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf-only`
- Metadata source: `cache/papers/In-Context Reinforcement Learning Without Optimal Action Labels.txt`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: with copious data have shown astonishing in-context learning (ICL) capabilities (Akyürek et al., 2022; Dong et al., 2022; Min et al., 2022), i.e., to solve new tasks with only a few demonstrations (Brown et al., 2020a; Perez et al., 2021; Alayrac et al., 2022). In the setting of ICL for supervised learning, when presented with the context of a small batch of paired inputs and labels from a new task, LLMs generate the associated label for an unpaired input.
- Core mechanism: 提出 DIT，用 discounted future reward 给 observed action 加权，替代最优动作标签。
- Primary bottleneck: 权重只是局部 proxy；如果回报延迟太长或状态覆盖太差，pseudo-optimal label 会很噪。
- Evaluated on: 在 bandit 与 MDP 离线数据上，对比 DPT、行为克隆和加权训练变体，目标是次优数据下逼近最优策略。
- Key failure mode: 极端 delayed reward 或 coverage 很弱时，future return 不能可靠反映当前动作质量，WMLE 会失灵。

## Problem setting
with copious data have shown astonishing in-context learning (ICL) capabilities (Akyürek et al., 2022; Dong et al., 2022; Min et al., 2022), i.e., to solve new tasks with only a few demonstrations (Brown et al., 2020a; Perez et al., 2021; Alayrac et al., 2022). In the setting of ICL for supervised learning, when presented with the context of a small batch of paired inputs and labels from a new task, LLMs generate the associated label for an unpaired input. This process does not involve any parameter updates; instead, LLMs rely solely on the provided demonstrations to determine the correct label.

## Method summary
提出 DIT，用 discounted future reward 给 observed action 加权，替代最优动作标签。 Episodes

## Datasets / tasks / benchmarks
在 bandit 与 MDP 离线数据上，对比 DPT、行为克隆和加权训练变体，目标是次优数据下逼近最优策略。

## Strongest results
We empirically demonstrate the efficacy of DIT through experiments on various bandit and MDP problems. In bandit problem, DIT showcases matching performance to that of the theoretically optimal bandit algorithms in both online and offline settings. In MDP problems, we corroborate that DIT can infer close-to-optimal policies from suboptimal pretraining datasets. Notably, albeit without optimal action labels during pretraining, DIT models demonstrate performance as strong as that of DPT models, which have access to optimal action labels during pretraining.

## Failure modes or limitations
极端 delayed reward 或 coverage 很弱时，future return 不能可靠反映当前动作质量，WMLE 会失灵。

## Evidence anchors
- Abstract / first-page parse
- Method/Results inferred from cached text or source text

## Tags
`benchmark` `llm` `meta-rl` `bandits` `offline-rl` `memory` `action-models` `icrl`

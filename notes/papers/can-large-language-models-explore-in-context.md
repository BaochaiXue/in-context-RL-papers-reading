# Can Large Language Models Explore In-Context?

- Paper folder: `papers/Can Large Language Models Explore In-Context`
- Note slug: `can-large-language-models-explore-in-context`

## Full citation
Akshay Krishnamurthy, Keegan Harris, Dylan J. Foster, Cyril Zhang, Aleksandrs Slivkins. Can Large Language Models Explore In-Context?. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf+source`
- Metadata source: `papers/Can Large Language Models Explore In-Context/paper.tex`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: We investigate the extent to which contemporary Large Language Models (LLMs) can engage in exploration , a core capability in reinforcement learning and decision making. We focus on native performance of existing LLMs, without training interventions.
- Core mechanism: 系统性拆解 LLM 在 bandit 里的原生 in-context exploration，并明确区分 suffix failure 与 uniform-like failure。
- Primary bottleneck: 瓶颈不是 token 数，而是模型无法把原始交互历史转成足够统计量，也难以稳定利用负反馈。
- Evaluated on: 使用多臂 bandit 与多种 prompt 设计；核心 baseline 是 Thompson Sampling、UCB 和随机策略，指标是是否收敛到最优臂及 surrogate 失败统计量。
- Key failure mode: 除一套“总结历史+CoT+特定 framing”的配置外，大多数设置都会在早期停止探索或始终近似均匀探索。

## Problem setting
We investigate the extent to which contemporary Large Language Models (LLMs) can engage in exploration , a core capability in reinforcement learning and decision making. We focus on native performance of existing LLMs, without training interventions. We deploy LLMs as agents in simple multi-armed bandit environments, specifying the environment description and interaction history entirely in-context , within the LLM prompt.

## Method summary
系统性拆解 LLM 在 bandit 里的原生 in-context exploration，并明确区分 suffix failure 与 uniform-like failure。

## Datasets / tasks / benchmarks
使用多臂 bandit 与多种 prompt 设计；核心 baseline 是 Thompson Sampling、UCB 和随机策略，指标是是否收敛到最优臂及 surrogate 失败统计量。

## Strongest results
Multi-armed bandits (MAB). We consider a basic multi-armed bandit variant, stochastic Bernoulli bandits . There are possible actions ( arms ), indexed as . Each arm is associated with mean reward , which is unknown.

## Failure modes or limitations
除一套“总结历史+CoT+特定 framing”的配置外，大多数设置都会在早期停止探索或始终近似均匀探索。

## Evidence anchors
- Introduction
- Experimental setup
- Experimental results
- Overview
- Identifying failures
- Investigating successes
- Root causes
- Related work
- Further background on multi-armed bandits
- Discussion and open questions
- Prompt designs
- Prompt examples
- Scatter plots and summary tables

## Tags
`benchmark` `llm` `meta-rl` `exploration` `bandits` `memory` `action-models`

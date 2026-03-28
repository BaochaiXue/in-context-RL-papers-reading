# Meta Reinforcement Learning Robust To Distributional Shift Via Performing Lifelong In Context Learning

- Paper folder: `papers/Meta-Reinforcement Learning Robust to Distributional Shift Via Performing Lifelong In-Context Learning`
- Note slug: `meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning`

## Full citation
Authors could not be extracted reliably from the local source. Meta Reinforcement Learning Robust To Distributional Shift Via Performing Lifelong In Context Learning. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `pdf-only`
- Metadata source: `cache/papers/Meta-Reinforcement Learning Robust to Distributional Shift Via Performing Lifelong In-Context Learning.txt`
- No parsing issues detected in the primary source selection step.

## 5-bullet thesis
- Addresses: imize expected returns across any task sampled from the task distribution. However, most meta-RL methods evaluate their performance on tasks drawn from the same distribution, leaving the generalization capability, particularly with frozen parameters, in Out-of-Distribution (OOD) tasks less studied.
- Core mechanism: PSBL 直接做 predictive posterior distribution 的 amortized inference，并在测试时执行 posterior sampling。
- Primary bottleneck: 动态窗口与近似 posterior 的质量是核心瓶颈；当前证据主要还局限于导航和连续控制。
- Evaluated on: 在 sparse-reward 离散导航与连续控制 OOD 任务上，与标准 meta-RL 方法比较 OOD 适应回报。
- Key failure mode: 论文展示了强 OOD 收益，但更复杂任务家族、可变动作接口和更长时程上的鲁棒性尚未验证。

## Problem setting
imize expected returns across any task sampled from the task distribution. However, most meta-RL methods evaluate their performance on tasks drawn from the same distribution, leaving the generalization capability, particularly with frozen parameters, in Out-of-Distribution (OOD) tasks less studied. This aspect is crucial for real-world applications, as obtaining a comprehensive prior of all possible situations an RL agent might encounter is challenging (Beck et al., 2023).

## Method summary
PSBL 直接做 predictive posterior distribution 的 amortized inference，并在测试时执行 posterior sampling。

## Datasets / tasks / benchmarks
在 sparse-reward 离散导航与连续控制 OOD 任务上，与标准 meta-RL 方法比较 OOD 适应回报。

## Strongest results
In this section, various experiments, including discrete navigation tasks with sparse rewards and continuous control To evaluate the performance of PSBL in environments with

## Failure modes or limitations
论文展示了强 OOD 收益，但更复杂任务家族、可变动作接口和更长时程上的鲁棒性尚未验证。

## Evidence anchors
- Abstract / first-page parse
- Method/Results inferred from cached text or source text

## Tags
`benchmark` `meta-rl` `memory`

# Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning

- Paper folder: `papers/Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning`
- Note slug: `pretraining-decision-transformers-with-reward-prediction-for-in-context-multi-task-structured-bandit-learning`

## Full citation
Subhojyoti Mukherjee, Josiah P., Qiaomin Xie, Robert Nowak. Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Pretraining Decision Transformers with Reward Prediction for In-Context Multi-task Structured Bandit Learning/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.
- Inventory status: This paper folder contains no local PDF files, so it has no rows in `notes/tables/paper_inventory.csv`; the note is source-only.

## 5-bullet thesis
- Addresses: We study learning to learn for the multi-task structured bandit problem where the goal is to learn a near-optimal algorithm that minimizes cumulative regret. The tasks share a common structure and an algorithm should exploit the shared structure to minimize the cumulative regret for an unseen but related test task.
- Core mechanism: 不用最优动作标签，而是先学 reward prediction，再在多任务 structured bandit 上 in-context 做近似最优探索。
- Primary bottleneck: 方法依赖跨任务共享结构和足够多样的 demonstrator 数据；若数据不够 diverse，reward vector 很难被学对。
- Evaluated on: 在线性与非线性 structured bandit 上，与 DPT/AD 类 in-context 方法、LinUCB、Thompson Sampling 和 demonstrator 对比累计 regret。
- Key failure mode: 论文在 data collection analysis 里明确指出：如果示范者像 LinUCB 那样过早丢弃次优动作，数据不够多样，模型就学不出正确 reward 结构。

## Problem setting
We study learning to learn for the multi-task structured bandit problem where the goal is to learn a near-optimal algorithm that minimizes cumulative regret. The tasks share a common structure and an algorithm should exploit the shared structure to minimize the cumulative regret for an unseen but related test task. We use a transformer as a decision-making algorithm to learn this shared structure from data collected by a demonstrator on a set of training task instances.

## Method summary
不用最优动作标签，而是先学 reward prediction，再在多任务 structured bandit 上 in-context 做近似最优探索。

## Datasets / tasks / benchmarks
在线性与非线性 structured bandit 上，与 DPT/AD 类 in-context 方法、LinUCB、Thompson Sampling 和 demonstrator 对比累计 regret。

## Strongest results
在线性与非线性 structured bandit 上，与 DPT/AD 类 in-context 方法、LinUCB、Thompson Sampling 和 demonstrator 对比累计 regret。

## Failure modes or limitations
论文在 data collection analysis 里明确指出：如果示范者像 LinUCB 那样过早丢弃次优动作，数据不够多样，模型就学不出正确 reward 结构。

## Evidence anchors
- Introduction
- Background
- Preliminaries
- In-Context Learning Model
- Related In-context Learning Algorithms
- The ; pred Algorithm
- Pre-training Next Reward Prediction
- Deploying ; pred
- Empirical Study: Non-Linear Structure
- Empirical Study: Linear Structure and Understanding ; pred's Exploration
- Empirical Study: Importance of Shared Structure and Introducing New Actions
- Data Collection Analysis
- Theoretical Analysis of Generalization
- Conclusions, Limitations and Future Works
- Appendix
- Related Works
- Experimental Setting Information and Details of Baselines
- Experimental Details
- Details of Baselines
- Empirical Study: Comparison against K-armed bandits and ; dpt
- Empirical Study: Bilinear Bandits
- Empirical Study: Latent Bandits
- Connection between ; pred; and Linear Multivariate Gaussian Model
- Empirical Study: Increasing number of Actions
- Empirical Study: Increasing Horizon
- Empirical Study: Increasing Dimension
- Empirical Study: Increasing Attention Heads
- Empirical Study: Increasing Number of Tasks
- Exploration of ; pred (; gt) in New Arms Setting
- Empirical Validation of Theoretical Result
- Empirical Study: Offline Performance
- Theoretical Analysis
- Proof of ; Cref lemma:bayes-reg-1
- Generalization and Transfer Learning Proof for ; pred
- Generalization Proof
- Generalization Error to New Task
- Table of Notations

## Tags
`benchmark` `transformers` `meta-rl` `exploration` `bandits` `offline-rl` `memory` `action-models`

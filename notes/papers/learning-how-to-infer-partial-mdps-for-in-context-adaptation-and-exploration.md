# Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration

- Paper folder: `papers/Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration`
- Note slug: `learning-how-to-infer-partial-mdps-for-in-context-adaptation-and-exploration`

## Full citation
Chentian Jiang, Nan Rosemary Ke. Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Learning How to Infer Partial MDPs for In-Context Adaptation and Exploration/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: To generalize across tasks, an agent should acquire knowledge from past tasks that facilitate adaptation and exploration in future tasks. We focus on the problem of in-context adaptation and exploration, where an agent only relies on context, i.e., history of states, actions and/or rewards, rather than gradient-based updates.
- Core mechanism: 让 Transformer 学习 amortized posterior inference，把复杂任务压到可动态规划的 partial MDP 假设空间。
- Primary bottleneck: 核心限制是 partial model 假设空间必须足够小且有用，同时需要关于任务表示的监督。
- Evaluated on: 在 Symbolic Alchemy 变体上，与 exact posterior sampling oracle 比较适应速度与探索-利用平衡。
- Key failure mode: 若环境不能被有用地压缩成 partial models，或者表示监督缺失，该方法会退化。

## Problem setting
To generalize across tasks, an agent should acquire knowledge from past tasks that facilitate adaptation and exploration in future tasks. We focus on the problem of in-context adaptation and exploration, where an agent only relies on context, i.e., history of states, actions and/or rewards, rather than gradient-based updates. Posterior sampling (extension of Thompson sampling) is a promising approach, but it requires Bayesian inference and dynamic programming, which often involve unknowns (e.g., a prior) and costly computations.

## Method summary
让 Transformer 学习 amortized posterior inference，把复杂任务压到可动态规划的 partial MDP 假设空间。

## Datasets / tasks / benchmarks
在 Symbolic Alchemy 变体上，与 exact posterior sampling oracle 比较适应速度与探索-利用平衡。

## Strongest results
Model adaptation Our method adapts its inferred partial model in-context with a speed and accuracy that almost matches an exact implementation of posterior sampling ( Exact PS ) (Figure~REF; qualitatively reproduced with two more training seeds in Appendix~REF). These results suggest our transformer's learned inference over a broader hypothesis space of partial models ( cubes) approaches the speed and accuracy of perfect Bayesian inference over a known space of only 109 Alchemy cubes. Within 200 time steps, our method's model error almost reaches the True Partial Model oracle's 0 error, even though it has never seen the testing partial models' combinations of edges before. The ablation of our method---which is not performing posterior sampling but rather using the expectation of its posterior---adapts similarly well, but it is slower and less accurate, suggesting that sampling leads to better model adaptation.

## Failure modes or limitations
若环境不能被有用地压缩成 partial models，或者表示监督缺失，该方法会退化。

## Evidence anchors
- Introduction
- Problem Setting
- Task distribution
- Defining in-context adaptation and exploration
- Learning How to Infer Partial Models
- Partial MDP
- Approximating distributions
- Training
- Transformer Architecture and Hyperparameters
- Posterior Sampling
- Ablation
- Experimental Setup
- Simplified Symbolic Alchemy Environment
- Partial Models
- Evaluation
- Implementing our Method for Alchemy
- Reference Point Comparisons
- Experiments
- Model adaptation
- Exploration
- Policy adaptation
- Partial models can lead to rewarding policies
- Related Work
- Meta-Reinforcement Learning
- Abstract MDPs
- Conclusion
- Acknowledgments
- Reproducibility across Training Seeds

## Tags
`benchmark` `transformers` `meta-rl` `exploration` `memory` `action-models`

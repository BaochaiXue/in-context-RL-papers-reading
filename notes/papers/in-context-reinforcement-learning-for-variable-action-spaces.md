# In Context Reinforcement Learning For Variable Action Spaces

- Paper folder: `papers/In-Context Reinforcement Learning for Variable Action Spaces`
- Note slug: `in-context-reinforcement-learning-for-variable-action-spaces`

## Full citation
Authors could not be extracted reliably from the local source. In Context Reinforcement Learning For Variable Action Spaces. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/In-Context Reinforcement Learning for Variable Action Spaces/icml2024.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Recently, it has been shown that transformers pre-trained on diverse datasets with multi-episode contexts can generalize to new reinforcement learning tasks in-context. A key limitation of previously proposed models is their reliance on a predefined action space size and structure.
- Core mechanism: Headless-AD 去掉固定动作 head，让模型从上下文中推断动作语义，实现可变离散动作空间迁移。
- Primary bottleneck: 目前只处理离散动作，而且假设动作语义能从上下文/examples 中恢复。
- Evaluated on: 在 Bernoulli/contextual bandit 与 gridworld 上，对比 vanilla AD 和专用固定动作模型。
- Key failure mode: 当新动作缺少可辨识语义，或动作集合过大过组合化时，性能会快速下滑。

## Problem setting
Recently, it has been shown that transformers pre-trained on diverse datasets with multi-episode contexts can generalize to new reinforcement learning tasks in-context. A key limitation of previously proposed models is their reliance on a predefined action space size and structure. The introduction of a new action space often requires data re-collection and model re-training, which can be costly for some applications.

## Method summary
Headless-AD 去掉固定动作 head，让模型从上下文中推断动作语义，实现可变离散动作空间迁移。

## Datasets / tasks / benchmarks
在 Bernoulli/contextual bandit 与 gridworld 上，对比 vanilla AD 和专用固定动作模型。

## Strongest results
As Headless-AD extends and improves on AD, we checked it in two different aspects. Firstly, it should maintain In-Context Learning abilities and thus generalize well to new tasks. Secondly, it should show high performance on action spaces different from the one seen during training. All of the following environments are designed specifically to check both of the above aspects.

## Failure modes or limitations
当新动作缺少可辨识语义，或动作集合过大过组合化时，性能会快速下滑。

## Evidence anchors
- Introduction
- Algorithm Distillation Struggles with Novel Action Spaces
- Headless-AD
- Experiments
- Bernoulli Bandit
- Contextual Bandit
- Darkroom
- Ablations
- Action Set Prompt
- Contrastive Loss
- Orthonormal Action Embeddings
- Related Work
- Conclusion
- Impact Statement
- Background
- Related Work
- Transformers in Reinforcement Learning
- Offline Meta-RL
- In-Context Learning in RL
- Discarding the Linear Layer
- Algorithm Distillation on Permuted Train Sets
- Across-Environment Generalization
- Visual Darkroom
- Darkroom. Alternative Split
- MSE-Headless-AD In-Context Curves on Bernoulli Bandit
- Sampling of Orthonormal Vectors
- Algorithms' Training Times
- Model Hyperparameters
- Linear Dependence of Different Types of Action Embeddings
- Code Sample

## Tags
`benchmark` `transformers` `meta-rl` `bandits` `offline-rl` `memory` `action-models` `icrl`

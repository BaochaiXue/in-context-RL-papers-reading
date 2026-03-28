# Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models

- Paper folder: `papers/Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models`
- Note slug: `sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models`

## Full citation
Can Demircan, Tankred Saanum, Akshay K. Jagadish, Marcel Binz, Eric Schulz. Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models/math_commands.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: In-context learning, the ability to adapt based on a few examples in the input prompt, is a ubiquitous feature of large language models (LLMs). However, as LLMs' in-context learning abilities continue to improve, understanding this phenomenon mechanistically becomes increasingly important.
- Core mechanism: 用 SAE 在 Llama 残差流里找出 TD-error/Q-value 风格特征，并做因果干预验证。
- Primary bottleneck: 机制解释依赖 SAE 质量，而且证据主要停留在简单 RL/graph learning 任务。
- Evaluated on: 在三个简单 RL 风格任务上分析内部表征，核心 baseline 是不干预与有针对性的 feature intervention。
- Key failure mode: 论文未证明这些特征能直接扩展到复杂 RL；next-token 预训练学到的也可能只是 proxy 机制。

## Problem setting
In-context learning, the ability to adapt based on a few examples in the input prompt, is a ubiquitous feature of large language models (LLMs). However, as LLMs' in-context learning abilities continue to improve, understanding this phenomenon mechanistically becomes increasingly important. In particular, it is not well-understood how LLMs learn to solve specific classes of problems, such as reinforcement learning (RL) problems, in-context.

## Method summary
用 SAE 在 Llama 残差流里找出 TD-error/Q-value 风格特征，并做因果干预验证。 Reinforcement Learning We investigate in-context learning in the setting of Markov Decision Processes (MDPs). An MDP consists of a state space , an action space , and transition dynamics , defining the probability distribution of successor states given the current state and action, as well as a reward function that maps state-action pairs to a scalar reward term. The goal of the agent is to learn a policy that maximizes future discounted rewards, e.g. -values , where is a discount factor.

## Datasets / tasks / benchmarks
在三个简单 RL 风格任务上分析内部表征，核心 baseline 是不干预与有针对性的 feature intervention。

## Strongest results
TD learning is a fundamental algorithm in artificial intelligence research . It offers a simple yet efficient solution to the problem of distilling temporally distant consequences of actions into an immediate value signal. TD learning is general: it can be used not only to learn future discounted rewards but also state occupancies , uncertainties and prediction errors .

## Failure modes or limitations
论文未证明这些特征能直接扩展到复杂 RL；next-token 预训练学到的也可能只是 proxy 机制。

## Evidence anchors
- Introduction
- Methods
- Reinforcement Learning
- Sparse Autoencoders
- Llama uses TD features to learn policies in-context
- texorpdfstring $Q$
- Learning graph structures without rewards
- Related work
- Discussion
- Limitations ; & Future Work
- Conclusion
- Acknowledgements
- Appendix
- texorpdfstring $Q$
- SAE Training
- SAE ; texorpdfstring $L_0$
- The Two-Step Task
- Reinforcement learning in a grid world
- Graph Learning

## Tags
`benchmark` `llm` `sequence-models` `meta-rl` `memory` `theory` `action-models` `systems`

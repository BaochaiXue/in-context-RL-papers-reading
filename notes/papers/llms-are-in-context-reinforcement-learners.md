# LLMs Are In-Context Bandit Reinforcement Learners

- Paper folder: `papers/LLMs Are In-Context Reinforcement Learners`
- Note slug: `llms-are-in-context-reinforcement-learners`

## Full citation
Giovanni Monea, Antoine Bosselut, Yoav Artzi. LLMs Are In-Context Bandit Reinforcement Learners. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/LLMs Are In-Context Reinforcement Learners/30-exp.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Large Language Models (LLMs) excel at in-context learning (ICL), a supervised learning technique that relies on adding annotated examples to the model context. We investigate a contextual bandit version of in-context reinforcement learning (ICRL), where models learn in-context, online, from external reward, instead of supervised data.
- Core mechanism: 把分类任务改写成 contextual bandit，证明 off-the-shelf LLM 可以从自身预测与奖励中 in-context 学习。
- Primary bottleneck: 最大瓶颈是稳定性和负例处理；模型更擅长从正奖励示范学，不擅长推理负奖励。
- Evaluated on: 在多种分类基准构造的 contextual bandit 上，比较 zero-shot、不同 prompt 采样与 ICRL 变体；观察 accuracy 随 episode 增长。
- Key failure mode: discussion 明确指出负奖励 episode 处理仍是开放问题；多步 RL、数值型复杂 reward 也尚未覆盖。

## Problem setting
Large Language Models (LLMs) excel at in-context learning (ICL), a supervised learning technique that relies on adding annotated examples to the model context. We investigate a contextual bandit version of in-context reinforcement learning (ICRL), where models learn in-context, online, from external reward, instead of supervised data. We show that LLMs effectively demonstrate such learning, and provide a detailed study of the phenomena, experimenting with challenging classification tasks and models of sizes from 500M to 70B parameters.

## Method summary
把分类任务改写成 contextual bandit，证明 off-the-shelf LLM 可以从自身预测与奖励中 in-context 学习。

## Datasets / tasks / benchmarks
在多种分类基准构造的 contextual bandit 上，比较 zero-shot、不同 prompt 采样与 ICRL 变体；观察 accuracy 随 episode 增长。

## Strongest results
Models We use the instruction-tuned versions of ~3.1 8B ~ and 2.5 ~ for all model sizes. -3.5-mini~ , which generally performs worse due to relative model weakness. For the hardest tasks, we also experiment with ~1.5 Flash 8B~ . 120 USD on API calls.

## Failure modes or limitations
discussion 明确指出负奖励 episode 处理仍是开放问题；多步 RL、数值型复杂 reward 也尚未覆盖。

## Evidence anchors
- Introduction
- In-context Reinforcement Learning
- naiveshort and ; naiveplus
- explorative
- Experimental Setup
- Results and Analysis
- Related Work
- Discussion and Limitations
- Acknowledgments
- Evaluation Measures in the Appendix
- Additional Method Analysis
- naiveshort and ; naiveplus Hyperparameters
- explorative
- Downsampling Strategies
- Hyperparameter Tuning and Sensitivity
- approximate
- explorative Computational Costs
- Method
- Results
- Experimental Setup
- Prompt Design
- Context Windows and Episode Capacity
- Datasets
- Additional Results

## Tags
`benchmark` `llm` `meta-rl` `exploration` `bandits` `memory` `icrl`

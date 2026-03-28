# Large Language Models Can Implement Policy Iteration

- Paper folder: `papers/Large Language Models can Implement Policy Iteration`
- Note slug: `large-language-models-can-implement-policy-iteration`

## Full citation
Logan Walls, Richard L. Lewis, Satinder Singh, Computer Science. Large Language Models Can Implement Policy Iteration. Local manuscript in repository, 2022.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Large Language Models can Implement Policy Iteration/neurips_2022.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: In this work, we demonstrate a method for implementing policy iteration using a large language model. While the application of foundation models to RL has received considerable attention, most approaches rely on either (1) the curation of expert demonstrations (either through manual design or task-specific pretraining) or (2) adaptation to the task of interest using gradient methods (either fine-tuning or training of adapter layers).
- Core mechanism: 用 LLM 在 prompt 内完成 policy evaluation / improvement 循环，把 policy iteration 外显化为推理过程。
- Primary bottleneck: 瓶颈是 rollout/world modeling 质量和 token 成本；性能强依赖模型推理质量。
- Evaluated on: 在 6 个示例型领域上验证，与不带 rollout-based improvement 的变体对比。
- Key failure mode: 作者自己承认经验结果仍较 modest；一旦世界模型误差累积，ICPI 就会迅速偏离正确策略。

## Problem setting
In this work, we demonstrate a method for implementing policy iteration using a large language model. While the application of foundation models to RL has received considerable attention, most approaches rely on either (1) the curation of expert demonstrations (either through manual design or task-specific pretraining) or (2) adaptation to the task of interest using gradient methods (either fine-tuning or training of adapter layers). Both of these techniques have drawbacks.

## Method summary
用 LLM 在 prompt 内完成 policy evaluation / improvement 循环，把 policy iteration 外显化为推理过程。 How can standard policy iteration make use of in-context learning? Policy iteration is either model-based ---using a world-model to plan future trajectories in the environment---or model-free ---inferring value-estimates without explicit planning. Both methods can be realized with in-context learning. We choose model-based learning because planned trajectories make the underlying logic of value-estimates explicit to our foundation model backbone, providing a concrete instantiation of a trajectory that realizes the values.

## Datasets / tasks / benchmarks
在 6 个示例型领域上验证，与不带 rollout-based improvement 的变体对比。

## Strongest results
We have three main goals in our experiments: (1) Demonstrate that the agent algorithm can in fact quickly learn good policies, using pretrained LLMs, in a set of six simple illustrative domains of increasing challenge; (2) provide evidence through an ablation that the policy-improvement step---taking the over Q-values computed through LLM rollouts---accelerates learning; and (3) investigate the impact of using different LLMs (see Table~REF)---different sizes and trained on different data, in particular, trained on (mostly) natural language (GPT-3 and GPT-J) vs.\ program code (Codex and InCoder). We next describe the six domains and their associated prompt formats, and then describe the experimental methodology and results. Domains and prompt format Chain. ~~ In this environment, the agent occupies an 8-state chain.

## Failure modes or limitations
作者自己承认经验结果仍较 modest；一旦世界模型误差累积，ICPI 就会迅速偏离正确策略。

## Evidence anchors
- Introduction
- Related Work
- Learning from demonstrations
- Gradient-based Training ; & Finetuning on RL Tasks
- In-Context Learning
- Method
- Experiments
- Domains and prompt format
- Experiment Methodology and Results
- Conclusion
- NeurIPS Paper Checklist
- For all authors; dots
- If you are including theoretical results; dots
- If you ran experiments; dots
- If you are using existing assets (e.g., code, data, models) or curating/releasing new assets; dots
- If you used crowdsourcing or conducted research with human subjects; dots

## Tags
`benchmark` `llm` `meta-rl` `memory` `world-models` `action-models`

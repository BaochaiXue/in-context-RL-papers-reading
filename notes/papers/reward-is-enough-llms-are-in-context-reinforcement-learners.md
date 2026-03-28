# Reward Is Enough: LLMs Are In-Context Reinforcement Learners

- Paper folder: `papers/Reward Is Enough LLMs Are In-Context Reinforcement Learners`
- Note slug: `reward-is-enough-llms-are-in-context-reinforcement-learners`

## Full citation
Kefan Song, Amir Moeini, Peng Wang, Lei Gong, Rohan Chandra, Shangtong Zhang, Yanjun Qi. Reward Is Enough: LLMs Are In-Context Reinforcement Learners. Local manuscript in repository, 2025.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Reward Is Enough LLMs Are In-Context Reinforcement Learners/main_ICLR.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Reinforcement learning (RL) is a framework for solving sequential decision-making problems. In this work, we demonstrate that, surprisingly, RL emerges during the inference time of large language models (LLMs), a phenomenon we term in-context RL (ICRL).
- Core mechanism: 提出最小化的 scalar-reward prompting，让 LLM 在推理时通过多轮反馈自我改进。
- Primary bottleneck: 主要受限于多轮提示计算成本和 reward evaluator 质量；训练时增强机制还未建立。
- Evaluated on: 在 Game of 24、creative writing、ScienceWorld、AIME/HMMT 上，与 Self-Refine、Reflexion 等基线比较成功率/胜率。
- Key failure mode: 更长时程和更强交互性的 RL 场景尚未证明；多轮 prompting 成本会快速升高。

## Problem setting
Reinforcement learning (RL) is a framework for solving sequential decision-making problems. In this work, we demonstrate that, surprisingly, RL emerges during the inference time of large language models (LLMs), a phenomenon we term in-context RL (ICRL). To reveal this capability, we introduce a simple multi-round prompting framework, we call ICRL prompting, for inference-time self-improvement.

## Method summary
提出最小化的 scalar-reward prompting，让 LLM 在推理时通过多轮反馈自我改进。

## Datasets / tasks / benchmarks
在 Game of 24、creative writing、ScienceWorld、AIME/HMMT 上，与 Self-Refine、Reflexion 等基线比较成功率/胜率。

## Strongest results
In this paper, we demonstrate that reinforcement learning is an emergent capability of LLMs at inference time. We show that our minimal, scalar-reward-based ICRL prompting framework unlocks this ability across diverse models and general-purpose tasks, outperforming self-revision methods. A key direction in future work is to investigate how training-time interventions might further enhance this in-context RL capability in LLMs.

## Failure modes or limitations
更长时程和更强交互性的 RL 场景尚未证明；多轮 prompting 成本会快速升高。

## Evidence anchors
- Introduction
- Background
- In-Context Reinforcement Learning Prompting
- Related Works
- In-Context Reinforcement Learning.
- Inference-Time LLM Self-Improvement
- Experiment
- Game of 24
- Creative Writing
- ScienceWorld
- Analysis
- Conclusion
- Acknowledgments
- Prompt Examples
- Additional Experimental Results
- Additional Benchmark: Math Competitions
- Additional Analysis Results
- Unseen Paper Abstract Generation

## Tags
`benchmark` `llm` `meta-rl` `memory` `icrl`

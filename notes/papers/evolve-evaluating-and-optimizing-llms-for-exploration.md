# EVOLvE: aluating and ptimizing LMs For xploration

- Paper folder: `papers/EVOLvE Evaluating and Optimizing LLMs For Exploration`
- Note slug: `evolve-evaluating-and-optimizing-llms-for-exploration`

## Full citation
Allen Nie, Bo Chang, Jonathan N. Lee, Ed H. Chi, Quoc V. Le, Minmin Chen. EVOLvE: aluating and ptimizing LMs For xploration. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/EVOLvE Evaluating and Optimizing LLMs For Exploration/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Despite their success in many domains, large language models (LLMs) remain under-studied in scenarios requiring optimal decision-making under uncertainty. This is crucial as many real-world applications, ranging from personalized recommendations to healthcare interventions, demand that LLMs not only predict but also actively learn to make optimal decisions through exploration .
- Core mechanism: 提出 BanditBench，并用 inference-time algorithm support 与 synthetic demonstration distillation 提升 LLM 探索。
- Primary bottleneck: 原始 history 文本化后并不足以诱发稳定探索，剩余最优性差距主要来自 regret 仍高于经典 bandit 算法。
- Evaluated on: 评估 context-free/contextual bandits；核心 baseline 是 raw prompting、UCB/TS 风格支持、few-shot demonstration 和 fine-tuning。
- Key failure mode: 弱模型在 hard bandit 上仍停留在线性 regret 区域；即便加 support，和经典最优算法之间仍有明显 gap。

## Problem setting
Despite their success in many domains, large language models (LLMs) remain under-studied in scenarios requiring optimal decision-making under uncertainty. This is crucial as many real-world applications, ranging from personalized recommendations to healthcare interventions, demand that LLMs not only predict but also actively learn to make optimal decisions through exploration . In this work, we measure LLMs' (in)ability to make optimal decisions in bandits, a state-less reinforcement learning setting relevant to many applications.

## Method summary
提出 BanditBench，并用 inference-time algorithm support 与 synthetic demonstration distillation 提升 LLM 探索。

## Datasets / tasks / benchmarks
评估 context-free/contextual bandits；核心 baseline 是 raw prompting、UCB/TS 风格支持、few-shot demonstration 和 fine-tuning。

## Strongest results
In this work, we explored the in-context exploration capabilities of LLMs in bandit environments, introducing BanditBench, a comprehensive benchmark designed to rigorously evaluate LLM's performance. Our evaluation reveals that LLMs struggle with in-context exploration when relying solely on raw interaction history, while inference-time support significantly improves performance. Motivated by the presence of optimal algorithms in this domain, we investigated methods to integrate these algorithms into LLMs through both algorithm-guided support and algorithm distillation via synthesized demonstration data.

## Failure modes or limitations
弱模型在 hard bandit 上仍停留在线性 regret 区域；即便加 support，和经典最优算法之间仍有明显 gap。

## Evidence anchors
- Introduction
- In-Context Exploration
- BanditBench
- Learning Optimal Exploration Behaviors
- Inference-time ; ag
- Algorithm Distillation via Demonstration and Fine-tuning
- Empirical Evaluations
- Setup and Baselines
- Results and Ablation studies
- Functional Interpretation of LLM Exploration Behavior
- Related Work
- Conclusion
- Software and Data
- Acknowledgements
- Appendix
- Details on Multi-Armed Bandit Task
- Details on Contextual Bandit Task
- UCB and LinUCB
- Example of Win-Rate Calculation
- Benchmark Evaluation Cost
- Details on Exploration Optimality Analysis
- Details on Fitting Regret Function
- Evaluation Implementation Details
- Full List of Models
- Scenario Prompts
- Examples of few-shot demonstrations

## Tags
`benchmark` `llm` `meta-rl` `exploration` `bandits` `memory` `action-models`

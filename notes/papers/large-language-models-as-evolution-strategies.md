# Large Language Models As Evolution Strategies

- Paper folder: `papers/Large Language Models As Evolution Strategies`
- Note slug: `large-language-models-as-evolution-strategies`

## Full citation
Robert Tjarko Lange, Yingtao Tian, Yujin Tang. Large Language Models As Evolution Strategies. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Large Language Models As Evolution Strategies/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.
- Inventory status: This paper folder contains no local PDF files, so it has no rows in `notes/tables/paper_inventory.csv`; the note is source-only.

## 5-bullet thesis
- Addresses: Large Transformer models are capable of implementing a plethora of so-called in-context learning algorithms. These include gradient descent, classification, sequence completion, transformation, and improvement.
- Core mechanism: 把 LLM 作为黑盒优化中的 recombination operator，用 prompt 驱动 zero-shot evolution strategy。
- Primary bottleneck: 对表示方式、上下文构造和搜索空间规模高度敏感；长上下文 reasoning 可能成为进一步扩展的前提。
- Evaluated on: 在 BBOB 合成函数与小型 neuroevolution 上，对比 random search、Gaussian hill climbing 和 teacher fine-tuning。
- Key failure mode: 作者提到非各向同性协方差扩展未显著改善；一旦搜索空间变大，当前提示式 ES 可能迅速失效。

## Problem setting
Large Transformer models are capable of implementing a plethora of so-called in-context learning algorithms. These include gradient descent, classification, sequence completion, transformation, and improvement. In this work, we investigate whether large language models (LLMs), which never explicitly encountered the task of black-box optimization, are in principle capable of implementing evolutionary optimization algorithms.

## Method summary
把 LLM 作为黑盒优化中的 recombination operator，用 prompt 驱动 zero-shot evolution strategy。

## Datasets / tasks / benchmarks
在 BBOB 合成函数与小型 neuroevolution 上，对比 random search、Gaussian hill climbing 和 teacher fine-tuning。

## Strongest results
Summary . We outline a prompt strategy that enables purely text-trained LLMs to robustly act as an ES on various BBO tasks. Furthermore, we provide several ablations highlighting the importance of careful solution representation and context construction.

## Failure modes or limitations
作者提到非各向同性协方差扩展未显著改善；一旦搜索空间变大，当前提示式 ES 可能迅速失效。

## Evidence anchors
- Introduction
- Related Work
- Background
- Turning LLMs into ES Algorithms
- LLMs are Zero-Shot Evolution Strategies
- Evaluation on Synthetic BBO Functions
- Evaluation on Neuroevolution Tasks
- EvoLLM Ablation Studies
- Prompt Strategy Ablations
- Raw text vs. discretized representation
- Impact of Resolution ; & Context Length
- EvoLLM with Teacher Fine-Tuning
- Discussion
- Additional Results
- Impact of Search Space Resolution
- Context Members ; & Generations
- Prompt Construction Example: 2 Dim. Sphere / 5 Population members
- Floating Point Number Tokenization
- Hill Climbing Instruction Fine-Tuning

## Tags
`benchmark` `llm` `transformers` `meta-rl` `memory` `sequence-modeling`

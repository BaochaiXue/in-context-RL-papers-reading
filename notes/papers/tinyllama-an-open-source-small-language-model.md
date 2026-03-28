# TinyLlama: An Open-Source Small Language Model

- Paper folder: `papers/TinyLlama An Open-Source Small Language Model`
- Note slug: `tinyllama-an-open-source-small-language-model`

## Full citation
Peiyuan Zhang, Guangtao Zeng, Tianduo Wang Wei Lu. TinyLlama: An Open-Source Small Language Model. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/TinyLlama An Open-Source Small Language Model/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: We present TinyLlama, a compact 1.1B language model pretrained on around 1 trillion tokens for up to 3 epochs Our latest model, TinyLlama v1.1, is only trained for 2 trillion tokens. More details about this latest version will be elaborated in the later section.
- Core mechanism: 训练一个 1.1B 的开源小型 Llama 风格模型，强调训练配方、数据日程和高效率实现。
- Primary bottleneck: 小模型容量本身就是瓶颈，性能上限明显受参数规模和数据调度影响。
- Evaluated on: 在 commonsense reasoning 与 problem-solving benchmark 上，与 OPT-1.3B、Pythia-1.0B/1.4B 对比。
- Key failure mode: 它本身不是追求 frontier 能力的模型；在更难推理任务上会明显弱于更大 LLM。

## Problem setting
We present TinyLlama, a compact 1.1B language model pretrained on around 1 trillion tokens for up to 3 epochs Our latest model, TinyLlama v1.1, is only trained for 2 trillion tokens. More details about this latest version will be elaborated in the later section. .

## Method summary
训练一个 1.1B 的开源小型 Llama 风格模型，强调训练配方、数据日程和高效率实现。

## Datasets / tasks / benchmarks
在 commonsense reasoning 与 problem-solving benchmark 上，与 OPT-1.3B、Pythia-1.0B/1.4B 对比。

## Strongest results
-1em We evaluate TinyLlama on a wide range of commonsense reasoning and problem-solving tasks and compare it with several existing open-source language models with similar model parameters. -1em Baseline models We primarily focus on language models with a decoder-only architecture, comprising approximately 1 billion parameters. Specifically, we compare TinyLlama with OPT-1.3B~ , Pythia-1.0B, and Pythia-1.4B~ . -0.5em Commonsense reasoning tasks To understand the commonsense reasoning ability of TinyLlama, we consider the following tasks: Hellaswag~ , OpenBookQA~ , WinoGrande~ , ARC-Easy and ARC-Challenge~ , BoolQ~ , and PIQA~ .

## Failure modes or limitations
它本身不是追求 frontier 能力的模型；在更难推理任务上会明显弱于更大 LLM。

## Evidence anchors
- Introduction
- Pre-training
- Pre-training data
- Architecture
- Speed Optimization
- Training
- Version 1.1
- Results
- Conclusion
- Acknowledgements
- Data sampling ratio for TinyLlama v1.1

## Tags
`benchmark` `llm` `meta-rl` `open-source` `pretraining`

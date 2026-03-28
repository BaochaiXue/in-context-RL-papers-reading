# xLSTM: Extended Long Short-Term Memory

- Paper folder: `papers/xLSTM Extended Long Short-Term Memory`
- Note slug: `xlstm-extended-long-short-term-memory`

## Full citation
Maximilian Beck, Markus Spanring, ELLIS Unit, LIT AI Lab, Machine Learning, JKU Linz, NXAI Lab, NXAI GmbH. xLSTM: Extended Long Short-Term Memory. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/xLSTM Extended Long Short-Term Memory/xlstm.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: -0.3cm In the 1990s, the constant error carousel and gating were introduced as the central ideas of the Long Short-Term Memory (LSTM). Since then, LSTMs have stood the test of time and contributed to numerous deep learning success stories, in particular they constituted the first Large Language Models (LLMs).
- Core mechanism: 通过 exponential gating、memory mixing 和新 memory 结构，把 LSTM 扩展到可与 Transformer/SSM 竞争的规模。
- Primary bottleneck: sLSTM 的 memory mixing 不能完全并行化；即便有 CUDA kernel，也比并行的 mLSTM 更慢。
- Evaluated on: 在 SlimPajama 15B-token 语言建模和合成任务上，与 Transformer 和状态空间模型比较 perplexity、缩放趋势与吞吐。
- Key failure mode: 作者明确写了两点：sLSTM 并行性受限，且当前优势主要体现在 language modeling，并不自动泛化到所有序列任务。

## Problem setting
-0.3cm In the 1990s, the constant error carousel and gating were introduced as the central ideas of the Long Short-Term Memory (LSTM). Since then, LSTMs have stood the test of time and contributed to numerous deep learning success stories, in particular they constituted the first Large Language Models (LLMs). However, the advent of the Transformer technology with parallelizable self-attention at its core marked the dawn of a new era, outpacing LSTMs at scale.

## Method summary
通过 exponential gating、memory mixing 和新 memory 结构，把 LSTM 扩展到可与 Transformer/SSM 竞争的规模。

## Datasets / tasks / benchmarks
在 SlimPajama 15B-token 语言建模和合成任务上，与 Transformer 和状态空间模型比较 perplexity、缩放趋势与吞吐。

## Strongest results
In this section, we experimentally evaluate xLSTM and compare it to existing methods with a focus on language modeling. We investigate xLSTM's specific capabilities on synthetic tasks in Section~REF. In Section~REF, we compare the validation set perplexity of various current language modeling methods that were trained on 15B tokens from SlimPajama~ . On the same dataset, we perform ablation studies for xLSTM.

## Failure modes or limitations
作者明确写了两点：sLSTM 并行性受限，且当前优势主要体现在 language modeling，并不自动泛化到所有序列任务。

## Evidence anchors
- Introduction
- Extended Long Short-Term Memory
- Review of the Long Short-Term Memory
- sLSTM
- mLSTM
- xLSTM Architecture
- Memory and Speed Considerations
- Related Work
- Experiments
- Synthetic Tasks and Long Range Arena
- Method Comparison and Ablation Study
- xLSTM as Large Language Model
- Limitations
- Conclusion
- Acknowledgements
- Extended Long Short-Term Memory
- Vanilla Long Short-Term Memory Formulation: Vector Notation
- sLSTM
- mLSTM
- Detailed Block Structure
- Experiments
- Synthetic Tasks and Long Range Arena
- Test of xLSTM's Exponential Gating with Memory Mixing.
- Test of xLSTM's Memory Capacities on Associative Recall Tasks.
- Test of xLSTM's Long Range Capabilities on the Long Range Arena.
- Method Comparison and Ablation Study on SlimPajama (15B)
- xLSTM Large Language Models -- SlimPajama300B
- Detailed Results on PALOMA Language Model Evaluation

## Tags
`benchmark` `llm` `transformers` `sequence-models` `meta-rl` `memory` `systems` `sequence-modeling`

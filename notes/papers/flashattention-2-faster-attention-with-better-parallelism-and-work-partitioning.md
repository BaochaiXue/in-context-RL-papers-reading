# Faster Attention with Better Work Scheduling

- Paper folder: `papers/FlashAttention-2 Faster Attention with Better Parallelism and Work Partitioning`
- Note slug: `flashattention-2-faster-attention-with-better-parallelism-and-work-partitioning`

## Full citation
Authors could not be extracted reliably from the local source. Faster Attention with Better Work Scheduling. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/FlashAttention-2 Faster Attention with Better Parallelism and Work Partitioning/flash2.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: 通过更好的 GPU work partitioning 与并行调度，把 exact attention kernel 的吞吐进一步推高。
- Core mechanism: 通过更好的 GPU work partitioning 与并行调度，把 exact attention kernel 的吞吐进一步推高。
- Primary bottleneck: 它改善的是 kernel 常数项，不是 attention 的二次复杂度本身；而且高度依赖现代 GPU 与特定 kernel 形状。
- Evaluated on: 主要用 GPT 风格训练/推理吞吐和 wall-clock benchmark，对比 PyTorch attention 与 FlashAttention-1。
- Key failure mode: 在不支持的硬件、形状或极长序列下，虽然更快但仍受 quadratic FLOPs 和内存层次结构限制。

## Problem setting
通过更好的 GPU work partitioning 与并行调度，把 exact attention kernel 的吞吐进一步推高。

## Method summary
通过更好的 GPU work partitioning 与并行调度，把 exact attention kernel 的吞吐进一步推高。

## Datasets / tasks / benchmarks
主要用 GPT 风格训练/推理吞吐和 wall-clock benchmark，对比 PyTorch attention 与 FlashAttention-1。

## Strongest results
主要用 GPT 风格训练/推理吞吐和 wall-clock benchmark，对比 PyTorch attention 与 FlashAttention-1。

## Failure modes or limitations
在不支持的硬件、形状或极长序列下，虽然更快但仍受 quadratic FLOPs 和内存层次结构限制。

## Evidence anchors
- Background
- Hardware Performance
- Standard Attention Implementation
- sysnameone

## Tags
`benchmark` `sequence-models` `meta-rl` `systems` `efficiency` `sequence-modeling`

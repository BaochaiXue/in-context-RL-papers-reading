# Transformers as Decision Makers: Provable In-Context Reinforcement Learning via Supervised Pretraining

- Paper folder: `papers/Transformers as Decision Makers Provable In-Context Reinforcement Learning via Supervised Pretraining`
- Note slug: `transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining`

## Full citation
Licong Lin, Song Mei. Transformers as Decision Makers: Provable In-Context Reinforcement Learning via Supervised Pretraining. Local manuscript in repository, 2023.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Transformers as Decision Makers Provable In-Context Reinforcement Learning via Supervised Pretraining/notation.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Large transformer models pretrained on offline reinforcement learning datasets have demonstrated remarkable in-context reinforcement learning (ICRL) capabilities, where they can make good decisions when prompted with interaction trajectories from unseen environments. However, when and how transformers can be trained to perform ICRL have not been theoretically well-understood.
- Core mechanism: 给 supervised-pretrained Transformer 的 ICRL 能力建立 regret 和 sample complexity 理论，覆盖 LinUCB/TS/UCB-VI。
- Primary bottleneck: 理论建立在 realizability 和 expert/offline distribution ratio 假设上。
- Evaluated on: 在线性和 Bernoulli bandit 仿真中，与 empirical average、LinUCB、Thompson Sampling 比 regret/suboptimality。
- Key failure mode: 当 offline 数据与 expert 分布差异过大时，误差界会显著恶化，理论保证也会变弱。

## Problem setting
Large transformer models pretrained on offline reinforcement learning datasets have demonstrated remarkable in-context reinforcement learning (ICRL) capabilities, where they can make good decisions when prompted with interaction trajectories from unseen environments. However, when and how transformers can be trained to perform ICRL have not been theoretically well-understood. In particular, it is unclear which reinforcement-learning algorithms transformers can perform in context, and how distribution mismatch in offline training data affects the learned algorithms.

## Method summary
给 supervised-pretrained Transformer 的 ICRL 能力建立 regret 和 sample complexity 理论，覆盖 LinUCB/TS/UCB-VI。

## Datasets / tasks / benchmarks
在线性和 Bernoulli bandit 仿真中，与 empirical average、LinUCB、Thompson Sampling 比 regret/suboptimality。

## Strongest results
In this section, we perform preliminary simulations to demonstrate the ICRL capabilities of transformers and validate our theoretical findings. We remark that while similar experiments have been conducted in existing works~ , our setting differs in several aspects such as imitating the entire interaction trajectory in our pretrain loss~ eq:general_mle as opposed to on the last (query) state only as in~ . The code is available at~https://github.com/licong-lin/in-context-rl. We compare pretrained transformers against empirical average, LinUCB (or UCB), and Thompson sampling.

## Failure modes or limitations
当 offline 数据与 expert 分布差异过大时，误差界会显著恶化，理论保证也会变弱。

## Evidence anchors
- Introduction
- Related work
- Framework for In-Context Reinforcement Learning
- General framework
- Statistical analysis of supervised pretraining
- Main result
- Implications in special cases
- Approximation by transformers
- LinUCB for linear bandits
- Thompson sampling for linear bandit
- UCB-VI for Tabular MDPs
- Experiments
- Conclusions
- Acknowledgement
- Limitation and discussion
- Experimental details
- Implementation details
- Additional experiments and plots
- The effect of distribution ratio
- Technical preliminaries
- Proofs in Section ; ref sec:supervised-pretraining
- Proof of Theorem~; ref thm:diff_reward
- Proof of Proposition~; ref prop:app_opt_diff_reward
- An auxiliary lemma
- Soft LinUCB for linear stochastic bandit
- Embedding and extraction mappings
- LinUCB and soft LinUCB
- Approximation of the ridge estimator
- Proof of Theorem~; ref thm:approx_smooth_linucb
- Proof of Theorem~; ref thm:smooth_linucb
- Thompson sampling for stochastic linear bandit
- Thompson sampling algorithm
- Definitions and assumptions
- Proof of Theorem~; ref thm:approx_thompson_linear-formal
- Proof of Theorem~; ref thm:ts_linear_regret
- Proof of Lemma~; ref lm:lip_of_tps
- Learning in-context RL in markov decision processes
- Embedding and extraction mappings
- UCB-VI and soft UCB-VI
- Proof of Theorem~; ref thm:approx_ucbvi
- Proof of Theorem~; ref thm:ucbvi_icrl-main

## Tags
`benchmark` `transformers` `meta-rl` `bandits` `offline-rl` `memory` `theory` `action-models`

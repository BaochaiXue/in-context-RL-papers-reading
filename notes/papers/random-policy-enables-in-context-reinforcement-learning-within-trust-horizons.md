# Random Policy Enables In-Context Reinforcement Learning within Trust Horizons

- Paper folder: `papers/Random Policy Enables In-Context Reinforcement Learning within Trust Horizons`
- Note slug: `random-policy-enables-in-context-reinforcement-learning-within-trust-horizons`

## Full citation
Weiqin Chen, Systems Engineering, Santiago Paternain. Random Policy Enables In-Context Reinforcement Learning within Trust Horizons. Local manuscript in repository, 2024.
## Parsing status
- Primary source type: `source-only`
- Metadata source: `papers/Random Policy Enables In-Context Reinforcement Learning within Trust Horizons/main.tex`
- Issue: No top-level manuscript PDF found; note built from source files or existing cached parse only.

## 5-bullet thesis
- Addresses: Pretrained foundation models (FMs) have exhibited extraordinary in-context learning performance, allowing zero-shot (or few-shot) generalization to new environments/tasks not encountered during the pretraining. In the case of reinforcement learning (RL), in-context RL (ICRL) emerges when pretraining FMs on decision-making problems in an autoregressive-supervised manner.
- Core mechanism: SAD 用 random-policy 生成 state-action 监督，只在 trust horizon 内蒸馏可置信的动作信息。
- Primary bottleneck: trust horizon 是核心限制；目前只支持离散动作，超出 horizon 的 credit 会失真。
- Evaluated on: 在 Gaussian/Bernoulli bandits、DarkRoom、DarkRoom-Large、MiniWorld 上，与 AD、DPT、DIT 比较 in-context 表现。
- Key failure mode: 作者明确指出当前局限于离散动作；continuous action 和更复杂环境仍未解决。

## Problem setting
Pretrained foundation models (FMs) have exhibited extraordinary in-context learning performance, allowing zero-shot (or few-shot) generalization to new environments/tasks not encountered during the pretraining. In the case of reinforcement learning (RL), in-context RL (ICRL) emerges when pretraining FMs on decision-making problems in an autoregressive-supervised manner. Nevertheless, the current state-of-the-art ICRL algorithms, such as Algorithm Distillation, Decision Pretrained Transformer and Decision Importance Transformer, impose stringent requirements on the pretraining dataset concerning the behavior (source) policies, context information, and action labels, etc.

## Method summary
SAD 用 random-policy 生成 state-action 监督，只在 trust horizon 内蒸馏可置信的动作信息。

## Datasets / tasks / benchmarks
在 Gaussian/Bernoulli bandits、DarkRoom、DarkRoom-Large、MiniWorld 上，与 AD、DPT、DIT 比较 in-context 表现。

## Strongest results
In this section, we substantiate the efficacy of our proposed SAD method on five ICRL benchmark problems: Gaussian Bandits, Bernoulli Bandits, Darkroom, Darkroom-Large, Miniworld , which are commonly considered in the ICRL literature~ . All these problems are challenging to solve in-context, as the test environments differ from the pretraining environments, while the parameters of the FM remain frozen during the test. Environmental Setup Gaussian Bandits. We investigate a five-armed bandit problem in which the state space consists solely of a singleton state .

## Failure modes or limitations
作者明确指出当前局限于离散动作；continuous action 和更复杂环境仍未解决。

## Evidence anchors
- Introduction
- Main Contributions
- Related Work
- Offline Reinforcement Learning
- Autoregressive-Supervised Decision Making
- In-Context Reinforcement Learning
- In-Context Reinforcement Learning
- Preliminaries
- Supervised Pretraining Mechanism
- State-Action Distillation
- Trustworthiness of the Random Policy
- Performance Guarantees
- Experiments
- Environmental Setup
- Numerical Results
- Ablation Studies
- Conclusion
- Related Work
- Offline Reinforcement Learning
- Autoregressive-Supervised Decision Making
- In-Context Reinforcement Learning
- Omitted Proofs
- Proof of Theorem~; ref theorem_mab
- Validity of Assumption~; ref assumption_mdp_equal
- Discussion of Assumption~; ref assumption_mdp_equal
- Proof of Theorem~; ref theorem_mdp
- Technical Lemma
- Proof of Corollary~; ref corollary_ps_sampling
- Finite MDP setting from ; cite osband2013more
- Proof of Corollary~; ref corollary_regret_bound
- Implementation Details
- Experimental Details
- Hyperparameters
- Additional Results

## Tags
`benchmark` `transformers` `sequence-models` `meta-rl` `bandits` `offline-rl` `memory` `action-models`

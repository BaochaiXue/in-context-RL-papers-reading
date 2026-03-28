# Idea Ranking

## Scoring scheme

- `Novelty`: 1-5
- `Feasibility`: 1-5
- `Impact`: 1-5
- `Total`: sum of the three scores

These scores are speculative prioritization decisions grounded in the local note corpus, not empirical results.

| Rank | Idea | Direction | Novelty | Feasibility | Impact | Total | Rationale |
|---|---|---|---:|---:|---:|---:|---|
| 1 | Typed Algorithm-State Transformer | Direction 1 | 5 | 3 | 5 | 13 | Most direct response to the field's mechanism gap; high upside if explicit state proves learnable. |
| 2 | Experience Compiler for Task-Sufficient Context | Direction 2 | 5 | 3 | 5 | 13 | Strongly supported by repeated evidence that raw histories are a bad interface; likely high leverage across many subproblems. |
| 3 | Belief-Calibrated Conservative ICRL | Direction 3 | 4 | 4 | 5 | 13 | Connects offline RL objective repair with uncertainty tracking; likely to improve both robustness and deployability. |
| 4 | Demonstration-to-Affordance Distillation | Direction 4 | 5 | 3 | 4 | 12 | Targets the knowing-doing gap highlighted by multimodal long-context notes. |
| 5 | Abstention-Aware Embodied ICRL | Direction 5 | 4 | 3 | 5 | 12 | High deployment relevance because current notes underweight safe adaptation. |
| 6 | Revision-Capable Episodic Memory for ICRL | Direction 2 | 4 | 3 | 4 | 11 | Strong systems relevance; depends on memory revision machinery that current pipelines do not yet expose. |
| 7 | Action-Semantic Latent Interface Model | Direction 4 | 4 | 3 | 4 | 11 | Important for generalist agents and cross-domain transfer, though interface-supervision design may be difficult. |
| 8 | Non-Stationary Adaptation Stress Suite | Direction 5 | 3 | 5 | 3 | 11 | Lower novelty than mechanism work, but very feasible and immediately useful for the whole workspace. |
| 9 | Adaptive Trust Horizon Learning | Direction 3 | 4 | 4 | 3 | 11 | Concrete extension of existing trust-horizon ideas with reasonable experimental accessibility. |
| 10 | Counterfactual Credit Editing for ICRL | Direction 1 | 4 | 3 | 4 | 11 | Good probe of whether models really adapt internally, but may require careful synthetic task design. |
| 11 | Two-Timescale Sequence Backbone for Adaptive Memory | Direction 2 | 3 | 4 | 4 | 11 | Technically plausible and aligned with current systems pressure, but less conceptually new than a compiler view. |
| 12 | Negative-Episode Reasoning for LLM-Based ICRL | Direction 3 | 3 | 4 | 4 | 11 | Directly grounded in current LLM failure notes and can be prototyped relatively quickly. |
| 13 | Cultural and Multi-Agent Externalized Memory | Direction 5 | 4 | 3 | 3 | 10 | Interesting and underexplored, but farther from the main bottlenecks than uncertainty or context compilation. |
| 14 | Communicative Contextors for New Control Interfaces | Direction 4 | 4 | 2 | 4 | 10 | Conceptually appealing, but interface and protocol learning may be difficult to stabilize. |
| 15 | Memory-vs-Learning Disentanglement Suite | Direction 1 | 3 | 4 | 3 | 10 | Useful scientifically and feasible, though more diagnostic than transformative on its own. |

## Portfolio recommendation

### Best high-upside agenda

1. Typed Algorithm-State Transformer
2. Experience Compiler for Task-Sufficient Context
3. Belief-Calibrated Conservative ICRL

These three ideas form the cleanest mechanism-method-evaluation chain:

- explicit internal state,
- explicit context compilation,
- explicit uncertainty-aware decision making.

### Best near-term wins

1. Non-Stationary Adaptation Stress Suite
2. Negative-Episode Reasoning for LLM-Based ICRL
3. Adaptive Trust Horizon Learning

These are the most practical if the goal is to start producing results quickly while preserving a path toward a larger proposal.

## Note support by idea

- Typed Algorithm-State Transformer:
  `notes/papers/transformers-learn-temporal-difference-methods-for-in-context-reinforcement-learning.md`,
  `notes/papers/sparse-autoencoders-reveal-temporal-difference-learning-in-large-language-models.md`,
  `notes/papers/transformers-as-decision-makers-provable-in-context-reinforcement-learning-via-supervised-pretraining.md`
- Experience Compiler for Task-Sufficient Context:
  `notes/papers/filtering-learning-histories-enhances-in-context-reinforcement-learning.md`,
  `notes/papers/retrieval-augmented-decision-transformer-external-memory-for-in-context-rl.md`,
  `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`
- Belief-Calibrated Conservative ICRL:
  `notes/papers/yes-q-learning-helps-offline-in-context-rl.md`,
  `notes/papers/random-policy-enables-in-context-reinforcement-learning-within-trust-horizons.md`,
  `notes/papers/in-context-reinforcement-learning-without-optimal-action-labels.md`
- Demonstration-to-Affordance Distillation:
  `notes/papers/lmact-a-benchmark-for-in-context-imitation-learning-with-long-multimodal-demonstrations.md`,
  `notes/papers/large-language-models-as-general-pattern-machines.md`,
  `notes/papers/in-context-reinforcement-learning-via-communicative-world-models.md`
- Abstention-Aware Embodied ICRL:
  `notes/papers/relic-a-recipe-for-64k-steps-of-in-context-reinforcement-learning-for-embodied-ai.md`,
  `notes/papers/human-timescale-adaptation-in-an-open-ended-task-space.md`,
  `notes/papers/meta-reinforcement-learning-robust-to-distributional-shift-via-performing-lifelong-in-context-learning.md`

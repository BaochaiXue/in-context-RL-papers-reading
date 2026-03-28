# Agenda Ranking

## Scope

This ranking compares candidate research agendas for `in-context-rl` using only the local synthesis and claim ledger.

## Scoring

- `Novelty`: does the agenda target a deep unsolved bottleneck rather than a surface optimization?
- `Coherence`: does the agenda form one causal program rather than a bundle?
- `Feasibility`: can it be executed as a staged research program with bounded fallbacks?
- `Leverage`: if successful, does it unlock multiple downstream problems?

Scores are from `1` to `5`.

| Rank | Agenda | Novelty | Coherence | Feasibility | Leverage | Total | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | Agenda A: Testable Algorithmic State for Adaptive Agents | 5 | 5 | 4 | 5 | 19 | Best primary agenda |
| 2 | Agenda B: Objective-Repair for Offline-to-Online Adaptation | 4 | 4 | 5 | 4 | 17 | Strong secondary agenda |
| 3 | Agenda D: Scalable Context Systems under Shift | 4 | 4 | 4 | 4 | 16 | High practical value, weaker mechanism story |
| 4 | Agenda C: Interface-Robust Multimodal Adaptive Control | 5 | 3 | 3 | 4 | 15 | High upside, but riskier and more setup-dependent |

## Why Agenda A wins

### Novelty

Agenda A targets the deepest unresolved issue in the local corpus:

- `icrl-foundation-002`
- `icrl-foundation-004`

It does not merely optimize context or objectives. It asks what internal adaptive state should exist and whether making that state explicit improves behavior.

### Coherence

Agenda A has the cleanest causal chain:

- mechanism hypothesis,
- architecture built around that mechanism,
- closed-loop validation under shift.

This makes it less collage-like than the alternatives.

### Feasibility

Agenda A is still ambitious, but it admits a staged execution path:

- controlled intervention tasks first,
- context-compilation architecture second,
- bounded multimodal or embodied validation third.

This staging is better aligned with local contradictions around scale and diversity:

- `icrl-contradiction-001`
- `icrl-contradiction-002`

### Leverage

If Agenda A works, it informs:

- mechanism interpretation,
- context construction,
- uncertainty-aware adaptation,
- evaluation under shift.

That gives it higher leverage than a narrower objective-only or interface-only program.

## Why the others lose

### Agenda B

Strong and feasible, but not deep enough as a top-level spine. It risks treating objective mismatch as the whole story when the local corpus also points to state and memory confounds.

Grounding:

- `icrl-method-001`
- `icrl-method-002`
- `icrl-contradiction-003`

### Agenda C

Conceptually exciting, but too dependent on interface-specific task design and multimodal setup quality. It is better as a downstream validation branch or later expansion.

Grounding:

- `icrl-method-005`
- `icrl-systems-003`
- `icrl-eval-003`

### Agenda D

Very useful for deployment realism, but it is closer to a reliability and systems agenda than a central scientific account of adaptation.

Grounding:

- `icrl-systems-001`
- `icrl-systems-002`
- `icrl-contradiction-001`
- `icrl-contradiction-002`

## Selected program

- Selected agenda: **Agenda A: Testable Algorithmic State for Adaptive Agents**
- Supporting synthesis:
  - [research_directions.md](/Users/xinjiezhang/in%20context%20RL/synthesis/in-context-rl/research_directions.md)
  - [research_gaps.md](/Users/xinjiezhang/in%20context%20RL/synthesis/in-context-rl/research_gaps.md)
  - [contradictions.md](/Users/xinjiezhang/in%20context%20RL/synthesis/in-context-rl/contradictions.md)

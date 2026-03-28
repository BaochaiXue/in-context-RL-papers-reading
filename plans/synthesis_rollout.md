# Synthesis Rollout

## Goal

Produce topic-scoped, evidence-backed synthesis artifacts from existing local notes, claim ledgers, and tables only.

## Scope

- Input sources:
  - `./notes/papers/*.md`
  - `./notes/claims/in-context-rl/*.yaml`
  - `./notes/tables/paper_inventory.csv`
  - `./notes/tables/method_comparison.md`
  - `./notes/tables/evidence_map.md`
  - `./notes/tables/note_coverage.md`
- Output artifacts:
  - `./synthesis/in-context-rl/trends.md`
  - `./synthesis/in-context-rl/research_gaps.md`
  - `./synthesis/in-context-rl/contradictions.md`
  - `./synthesis/in-context-rl/method_map.md`

## Steps

1. Read the topic claim ledger and use it as the primary synthesis backbone.
2. Use `method_comparison.md`, `evidence_map.md`, and `note_coverage.md` to cross-check coverage and parsing limits.
3. Identify evidence-backed major trends and keep speculative implications in a separate subsection.
4. Identify deep research gaps only when they can be traced to local claims or notes.
5. Make unresolved tensions explicit in a dedicated contradictions artifact.
6. Build a method map that clusters local approaches, strengths, and persistent bottlenecks.

## Constraints

- No new claims from raw PDFs.
- No proposal drafting here.
- Every major gap or contradiction must trace to local claims or notes.
- Separate evidence-backed synthesis from speculative interpretation.

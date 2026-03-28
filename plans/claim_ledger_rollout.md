# Claim Ledger Rollout

## Goal

Convert the local note layer under `./notes/papers` into a reusable claim ledger under `./notes/claims/in-context-rl` without writing synthesis or proposal prose.

## Scope

- Topic assumption for this run: `in-context-rl`
- Inputs:
  - `AGENTS.md`
  - `notes/papers/*.md`
- Out of scope:
  - global survey writing
  - proposal drafting
  - new claims from raw PDFs

## Required claim fields

Each claim record must contain:

- `claim_id`
- `statement`
- `type`: `evidence` | `inference` | `speculation`
- `support_note_files`
- `evidence_anchors`
- `confidence`
- `downstream_use_candidates`

## Artifact layout

- `notes/claims/in-context-rl/foundation.yaml`
- `notes/claims/in-context-rl/methodology.yaml`
- `notes/claims/in-context-rl/evaluation.yaml`
- `notes/claims/in-context-rl/systems_and_data.yaml`
- `notes/claims/in-context-rl/contradictions.yaml`
- `notes/claims/in-context-rl/weak_claims.yaml`

## Rules

- Reuse only claims that can be traced to local notes.
- Merge near-duplicate claims rather than storing paraphrase variants.
- If support is thin or noisy, downgrade the record to `inference` or `speculation`.
- Unsupported claims must not enter the ledger.

## Validation gate

- YAML files exist under `notes/claims/in-context-rl/`
- Every reusable claim has all required fields
- Contradictory and weakly supported claims are explicitly flagged
- No claim in the main ledger lacks support note files or evidence anchors

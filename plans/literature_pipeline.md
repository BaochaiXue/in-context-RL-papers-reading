# Literature Pipeline

## Objective

Initialize and maintain a Codex-friendly workflow that turns local papers in `./papers` into grounded notes, synthesis artifacts, research directions, and a compiled proposal.

## Milestones

### 1. Ingestion

- Scan `./papers` for candidate main PDFs.
- Extract reusable plain text into `./cache`.
- Record parsing failures and fallback decisions.

### 2. Per-paper notes

- Create one note per paper under `./notes/papers`.
- Capture citation, problem, method, data/tasks, main results, limitations, and evidence anchors.
- Mark incomplete notes when a PDF cannot be parsed reliably.

### 3. Cross-paper synthesis

- Build inventories and comparison tables under `./notes/tables`.
- Summarize trends, agreements, disagreements, and recurring bottlenecks under `./synthesis`.
- Keep evidence-backed observations separate from interpretation.

### 4. Idea generation

- Derive research gaps from note coverage rather than titles.
- Map each idea to concrete evidence from local notes.
- Rank ideas by novelty, feasibility, and expected impact.

### 5. Proposal drafting

- Write proposal sources under `./proposal`.
- Cite only papers already read locally and already reflected in notes.
- Maintain a traceable link from proposal claims back to local evidence.

### 6. Proposal review

- Check citation traceability.
- Check internal consistency between notes, synthesis, and proposal claims.
- Compile LaTeX until a valid PDF exists.
- Record unresolved risks or missing prerequisites before claiming completion.

# Proposal Build

## Files

- `main.tex`
- `references.bib`
- `proposal.pdf`

## Exact build command

```bash
cd proposal && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

## Build assumptions

- `pdflatex` is available on `PATH`
- `bibtex` is available on `PATH`
- the bibliography uses only entries defined in `references.bib`
- the proposal is grounded in local notes under `../notes/papers` and local synthesis under `../synthesis`

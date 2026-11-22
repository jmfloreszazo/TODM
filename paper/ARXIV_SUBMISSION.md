# arXiv submission package — author checklist

## Current manuscript v1.6

**Status:** finalized manuscript dated 22 November 2026, not submitted to or accepted by arXiv. A GitHub paper release is separate from academic publication. The software remains v1.5.0. Use [v1.6.tex](source/v1.6.tex), [references-v1.6.bib](source/references-v1.6.bib), a matching generated `v1.6.bbl`, and both referenced PDF figures. Put the main file at the ZIP root and preserve `figures/`. Do not include historical sources, logs, auxiliary files, or the output manuscript PDF in the TeX source ZIP. Select `v1.6.tex` as the main document when importing into Overleaf.

Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error v1.6.tex` from `paper/source`, or use the alternative in the [paper README](README.md). Copy the exact title, author, abstract and five keywords from v1.6, not the historical metadata below. Preserve the author's accented name using supported TeX accents in arXiv metadata fields where required.

The official [submission guidelines](https://info.arxiv.org/help/submit/index.html), [TeX requirements](https://info.arxiv.org/help/submit_tex.html) and [metadata instructions](https://info.arxiv.org/help/prep.html) were consulted on 22 November 2026. The general instructions do not impose a universal article page limit or journal template. Supply TeX sources for a TeX-generated article, include all figures with case-sensitive paths, and inspect the PDF compiled by arXiv itself. Successful local compilation does not establish arXiv acceptance.

The author has designated manuscript v1.6 as final. Authorization to submit, Rafael's final review, license selection, account/category eligibility, any endorsement, and moderation remain separate pending steps. No Overleaf synchronization, ResearchGate upload or arXiv submission has been performed. The existing PDF workflow still targets v1.5 and does not publish v1.6.

The current [source ZIP](TODM_arXiv_source_v1.6.zip) includes `figures/todm_method.pdf` and the redrawn `figures/todm_planes_v1.6.pdf`. The editable source for the latter is maintained in the repository; arXiv compilation uses the included vector PDF.

## Historical v1.4 checklist (not the v1.6 submission metadata)

The remainder preserves the previous candidate's files and instructions for provenance; do not use its `main.tex`, abstract or keywords for manuscript v1.6.

**Historical status:** Complete candidate source package and compiled PDF are publicly available. **Not submitted to or accepted by arXiv.**

## Files

- [Compiled 20-page manuscript PDF](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_Paper_v1.4.pdf)
- [Standalone LaTeX source ZIP for arXiv](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_arXiv_source_v1.4.zip)
- [Full research artifact](https://github.com/jmfloreszazo/TODM/releases/download/todm-research-v1.4.0/TODM_Research_Artifact_v1.4.0.zip)
- [Verified paper compilation](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468)

## Suggested metadata (review before submitting)

**Title:** TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering

**Subtitle:** A Tool-Agnostic, Falsifiable Method for Greenfield Development, Brownfield Modernization, and Application Management

**Author:** José María Flores Zazo

**Primary subject area to consider:** Computer Science — Software Engineering (`cs.SE`). Category eligibility and any endorsement requirement are decided by arXiv, not this repository.

**Keywords:** test oracle problem; software engineering methodology; AI coding agents; model-based testing; human oversight; agent governance; legacy modernization; software maintenance; mutation testing; behavioral contracts.

**Abstract:** Use the exact abstract from `paper/source/main.tex`; do not substitute promotional claims or synthetic engineering results as empirical findings.

## Submission steps requiring the author

1. Sign in to your own [arXiv submission account](https://arxiv.org/submit).
2. Check account/category eligibility, possible endorsement and current submission policies.
3. Select the appropriate submission license. **No license choice has been made on your behalf.**
4. Upload the source ZIP, allow arXiv to compile it and inspect every page, figure and reference.
5. Enter exact author/title/abstract/subject metadata, code availability URL and relevant comments.
6. Submit and wait for arXiv moderation; record the resulting arXiv ID **only after acceptance/announcement**.
7. Add the verified arXiv ID to the paper metadata, repository README and `CITATION.cff`.

## Claim boundaries

The manuscript presents a proposed method and a synthetic, deterministic demonstration. It does not report a randomized industrial trial or establish causal superiority over existing SDD/TDD/BDD practices. Five OMG-inspired semantic profiles are limited JSON implementations, not certified standard engines.

## Rebuild

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

This historical rebuild command is not the v1.6 build command. The existing GitHub Actions PDF workflow targets v1.5; it does not build or publish manuscript v1.6.

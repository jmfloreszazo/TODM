# TODM research manuscript — v1.4

**Title:** TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering  
**Author:** José María Flores Zazo  
**Unified research version:** **1.4.0** (28 October 2026)  
**Status:** Methodological proposal and reproducible **synthetic** engineering demonstration; not peer-reviewed or arXiv-accepted.

## Canonical v1.4 publication

- [Full English manuscript — PDF](TODM_Paper_v1.4.pdf), compiled by GitHub Actions from [LaTeX source](source/main.tex).
- [Complete manuscript — Markdown](TODM_Paper_v1.4.md).
- [Bibliography](source/references.bib), [BibTeX output](source/main.bbl) and [method](source/figures/todm_method.pdf) / [three-plane](source/figures/todm_planes.pdf) figures.
- [arXiv author checklist](ARXIV_SUBMISSION.md).
- [Canonical PDF compilation CI](../.github/workflows/paper-pdf.yml).
- [Versioning policy](../docs/VERSIONING.md).

## Rebuild

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The CI compiles, checks the visible `v1.4` manuscript version, packages LaTeX sources, uploads artifacts and commits the PDF on `main`. A **successful paper workflow** triggers the release verification; the release must not precede the new PDF.

## Historical files

`TODM_Paper_v1.2.md` and `TODM_Paper_v1.2.pdf` are retained for provenance. They are **not** the canonical v1.4 publication.

## Scope boundary

The [demo v1.4](../demo/) uses five **limited** JSON semantic oracle profiles and 16 synthetic governance fixtures, not complete OMG standard engines, real IAM or an industrial controlled evaluation. No DOI or arXiv submission has been assigned.

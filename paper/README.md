# TODM full research manuscript

**Title:** TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering  
**Author:** José María Flores Zazo  
**Version:** v1.2 (27 October 2026)  
**Status:** Research proposal with reproducible synthetic engineering acceptance, not a peer-reviewed result or an accepted arXiv submission.

## Complete files in this repository

- [LaTeX manuscript](source/main.tex) — full English paper, 20 pages when compiled locally.
- [Bibliography](source/references.bib) and [prebuilt BibTeX output](source/main.bbl).
- [Figure: TODM method](source/figures/todm_method.pdf) and [Figure: three planes](source/figures/todm_planes.pdf).
- [Full Markdown manuscript](TODM_Paper_v1.2.md).
- [Generated PDF](TODM_Paper_v1.2.pdf) — generated and committed by GitHub Actions when the paper workflow succeeds.

## Build from source

With TeX Live, Latin Modern fonts and latexmk installed:

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The workflow [paper-pdf.yml](../.github/workflows/paper-pdf.yml) compiles the full article, verifies the PDF, uploads the PDF and a standalone arXiv-source ZIP as CI artifacts, and commits the PDF to `paper/TODM_Paper_v1.2.pdf`. The paper build has **passed GitHub Actions**: [verified 20-page PDF compilation](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468). The PDF is also a downloadable asset in the [tagged research release](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.2).

## Reproducibility and limitations

The full [research demo](../demo/) implements limited operational profiles for SBVR, BPMN, CMMN, DMN and OCL, not full OMG standards. The demo uses synthetic business and authorization fixtures, not real production signatures or independent industrial data. The [full-demo workflow](../.github/workflows/full-demo.yml) independently checks Python/.NET 10 parity for 16 fixtures and all five oracle families.

## arXiv

See [author submission checklist](ARXIV_SUBMISSION.md).
The CI artifact `TODM_arXiv_source_v1.2.zip` is a *candidate* LaTeX upload bundle. **No arXiv submission or endorsement is asserted.** The author must review submission metadata, references, license and any arXiv moderation requirements before submitting.

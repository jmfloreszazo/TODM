# TODM research manuscript — v1.6 draft

The editorial revision dated 22 November 2026 is available as [PDF](TODM_Paper_v1.6.pdf), [Markdown](TODM_Paper_v1.6.md), and [LaTeX](source/v1.6.tex). **Manuscript v1.6 is a draft, not a new software release.** The companion artifact remains v1.5.0 and its existing DOI does not archive or endorse this revision.

The revision reduces the article from 18 to eight main sections, makes the abstract's acceptance gap explicit, uses five keywords, and places the current synthetic evaluation protocol and justified research questions before the illustration and observations. It distinguishes the activity lifecycle from the component architecture, classifies threats to validity, and integrates future work into the conclusion. The quantitative observations are historical synthetic checks, not new experiments or industrial effectiveness evidence.

The original [v1.5 PDF](TODM_Paper_v1.5.pdf), [v1.5 Markdown](TODM_Paper_v1.5.md), [v1.5 LaTeX](source/v1.5.tex), [v1.4 PDF](TODM_Paper_v1.4.pdf), and [v1.4 manuscript](TODM_Paper_v1.4.md) are preserved. The new draft uses a separate [bibliography](source/references-v1.6.bib) so rebuilding historical sources does not alter their references.

## Build the draft

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error v1.6.tex
```

Alternatively, with Tectonic:

```bash
cd paper/source
tectonic --keep-logs --keep-intermediates v1.6.tex
```

After inspecting the output, copy `paper/source/v1.6.pdf` to `paper/TODM_Paper_v1.6.pdf`. Local Tectonic compilation is not proof of compilation by arXiv's TeX Live service. The existing [PDF workflow](../.github/workflows/paper-pdf.yml) still builds v1.5; it has not been redirected to publish this draft.

## Review and submission

Follow the [submission checklist](ARXIV_SUBMISSION.md). The draft source ZIP must contain `v1.6.tex`, `references-v1.6.bib`, its matching `v1.6.bbl` when generated, and the two referenced PDF figures under `figures/`. Import it into Overleaf and select `v1.6.tex` as the main document with pdfLaTeX. Sharing, license selection, endorsement and submission remain author actions; no accounts or publication have been created.

See [publication status](../docs/PUBLICATION_STATUS.md), [reproducible demo](../demo/README.md) and [versioning](../docs/VERSIONING.md).

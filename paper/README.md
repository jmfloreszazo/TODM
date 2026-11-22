# TODM research manuscript — v1.6

The finalized manuscript dated 22 November 2026 is available as [PDF](TODM_Paper_v1.6.pdf), [Markdown](TODM_Paper_v1.6.md), and [LaTeX](source/v1.6.tex). **Manuscript v1.6 is final for submission preparation, but it has not been submitted or accepted; it is not a new software release.** The companion artifact remains v1.5.0 and its existing DOI does not archive or endorse this revision.

The revision reduces the article from 18 to eight main sections, makes the abstract's acceptance gap explicit, uses five keywords, and places the current synthetic evaluation protocol and justified research questions before the illustration and observations. It distinguishes the activity flow from the responsibility and information-flow model, classifies threats to validity, and integrates future work into the conclusion. The quantitative observations are historical synthetic checks, not new experiments or industrial effectiveness evidence.

The original [v1.5 PDF](TODM_Paper_v1.5.pdf), [v1.5 Markdown](TODM_Paper_v1.5.md), [v1.5 LaTeX](source/v1.5.tex), [v1.4 PDF](TODM_Paper_v1.4.pdf), and [v1.4 manuscript](TODM_Paper_v1.4.md) are preserved. Manuscript v1.6 uses a separate [bibliography](source/references-v1.6.bib) so rebuilding historical sources does not alter their references.

Figure 2 has a version-specific [editable TikZ source](source/figures/todm_planes_v1.6.tex) and [vector PDF](source/figures/todm_planes_v1.6.pdf). The historical figure remains unchanged. To regenerate the revised figure, run `tectonic todm_planes_v1.6.tex` from `paper/source/figures` before rebuilding the manuscript.

## Build v1.6

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error v1.6.tex
```

Alternatively, with Tectonic:

```bash
cd paper/source
tectonic --keep-logs --keep-intermediates v1.6.tex
```

After inspecting the output, copy `paper/source/v1.6.pdf` to `paper/TODM_Paper_v1.6.pdf`. Local Tectonic compilation is not proof of compilation by arXiv's TeX Live service. The [v1.6 workflow](../.github/workflows/paper-v1.6.yml) compiles the manuscript with pdfLaTeX, checks the PDF, and independently rebuilds its source ZIP on pull requests and relevant pushes to `main`. The historical [v1.5 PDF workflow](../.github/workflows/paper-pdf.yml) remains unchanged.

## Paper-only GitHub release

After merging and checking CI, an authorized maintainer can dispatch `paper-v1.6.yml` on `main` with `confirm_release=PUBLISH_PAPER_V1_6`. Only that explicit dispatch can publish the immutable tag `todm-paper-v1.6`; ordinary pushes and pull requests produce build artifacts only. An existing release is not overwritten.

The release contains the compiled PDF, Markdown, portable source ZIP, build provenance with the exact commit and CI run, and SHA-256 checksums. It does not create a software release, modify historical evidence, submit to arXiv, or establish scientific acceptance.

## Review and submission

Follow the [submission checklist](ARXIV_SUBMISSION.md). The [v1.6 source ZIP](TODM_arXiv_source_v1.6.zip) contains `v1.6.tex`, `references-v1.6.bib`, its matching generated `v1.6.bbl`, and the two referenced PDF figures under `figures/`: `todm_method.pdf` and `todm_planes_v1.6.pdf`. Import it into Overleaf and select `v1.6.tex` as the main document with pdfLaTeX. Overleaf sharing, arXiv license selection, endorsement and submission remain author actions; a GitHub release does not perform them.

See [publication status](../docs/PUBLICATION_STATUS.md), [reproducible demo](../demo/README.md) and [versioning](../docs/VERSIONING.md).

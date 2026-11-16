# TODM research manuscript — v2.0 editorial draft

Review the [v2.0 article](TODM_Paper_v2.0.md), [PDF](TODM_Paper_v2.0.pdf), and canonical [LaTeX source](source/v2.0.tex). Phase 1 reorganizes and shortens the article; it introduces no new empirical results or v2.0 release.

The [operational and research supplement](TODM_Supplement_v2.0.md) retains detailed inventories, interfaces, contracts, metrics and roadmap. See the [revision plan](../docs/V2.0_EDITORIAL_PLAN_ES.md) and [measured reduction](editorial-metrics-v2.0.json).

## Build v2.0

Requires LaTeX, BibTeX, latexmk, Poppler, and Pandoc.

```bash
cd paper/source
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error v2.0.tex
cp v2.0.pdf ../TODM_Paper_v2.0.pdf
cd ../..
pdftoppm -scale-to 1600 -png -singlefile paper/source/figures/todm_method.pdf paper/source/figures/todm_method
pdftoppm -scale-to 1600 -png -singlefile paper/source/figures/todm_planes.pdf paper/source/figures/todm_planes
python3 scripts/render_paper_markdown.py
python3 scripts/report_editorial_metrics.py
```

The [v2.0 workflow](../.github/workflows/paper-v2-pdf.yml) packages PDF, Markdown, sources, metrics and page previews. On a push to the isolated editorial branch, it commits the generated review files there; it does not publish a release or write to main.

## Historical versions

- v1.5: [PDF](TODM_Paper_v1.5.pdf), [Markdown](TODM_Paper_v1.5.md), [LaTeX](source/v1.5.tex).
- v1.4: [PDF](TODM_Paper_v1.4.pdf), [Markdown](TODM_Paper_v1.4.md).

The existing published artifact citation remains v1.5.0; its DOI must not be presented as a v2.0 DOI. See [publication status](../docs/PUBLICATION_STATUS.md) and [versioning](../docs/VERSIONING.md).

# TODM versioning and reproducibility

**Development target: 1.5.0 (not yet released).** Latest validated public research release: **1.4.0**.

- **Methodology:** eight gates G0–G7; independently approved oracle baseline; greenfield, brownfield and AMS.
- **Research manuscript:** v1.4 remains the last published canonical manuscript until v1.5 source, Markdown and PDF are compiled and verified.
- **Demo:** v1.5 evidence generator writes `demo/results/reproducibility-v1.5.json`; the underlying synthetic JSON profile schema remains **0.4.0**.
- **Historical evidence:** `demo/results/reproducibility-v0.4.json`, historical research models, prior papers and prior release artifacts must remain intact.
- **Latest published release:** `todm-research-v1.4.0`. Do not create a v1.5 tag until the manuscript, citation, integrity checks, and release workflow are aligned.
- **SHA-256 provenance:** `docs/ARTIFACT_MANIFEST.json` freezes 88 historical sources. Never modify a frozen source without explicit manifest reconciliation and review.
- **External scientific status:** no DOI, arXiv acceptance, industrial comparative superiority, or complete OMG implementation is claimed.

The root VERSION tracks the development target. It must not be used alone as evidence that the release or manuscript has been published.

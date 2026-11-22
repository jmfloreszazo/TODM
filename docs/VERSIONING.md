# TODM versioning and reproducibility

**Software/research artifact: 1.5.0. Manuscript: 1.6.** These are separate version tracks.

- **Methodology:** eight gates G0–G7; independently approved oracle baseline; greenfield, brownfield and AMS.
- **Research manuscript:** v1.6 is the current finalized paper. The paper-only tag `todm-paper-v1.6` is published through an explicitly confirmed workflow after compilation and checks; it does not bump the software version.
- **Demo:** v1.5 evidence generator writes `demo/results/reproducibility-v1.5.json`; the underlying synthetic JSON profile schema remains **0.4.0**.
- **Historical evidence:** `demo/results/reproducibility-v0.4.json`, historical research models, prior papers and prior release artifacts must remain intact.
- **Published software/research release:** `todm-research-v1.5.0`; prior `todm-research-v1.4.0` assets remain historical records. Root `VERSION` and the top-level software fields in `CITATION.cff` continue to identify v1.5.0; its `preferred-citation` identifies paper v1.6, dated 22 November 2026.
- **SHA-256 provenance:** `docs/ARTIFACT_MANIFEST.json` currently freezes 84 historical sources from the original 88-file transfer baseline. Never modify a frozen source without explicit manifest reconciliation and review.
- **External scientific status:** the archived v1.5.0 artifact has DOI `10.5281/zenodo.23725201`; this is not a DOI for manuscript v1.6. No arXiv acceptance, industrial comparative superiority, or complete OMG implementation is claimed.

The root VERSION identifies the software track. It must not be used alone as evidence that a manuscript has been published. See [publication status](PUBLICATION_STATUS.md) for the distinction between GitHub releases, archival deposits, and scientific acceptance.

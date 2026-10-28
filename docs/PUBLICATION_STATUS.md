# TODM publication status — 28 October 2026

## Canonical unified artifact: **v1.4.0**

- [Full research paper PDF](../paper/TODM_Paper_v1.4.pdf) and [Markdown manuscript](../paper/TODM_Paper_v1.4.md); [LaTeX source](../paper/source/main.tex).
- [Python/.NET 10 synthetic research demo v1.4](../demo/) with five limited oracle profiles, 16 governance fixtures, synthetic Ed25519 attestations, fail-closed negative controls and a reproducible results generator.
- [88-file SHA-256 source manifest](ARTIFACT_MANIFEST.json), [version alignment policy](VERSIONING.md) and automated [CI verification](../.github/workflows/docs-integrity.yml).
- [Paper compilation CI](../.github/workflows/paper-pdf.yml), [full research CI](../.github/workflows/full-demo.yml), [seed cross-language CI](../.github/workflows/ci.yml) and [release gate](../.github/workflows/release.yml).
- [Canonical v1.4.0 release](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.4.0): published **only after** the compiled v1.4 paper and full verification pass.

**Historical provenance:** `paper/TODM_Paper_v1.2.*`, `demo/results/reproducibility-v0.4.json`, and `research-models/v0.4/` are intentionally retained as earlier source/evidence formats. They are not the current research artifact version.

## Still pending external scientific steps

- [ ] Actual [arXiv submission](../paper/ARXIV_SUBMISSION.md) and acceptance.
- [ ] Permanent archival DOI, e.g. [Zenodo deposit](DOI_ARCHIVE.md).
- [ ] Preregistered controlled comparative experiment and independent industrial replication.

## Claims boundary

Passing synthetic fixtures, signed **demo** approvals and cross-language parity does not establish real human identity, production access control, complete OMG conformance, peer review or superior industrial effectiveness.

See [audit history](AUDIT_2026-10-28.md).

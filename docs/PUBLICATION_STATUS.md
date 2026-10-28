# TODM research publication status — 27 October 2026

## Completed and independently verifiable

- [x] Full English academic paper (20 pages) in [LaTeX](../paper/source/main.tex) and [Markdown](../paper/TODM_Paper_v1.2.md).
- [x] [PDF compiled by GitHub Actions](../paper/TODM_Paper_v1.2.pdf), [green build](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468).
- [x] Full v0.4 demo source published under [demo/](../demo/), with five **limited** JSON semantic oracle profiles.
- [x] Python/.NET 10 full demo parity across 16 synthetic governance fixtures and five oracle families: [green CI](https://github.com/jmfloreszazo/TODM/actions/runs/40598991585).
- [x] 88 source files matched to local research artifact with Git object hashes; [SHA-256 manifest](ARTIFACT_MANIFEST.json) verified in CI.
- [x] Synthetic signed G2/G6 evidence and negative controls executed, without asserting real human identity.
- [x] Tagged, downloadable [GitHub Research Release v1.4](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.4) with PDF, arXiv-source candidate ZIP and complete reproducibility ZIP.
- [x] Release workflow reran full Python/.NET 10 checks and integrity validation: [green release run](https://github.com/jmfloreszazo/TODM/actions/runs/40599015278).
- [x] MIT license and `CITATION.cff` software citation metadata.

The [28 October technical audit](AUDIT_2026-10-28.md) corrected stale documentation and relative links, and added automated Markdown link checks.

## Pending external scientific publication

- [ ] **arXiv:** author account, license choice, category/endorsement (if required), metadata and actual upload/submission. arXiv acceptance has not been claimed.
- [ ] **Permanent DOI:** deposit the verified tagged research release in a suitable archive such as Zenodo; no DOI is assigned yet.
- [ ] **Empirical evaluation:** preregister and execute a controlled comparison with independent adjudication and appropriate statistical reporting.
- [ ] **Industrial validation:** evaluate on real greenfield, brownfield and AMS cases under approved governance controls.

## Evidence boundary

The public artifact proves deterministic behavior of the implemented **synthetic test fixtures**, including 16-case Python/.NET parity and negative release controls. It does **not** prove comparative superiority, full OMG conformance, production identity assurance, safe autonomous deployment or peer-reviewed industrial effectiveness.

The release tag is a reproducible GitHub snapshot, not a peer-reviewed publication or a DOI.

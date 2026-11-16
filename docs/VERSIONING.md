# TODM versioning and reproducibility

**Development target: 2.0.0-dev.** This is an editorial draft, not a released methodology or new research result.

- **Manuscript:** `paper/source/v2.0.tex` is canonical for v2.0. `scripts/render_paper_markdown.py` generates its Markdown and the supplement.
- **Published citation:** `CITATION.cff` continues to identify the v1.5.0 artifact and its existing DOI. No v2.0 tag, DOI, arXiv identifier, or release is created.
- **Demo:** the v1.5 evidence generator and synthetic profile schema **0.4.0** are unchanged. The editorial revision does not independently validate their outcomes.
- **Historical evidence:** previous manuscripts, bibliography, figures and the 84 sources protected by `ARTIFACT_MANIFEST.json` remain intact.
- **Builds:** the historical v1.5 workflow remains available. `paper-v2-pdf.yml` compiles review artifacts and saves generated PDF/Markdown only on the isolated editorial branch after a push. It never writes to main or publishes a release.
- **Release boundary:** the existing release workflow stays pinned to v1.5.0. A later v2.0 release requires explicit reconciliation of source, evidence, citation and packaging.

The root VERSION tracks development and is not proof of publication. See the [revision plan](V2.0_EDITORIAL_PLAN_ES.md).

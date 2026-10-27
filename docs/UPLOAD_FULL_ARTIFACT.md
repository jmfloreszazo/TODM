# Transfer the complete TODM paper and v0.4 multi-oracle demo

The public repository currently has a **verified Python/.NET 10 minimal seed** and a **16-case JSON-policy parity suite**. The full five-family v0.4 demonstrator and complete academic paper are in the separate **TODM Publication Research Kit v1.6** package.

The full kit includes:
- English research paper v1.2: PDF, DOCX, Markdown, LaTeX/BibTeX and figures.
- Full demo v0.4: Python reference, C#/.NET 10 engine and governance CLI, five limited oracle profiles, 16 governance fixtures, public Ed25519 verification keys and detached synthetic signatures, evidence, dashboard and experimental protocol.
- `publication/publish_full_artifact.sh`: a **dry-run-first** script for transferring the complete kit to this GitHub repository using authenticated Git.
- `publication/full-demo-ci.yml`: a two-job GitHub Actions workflow for full Python and .NET 10 validation. Install it at `.github/workflows/full-demo.yml`.

## Transfer steps

1. Download and extract the v1.6 publication kit from the associated TODM project conversation.
2. From the extracted `publication/` directory, run `bash publish_full_artifact.sh /tmp/todm-review`.
3. Review the staged files and security exclusions, especially private signing material.
4. Run again with a fresh destination and `TODM_PUBLISH_CONFIRM=YES` to commit and push.
5. Check GitHub Actions: the **full demo** workflow must be green for both Python and .NET.
6. Confirm that `demo/scripts/compare_dotnet.py` compared all **16 full governance fixtures** and all **five oracle family verdicts**.
7. Freeze a commit, create a release, archive it (e.g., Zenodo) and insert the immutable identifier in the paper.

## Critical evidence boundary

The current green 16-case policy-parity run is **not** evidence that the five-family full demo passes .NET CI. Do not claim full parity until its own workflow is green. No comparative industrial experiment, DOI or arXiv submission has been confirmed.

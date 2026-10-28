# PR #5 — Acceptance record and research boundary

**Target:** `research/open-challenge-v1` -> `main`. **Draft review only; NO MERGE.**

## What constitutes a complete PR #5

This PR delivers a **research challenge and a reproducible synthetic assurance toolkit**, not the execution of an industrial or human-subject research programme. Research hypotheses are not evidence of experimental effectiveness. Every item below is checkable on the PR head.

| # | Acceptance criterion | Evidence / source | Scope |
| --- | --- | --- | --- |
| AC-01 | Single canonical TODM name and citation metadata in versioned research files | [README](../../README.md), [CITATION](../../CITATION.cff), [publication record](../../docs/PUBLICATION_STATUS.md) | Repository text only; About is admin-managed |
| AC-02 | External challenge has counterexample / replication templates, report and invitation | [challenge README](README.md), [protocol](PROTOCOL.md), [templates](../../.github/ISSUE_TEMPLATE/) | Reproducibility invitation, not replicated findings |
| AC-03 | S1 agent-oracle, S2 delivery, S3 human review arms unambiguously defined | [baselines](BASELINES.md), [canonical comparative protocol](../../docs/COMPARATIVE_PROTOCOL.md) | Preregistration **template**, no frozen study preregistration |
| AC-04 | Source-claim boundaries and evidentiary gaps explicit | [claim ledger](CLAIM_EVIDENCE_LEDGER.md), [limitations](../../demo/docs/limitations.md) | Source inspection, not external verification |
| AC-05 | Synthetic G2/G6 approval is content-bound, scope-bound and fail-closed | [approval reference](approval_reference/), [tests](approval_reference/test_approval_binding.py) | Unit-tested control logic, **not real IAM** |
| AC-06 | S1 scoring supports strict observations and preserves INCONCLUSIVE | [scorer](scoring/score_s1.py), [tests](scoring/test_score_s1.py) | Arithmetic validated; **no agent measurements** |
| AC-07 | Protected file ownership proposal is documented | [CODEOWNERS](../../.github/CODEOWNERS) | Review routing only; rulesets/environments are outside PR-file mutation |
| AC-08 | README/citation release checks match v1.5 while preserving historical v1.4 paper | [alignment checker](../../scripts/check_version_alignment.py), [docs workflow](../../.github/workflows/docs-integrity.yml) | CI source alignment, not external artifact equivalence |
| AC-09 | CI green at the **final head** | [PR checks](https://github.com/jmfloreszazo/TODM/pull/5/checks) | Verify after last commit, record SHA and run IDs |

## Scientific programme — not claims or blockers for this software/documentation PR

The following deliverables require separate authority, subjects, infrastructure or independently collected observations. They **must not be marked complete by code generation or synthetic tests**:

- Security assessment with a separately issued restricted agent credential and real GitHub ruleset denial (G2/G6). CODEOWNERS alone is not enforcement.
- Frozen preregistration, model/CLI benchmarking, independent blind ground truth and agent-execution cost records (S1/S2).
- Human participants, consent, G2 review usability and error-detection results (S3).
- Independent reproduction, external review, full OMG execution-engine conformance and industrial transfer.
- Publication into arXiv and an independently verified archival DOI landing record, if external APIs are unavailable.

The roadmap in [EVIDENCE_FIRST_PLAN.md](EVIDENCE_FIRST_PLAN.md) owns these longer-term research activities. Their unchecked status is **not a reason to misrepresent PR #5 as having completed them**.

## Final review instructions

1. Verify all changed repository-local code and docs are traceable in the single PR.
2. Inspect the last PR-head CI run for docs integrity, Python/.NET, full demo, approval-binding and S1 scoring.
3. State the exact head SHA and GitHub Actions run identifiers in the PR conversation or review. An earlier green SHA does not certify a newer head.
4. Keep PR in **Draft** until specifically authorized; do not auto-merge.
5. Never turn a hypothesis, synthetic fixture, CODEOWNERS proposal or DOI into a claim of experimental or production assurance.

**Acceptance is about completion of a narrowly defined PR artifact, not scientific proof of TODM's superiority.**

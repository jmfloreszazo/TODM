# TODM — Evidence-first hardening and research plan

**Status:** Working plan for draft PR #5; not a release commitment.  
**Branch:** `research/open-challenge-v1`  
**Rule:** No merge, no release promotion, and no claims of measured superiority without independently evaluated evidence.

## Purpose

Turn TODM from a reproducible synthetic demonstration and falsifiable proposal into a method with enforceable authority boundaries, an independent evaluation harness and a publishable comparative experiment. Distinguish **authorization** (may the actor do this?) from **correctness** (does it meet the approved rule?), and assess whether the approval itself is meaningful.

## What the external review establishes — and does not

The external review is a critical *opinion*, not independent experimental proof. Its strongest actionable concerns are (1) a synthetic oracle and test fixture can share assumptions; (2) a human-signed but unexamined G2 baseline can be wrong; (3) demo booleans and signatures are not permission enforcement; and (4) a JSON standards-inspired profile is not a standards-compliant execution engine. Check every factual accusation against the PR head, not an earlier default-branch snapshot.

Preserve the useful method: G0–G7, separation of authority and conformance, PASS/FAIL/INCONCLUSIVE with fail-closed release, honest limits, and the 10,000/12,000/11,000 illustrative case. Avoid treating GitHub badges, stars, manifest hashes or self-review checklists as evidence of effectiveness. DOI = archived artifact, not peer review.

## Work packages (sequential for implementation; research design may run in parallel)

### P0 — Evidence and consistency audit (blocker)

- [ ] Record PR head commit, main commit, release tag, DOI landing page, CI statuses and public repository description/topics.
- [ ] Maintain a claim–evidence ledger: each README, paper, demo and release claim mapped to command/log/artifact or explicitly labelled hypothesis.
- [ ] Reconcile publication versions, citation metadata, manuscript vs PDF and .NET execution evidence; keep historical formats visibly marked.
- [ ] Remove tool/process commentary from public-facing docs; rename any self-produced 'audit' to self-review; fix broken figures/links and minor editing issues when confirmed.
- [ ] Verify that the public name is **Test Oracle-Driven Methodology** throughout; document differences between the repository About and manuscript if API settings cannot be changed here.
- **Exit:** independent reader can identify the current artifact and reproduce each technical claim; no unresolved contradictory public version statements.

### P1 — Authorization enforcement PoC (G2/G4/G6)

- [ ] Define protected oracle and policy paths, trusted business owner/approver, reviewer identity and immutable approval payload hash.
- [ ] Demonstrate **denial at the permission boundary**: agent credentials lack writes to oracle/policy routes; optionally add CODEOWNERS/rulesets/environments subject to actual repository/platform capabilities.
- [ ] Build a negative control: agent attempts to change the approved threshold; record blocked attempt and provenance. Include a positive control with permitted candidate-code edits.
- [ ] Invalidate prior approval when approved content or scope changes. Keep release decision fail-closed for FAIL/INCONCLUSIVE/missing authorization.
- [ ] Prefer GitHub artifact attestations/Sigstore/in-toto conventions over bespoke trust claims; synthetic signing remains labelled synthetic.
- **Exit:** documented reproducible proof that a restricted actor cannot modify the judge using the tested credentials. A prompt or local hook alone is explicitly **not** a security boundary.

### P2 — Oracle independence and semantic depth

- [ ] Define three distinct origins: business-approved expected behavior, agent-generated implementation/tests, and an independent ground-truth adjudicator.
- [ ] Add blinded cases and clean controls that are unknown to the implementation agent; segregate evaluator fixtures and lock their hashes.
- [ ] Implement one real DMN execution integration or clearly scoped executable equivalent; verify license and runtime requirements first.
- [ ] Add property-based / metamorphic invariant tests (e.g. Hypothesis/FsCheck), including valid edge cases and mutation survivors.
- [ ] Treat BPMN conformance, CMMN, SBVR and OCL engines as **later work** unless independently implemented and validated.
- **Exit:** evaluator detects both seeded deviations and clean cases without importing expected verdicts from the same test fixture; results include false positives/negatives and inconclusives.

### P3 — Preregistered controlled agent study

- [ ] Freeze research questions, primary outcome, inclusion rules, sample size/power rationale, stopping rule, task set, randomization, models, CLI versions, prompts and per-arm budgets **before trials**.
- [ ] Compare **A:** coupled spec/tests and candidate authored by an agent; **B:** independent read-only approved oracle; **C:** independent oracle with mutation qualification. Include clean controls and an adversarial inconsistent-spec arm.
- [ ] Make the conventional human/developer baseline a separately reported exploratory arm if feasible; do not silently equate it with agent-only baselines already in `docs/COMPARATIVE_PROTOCOL.md`.
- [ ] Run at least two models and multiple CLI/harness implementations only after confirming cross-tool comparability; record exact tool identity and configuration.
- [ ] Measure defect escape / recall, precision, false-positive rate, gate-bypass attempts, INCONCLUSIVE, execution time, token/currency cost, and operator intervention; bootstrap **by task**, not by individual repeated run.
- [ ] Publish null outcomes, failed runs, deviations and uncertainty intervals; no unregistered early stopping.
- **Exit:** immutable preregistration and machine-readable evidence sufficient for independent reanalysis; no superiority claim unless supported.

### P4 — Human G2 review study (separate research question)

- [ ] Recruit external reviewers with documented expertise, consent and anonymized reporting; 6–10 participants can be a **pilot**, not evidence of broad generalizability.
- [ ] Randomize presentations of AI-proposed business thresholds and hidden errors in decision tables (DMN), Gherkin and code/plain language; counterbalance task order and control prior familiarity.
- [ ] Show exact approved text and changes, evidence provenance, implications, scope and expiry; bind consent to the immutable content digest.
- [ ] Measure missed incorrect oracle approvals, valid approvals wrongly rejected, time, reviewer confidence and disagreement.
- [ ] Include rushed/no-context approval control where ethically suitable; preregister hypotheses and analyze uncertainty.
- **Exit:** observed G2 error-detection/approval failure rates with transparent limits, not merely checkbox completion.

### P5 — Formal policy verification and paper revision

- [ ] Decide whether G0–G7 gate transition invariants warrant TLA+/Alloy. If used, publish runnable models and safety counterexamples; otherwise simplify unsupported formal notation.
- [ ] Add verified prior art and counterarguments (e.g. reward hacking, test tampering, inaccessible tests, specification mismatch, supply-chain attestations); substantiate citations and represent prompt-level mitigations fairly.
- [ ] Use separate sections for **synthetic demonstration**, **enforcement test**, **controlled experimental results**, and **external validation**, with no transfer of claims across evidence levels.
- [ ] Update figures, release artifacts, reproducibility recipes and paper together; keep arXiv submission/endorsement status distinct from repository/Zenodo publication.
- **Exit:** paper claims trace to evidence and limitations; external readers can reproduce tables and analyses.

## Decision gates before claiming readiness

| Milestone | Required evidence | Disallowed shortcut |
| --- | --- | --- |
| M0 — coherence | claim ledger + consistent release metadata | badges or self-review marked 'validated' |
| M1 — enforceability | successful deny/allow controls with real permissions | a boolean approval or prompt instruction |
| M2 — oracle evaluation | blind defects + clean controls + independent ground truth | expected verdict hardcoded in fixture |
| M3 — quantitative study | preregistered runs, full logs, CIs and costs | selective examples or post-hoc stop |
| M4 — business authority | G2 reviewer error analysis | a click counted as understanding |
| M5 — publication | reviewed paper + reproducible archive | DOI represented as peer review |

## Immediate PR #5 backlog (first safe commits)

- [x] Preserve the existing open research challenge, replication/counterexample templates and protocol.
- [x] Add this evidence-first execution plan to the **existing PR branch**, without merging.
- [x] Expand `research/challenge/PROTOCOL.md` with independent oracle-origin and G2 pilot preregistration requirements (documentation; no trial run).
- [x] Add `research/challenge/CLAIM_EVIDENCE_LEDGER.md` distinguishing inspected source assertions from unverified runtime/external evidence.
- [x] Reconcile `research/challenge/BASELINES.md` and `docs/COMPARATIVE_PROTOCOL.md`: S1 agent-oracle, S2 delivery, S3 human G2; protocol remains unregistered until TBDs are frozen.
- [ ] Audit CI and artifact/document claims at PR head.
- [ ] Begin M1 security-boundary spike on this same branch; never mark it complete without a demonstrated denied write.

## Working constraints

1. **No merge or release without explicit authorization.**
2. All future commits remain on `research/open-challenge-v1` unless explicitly instructed otherwise.
3. Changes to research hypotheses and preregistration are versioned; once trials begin, preserve the original plan and log deviations.
4. Mark every item complete only after collecting the stated exit evidence.
5. Keep synthetic demo, repository policy enforcement and industrial transfer at distinct assurance levels.

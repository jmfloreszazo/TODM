# TODM — Incremental delivery roadmap

This checklist distinguishes implemented research artifacts from proposed capabilities. Checked items mean *included and locally verified in the Python reference*, not production-ready.

## H0 — Baseline and oracle proof of concept
- [x] Narrow, versioned JSON contracts for SBVR, DMN, BPMN, CMMN, OCL
- [x] Synthetic G2 digest verification and explicit demo-approval warning
- [x] Five correct controls, four seeded mutants, missing-evidence verdict
- [x] Python reference evaluator and repeatable results
- [x] C# candidate and independent oracle engine source (compilation and synthetic parity verified in GitHub Actions)

## H1 — Governance separation (v0.2)
- [x] Explicit, time-bounded synthetic mandates and revocation
- [x] Independent authority and correctness verdicts
- [x] Simulated G6 release approval; block on FAIL/INCONCLUSIVE or missing approval
- [x] Sixteen fixture cases across greenfield/brownfield/AMS and governance failures
- [x] G0–G7 evidence traces and return paths
- [x] Offline executive dashboard and paper-to-code traceability
- [x] Python qualification tests and baseline tamper rejection
- [x] Confirm .NET 10 build and cross-language parity on [GitHub Actions](https://github.com/jmfloreszazo/TODM/actions/runs/40650709906)

## H2 — True independent authority and approvals
- [ ] Signed, human-reviewed G2 baseline with protected storage and separation of duties
- [ ] Real identity provider / short-lived mandate and revocation enforcement
- [ ] Non-bypassable G6 release protection and audit trail
- [ ] Provenance attestation of code, contracts and runtime evidence

## H3 — Deeper interpreters and brownfield discovery
- [ ] Documented DMN 1.x parser / FEEL subset or standards-backed adapter
- [ ] BPMN execution/trace semantics and CMMN stage/sentry adapter
- [ ] Typed OCL parser with a declared supported metamodel
- [ ] SBVR vocabulary/rule mapping with explicit human sign-off
- [ ] Source and trace collectors for a real legacy system
- [ ] Optional Bolt-Genome impact graph, never as a substitute for oracle authority

## H4 — Scientific validation
- [ ] Register protocol and hypotheses before experimentation
- [ ] Blinded and independently adjudicated ground truth
- [ ] Known-correct decoys and mutation-equivalence adjudication
- [ ] Paired comparison with SDD/TDD/BDD and ordinary agent-assisted delivery
- [ ] Recall, precision, false positives, inconclusive rate, coverage and intervals
- [ ] Multi-project replication; publish all negative and aborted cases

## H2a — Cryptographic integrity demonstrator (v0.3)
- [x] Detached Ed25519 signature over G2 baseline digest, demo-only trust anchor
- [x] Separate demo G6 signing identity; fixture-bound signed approval
- [x] Fail-closed verification, tamper, replay and missing-approval tests
- [ ] Real human identity, protected trust roots, organizational signing and CI release protection
- [ ] Complete H3 standards-backed parsers and real legacy evidence extraction
- [ ] Complete H4 preregistered industrial comparative study

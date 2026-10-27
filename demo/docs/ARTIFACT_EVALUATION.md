# TODM v0.4 — Reproducible research artifact

## What is actually demonstrated

This **synthetic reference implementation** tests a separation of concerns: candidate behavior (five *narrow JSON oracle profiles*), agent authorization (synthetic mandate fixtures), and cryptographically signed G2/G6 attestation (offline Ed25519 **demo** keys). It is not an OMG-compliant five-engine suite. It does not enforce access control at an operating-system or deployment-platform boundary and does not authenticate a real person.

The test suite includes positive controls, four intentionally incorrect candidate mutations, an inconclusive missing-evidence case, 16 governance scenarios, signature tampering, baseline digest mismatch, replay/misbinding controls, and a fail-closed command-line release decision. No code is deployed.

## Reproduction (Python 3.12+ and OpenSSL with Ed25519)

```bash
python3 scripts/reproduce.py
python3 scripts/audit_release.py --case GF-01-greenfield-approved --json
python3 scripts/audit_release.py --case GF-03-wrong-threshold --json # exit 2 = expected BLOCK
```

The first command exits nonzero on any unexpected result and writes `results/reproducibility-v0.4.json`. `scripts/audit_release.py` exits **0 only for synthetic signed allow**, and **2 for BLOCK**. It fails closed on missing/invalid G2, wrong model hashes, missing G6, invalid mandate or failing/inconclusive oracles. The fixture timestamp is fixed: **2026-10-27T12:00:00Z**. Results must not be interpreted as authorization to deploy.

For C# verification, use `bash scripts/run.sh` with .NET 10 SDK, or the GitHub Actions workflow. C# parity is **not established** unless that job succeeds; no .NET SDK is available in the local authoring environment.

## Trust and reproducibility boundary

- The G2 signature binds the manifest digest, and the manifest binds the five JSON model files. The G6 signature binds an individual case and the same manifest digest.
- Signing keys are **demonstration keys**, and the public keys are bundled. Anyone with a copy of the demonstration private keys could mint another attestation. A trusted production issuer, identity proofing, protected key custody, secure time, revocation service and actual deployment enforcement are out of scope.
- The mandate file is not itself signed; it is a static fixture, not a production authorization service. A successful synthetic gate must never be wired directly to production release.
- The reference evaluator and test fixtures are colocated in this repository, so the study does not establish organizational or epistemic independence.
- Case-level counts are **not** statistical evidence for reduced escaped defects; cases are selected synthetic fixtures, not a representative random sample.

## Threats to validity and external study

A future paired study must preregister primary endpoints, use independent business ground truth, separate oracle authors from implementers, include correct decoys and equivalent-mutant adjudication, blind reviewers, report failures and inconclusive cases, and stratify greenfield/brownfield/AMS. The paper's hypotheses remain untested.

## Results naming

Use the exact term **engineering acceptance tests** for these outcomes. Avoid terms such as industrial validation, independently proven effectiveness, full OMG support, or real human authorization.

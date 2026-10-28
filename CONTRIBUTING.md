# Contributing to TODM

Thank you for helping make agent-generated software verifiable.

## Start here

1. Read the [README](README.md), [research limitations](demo/docs/limitations.md) and [migration plan](docs/V1.5_MIGRATION_PLAN.md).
2. Reproduce the synthetic reference checks: `cd demo && python3 scripts/reproduce.py`.
3. If .NET 10 is installed, run `bash scripts/run.sh` from `demo/`.
4. Add a focused test, negative control, or counterexample before proposing a behavior change.
5. Submit a pull request describing expected behavior, observed behavior, reproducibility steps, and affected oracle baseline.

## Non-negotiable review rules

- The implementation agent must not independently authorize or modify its own acceptance baseline.
- Never silently rewrite historical evidence, signatures, SHA-256 digests or prior publication versions.
- Separate profile-schema version from artifact/release version.
- Do not claim full BPMN/DMN/CMMN/SBVR/OCL conformance or production identity assurance.
- Preserve fail-closed semantics and explicit INCONCLUSIVE outcomes.
- Do not commit secrets, virtual environments or compiled dependencies. Research results and provenance are intentionally tracked.

## Good first contributions

Reproducibility across operating systems, new negative controls, malformed or adversarial fixture coverage, traceability improvements, and independently reviewed modernization scenarios.

## Responsible disclosure

Do not publish credentials, real personal data, or vulnerabilities that could compromise an actual deployment. Open a minimal, non-sensitive issue for general defects.

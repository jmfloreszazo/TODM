# Important limitations and non-claims

- This is an **engineering reference prototype**, not empirical validation of TODM.
- No production human approval was performed. `approvalKind=DEMO_SIMULATED` is intentionally not a signature. The CLI requires explicit `--allow-demo-approval`.
- SHA-256 detects accidental or unauthorized model changes relative to the local manifest, **but an attacker who can edit both manifest and models can forge the local baseline**. Production requires signatures and protected review/CI permissions.
- The five `.json` files are **TODM-specific executable profiles**, not full SBVR, DMN, BPMN, CMMN, or OCL interpreters. They are not OMG-conformant formats.
- Mermaid is documentation, not an executable BPMN model.
- The demonstration checks runtime evidence emitted by an example candidate. It **does not inspect or prove correctness of all source code**. Integrate static analyzers, instrumented tests, and trace collectors for that objective.
- No real AI agents, legacy systems, GitHub approval workflow, production deployment, cryptographic attestation, or ontology are included.
- The `Todm.Baseline` example is **deliberately biased to a flawed expectation**. It illustrates a correlated-error failure mode; it is not a controlled SDD/TDD/BDD comparison.
- Results are synthetic and cannot establish general recall, precision, defect escape rate, quality improvement, or percentage of work delegated to AI.
- Some error conditions return `INCONCLUSIVE`; the demo's strict release gate must block both FAIL and INCONCLUSIVE. CLI exit codes: PASS=0, FAIL=2, INCONCLUSIVE=3, malformed/invalid baseline=4.
- SDK compilation is validated by the supplied GitHub Actions workflow when it runs; creation of this repository alone is not evidence that the .NET projects compiled in the authoring environment.

## Additions in v0.2

- The CPAG-style authorization plane is **only a synthetic fixture evaluator**, not a CPAG implementation, a real PDP/PEP, a verified mandate registry, an IAM system, or a cryptographically enforceable revocation mechanism.
- `SIMULATED_ALLOW` never deploys software, updates a repository, or grants privileges. G6 approval is a JSON boolean, not a human approval.
- All G0–G7 traces are **illustrative gate records**. No actual workflow orchestrator, protected human review, release infrastructure, or production G7 telemetry is integrated.
- Python and .NET are independent implementations of a small subset; their parity is **not verified locally** because .NET 10 SDK was unavailable. CI is supplied to validate it.
- `dashboard/index.html` is an offline visualization of precomputed synthetic evidence. It does not execute the .NET runtime, connect to a live agent, or change the release state.
- The nine Python qualification tests do not establish full oracle soundness/completeness or OMG-standard compliance. They only establish deterministic behavior for the declared fixtures.
- An attacker who can modify the model and manifest together can produce a self-consistent forged baseline; this is **explicitly shown** by the manifest-edit test.

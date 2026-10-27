# TODM — Test Oracle-Driven Methodology

**Human-governed AI software engineering with independent acceptance oracles.**

TODM is a proposed, vendor-neutral methodology for greenfield development, brownfield modernization and application maintenance (AMS). Its central rule is that an AI construction agent must not unilaterally define or change the acceptance conditions by which its own output is judged.

## Methodology

| Gate | Stage | Decision |
|---|---|---|
| G0 | Frame scope, risk and mandate | Authorize discovery |
| G1 | Discover and discriminate evidence | Qualify source evidence |
| G2 | Specify, review and freeze baseline | Human approves oracle contracts |
| G3 | Qualify the judges | Positive/negative controls and mutation tests |
| G4 | Delegate bounded implementation | Agent constructs within mandate |
| G5 | Run independent verification | PASS / FAIL / INCONCLUSIVE |
| G6 | Authorize controlled delivery | Separate release authorization |
| G7 | Observe, learn and version | Monitor drift and propose controlled updates |

## Research demonstration

The **minimal executable seed** in this repository illustrates independent oracle verification and release authorization, using synthetic data. Run:

```bash
python3 -m unittest discover -s tests -v
python3 src/todm_demo.py
```

The demo intentionally uses a **limited JSON policy profile**, not a complete SBVR/BPMN/CMMN/DMN/OCL interpreter. The complete v0.4 research artifact (Python reference, .NET 10 source, signed synthetic approvals, 16 governance fixtures, paper and experimental protocol) is being transferred and validated separately; **this repository does not yet contain that full package**.

## Two independent predicates

- **Behavioral conformance:** does the produced system satisfy a separately approved oracle baseline?
- **Agent authority:** was the actor authorized to perform the change and is release independently approved?

Both must hold for delivery. Passing a test is not permission to deploy.

## Scientific status

Methodological proposal and synthetic demonstration. **No claim of industrial effectiveness, empirical superiority, production IAM, human identity verification or complete OMG conformance.** A comparative study against conventional SDD/TDD/BDD is required before asserting benefits.

Author: José María Flores Zazo. See [publication status](docs/RESEARCH_STATUS.md).

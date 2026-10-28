# TODM — Test Oracle-Driven Methodology
## Research synopsis and publication status

**Author:** José María Flores Zazo  
**Working title:** *TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering*  
**Status:** Methodological research proposal with a synthetic executable proof of concept. This synopsis is **not** the full manuscript and is not an arXiv acceptance claim.

### Abstract

Agentic coding systems can generate implementations, specifications and acceptance tests from shared contextual assumptions. Consequently, all generated artifacts can be mutually consistent yet violate an independently authorized business requirement. TODM addresses this correlated-error risk by making human-approved behavioral oracles first-class, versioned and separately executed artifacts. Its lifecycle covers discovery, approval, oracle qualification, bounded AI construction, independent verification, release authorization and post-release monitoring. The method is vendor-neutral and applies to greenfield engineering, brownfield modernization and application maintenance (AMS). A synthetic demonstration illustrates fail-closed release decisions, mutated implementations, incomplete evidence and separation of agent authority from behavioral conformance. It does not establish comparative superiority or industrial effectiveness.

### 1. Research problem

A business rule says requests strictly above EUR 10,000 require human review. An agent changes the threshold to EUR 12,000 in both code and generated tests. A EUR 11,000 request is approved; all correlated generated tests may still pass. The missing control is not another assertion authored by the same agent: it is an **independently approved source of expected behavior**.

### 2. Central hypothesis

An independently approved and mutation-qualified oracle baseline should detect correlated specification/implementation defects missed by developer-authored or agent-authored tests, without unacceptable false-positive and inconclusive rates. This is a testable **hypothesis**, not an empirical conclusion.

### 3. Contribution and novelty boundary

TODM combines known techniques (test oracles, model-based testing, mutation testing, requirements traceability, human review, policy-as-code and governed AI agents) into a proposed **methodology with explicit decision gates**. It does not claim invention of those techniques, complete OMG language implementations, or demonstrated priority over all prior work.

### 4. Eight gates

| Gate | Purpose | Exit evidence |
|---|---|---|
| G0 | Scope, risk, roles, mandate | Authorized scope |
| G1 | Evidence discovery and provenance | Qualified evidence set |
| G2 | Baseline modeling and accountable human approval | Frozen oracle baseline |
| G3 | Oracle qualification | Positive controls, negative controls, mutation sensitivity |
| G4 | Bounded agent construction | Versioned candidate and provenance |
| G5 | Independent behavioral evaluation | PASS, FAIL or INCONCLUSIVE |
| G6 | Separate release authorization | Signed or otherwise verifiable approval tied to candidate and baseline |
| G7 | Observe, monitor and revise | Drift evidence, controlled baseline change |

A failed gate sends work to the relevant earlier stage. A change in requirements invalidates the affected approval and qualification evidence.

### 5. Five model profiles

- **SBVR:** terms, business vocabulary and normative obligations.
- **DMN:** decision tables and deterministic expected outcomes.
- **BPMN:** permitted/forbidden process transitions and paths.
- **CMMN:** case lifecycle, discretionary work and exceptional states.
- **OCL:** invariants, preconditions and postconditions.

The repository's JSON profiles are limited **illustrative adapters**. They are not certified or complete OMG implementations.

### 6. Governance separation

**Authority predicate:** the actor has a valid mandate for this operation.  
**Conformance predicate:** the resulting behavior passes the approved oracles.  
**Release predicate:** conformance, authority, baseline integrity and independent G6 approval all hold.

CPAG/constitutional governance concerns *who may act*. TODM concerns *what behavioral evidence establishes correctness*. These layers are complementary; CPAG is not a mandatory TODM dependency.

### 7. Three adoption contexts

**Greenfield:** approve behavior and oracles before agent-driven implementation.  
**Brownfield:** reconstruct behavior from heterogeneous legacy evidence, resolve ambiguities with domain owners and freeze a modernization equivalence baseline.  
**AMS:** map incidents and changes to existing rules, constrain agent edits and rerun affected oracles and regression controls.

### 8. Scientific evaluation design

Use matched tasks with controlled defects and independently adjudicated expected outcomes. Compare conventional implementation + developer tests, specification-driven agent work, and TODM-governed agent work. Pre-register tasks, defect seeds, exclusions, adjudication and stopping criteria. Report recall, precision, false positives, inconclusive rates, oracle mutation score, evidence coverage and inter-rater agreement. Publish exact software versions, fixture hashes, commit SHA and execution logs. Do not report synthetic controls as industrial outcome data.

### 9. Limitations

Oracle quality depends on the validity of the human-approved baseline; human approval can be wrong. Synthetic signatures are not proof of production human identity. Some requirements cannot be fully formalized. Five OMG profiles require stronger parsers and semantics than the JSON seed provides. No causal benefit can be claimed without controlled experiments.

### 10. Selected foundational literature

- Barr et al. (2015), *The Oracle Problem in Software Testing: A Survey*, IEEE TSE.
- Object Management Group: BPMN 2.0.2, DMN, CMMN, SBVR and OCL specifications.
- Mutation testing and model-based testing literature; full references belong in the submission manuscript.

### Artifact statement

The **complete** Python/.NET 10 five-family synthetic research artifact is [public](../demo/) and has [passed full cross-language CI](https://github.com/jmfloreszazo/TODM/actions/runs/40598991585). The [20-page paper](TODM_Paper_v1.2.pdf) has been compiled by [GitHub Actions](https://github.com/jmfloreszazo/TODM/actions/runs/40598669468). A [tagged release](https://github.com/jmfloreszazo/TODM/releases/tag/todm-research-v1.4) contains the paper and reproducibility bundle. arXiv acceptance, a DOI and industrial empirical validation remain pending.

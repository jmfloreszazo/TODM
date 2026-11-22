# TODM: A Test Oracle-Driven Methodology for Human-Governed AI Software Engineering

## A Tool-Agnostic, Falsifiable Method for Greenfield Development, Brownfield Modernization, and Application Management

**Author:** José María Flores Zazo

**Manuscript version:** 1.6 · **Date:** 22 November 2026 · **Companion artifact:** archived v1.5.0

**Status:** finalized, unsubmitted manuscript with bounded deterministic synthetic checks. This is the Markdown companion to the LaTeX/PDF manuscript v1.6. The software release remains v1.5.0; historical manuscripts and raw evidence remain unchanged.

## Abstract

AI coding agents can generate specifications, implementations, and tests that agree while violating an authoritative business rule. Consistency within generated artifacts therefore leaves an acceptance gap: expected behavior still needs an independently accountable source. The challenges are separating approval from construction, qualifying fallible oracles, and preventing incomplete evidence from becoming a passing verdict. We propose the Test Oracle-Driven Methodology (TODM), which composes established oracle and modeling techniques into a human-approved, versioned behavioral baseline, eight lifecycle gates, and separate governance, construction, and verification planes. Its deterministic acceptance policy distinguishes PASS, FAIL, and INCONCLUSIVE and separates action authorization from behavioral conformance. Greenfield, brownfield, and application management profiles define intended scope, not demonstrated generalization. A companion artifact records bounded deterministic synthetic checks: 16 fixtures, with five signed allows and eleven blocks. These observations demonstrate selected gate behavior, not comparative effectiveness. Explicit research questions and a planned comparative protocol address fault detection, oracle qualification, and governed autonomy. The work is an engineering-research proposal, not an organizational case study, controlled experiment, or validated quality guarantee.

**Keywords:** test oracle problem; AI coding agents; model-based testing; human oversight; mutation testing.

## 1. Introduction

The *test oracle problem* is deciding whether an observed software response is correct [@barr2015oracle]. Agentic construction intensifies a familiar failure mode: the same mistaken interpretation can supply specifications, code, and passing tests. Increasing their mutual consistency does not establish agreement with an authoritative business rule. The acceptance gap concerns the source of expected behavior and who may change it, not simply the number of tests.

TODM addresses this gap through approved behavioral oracles whose authority is separated from delegated construction. Agents may propose rules and implementations but cannot unilaterally approve their acceptance baseline. The challenges are establishing accountable semantics, qualifying imperfect evaluators, maintaining observable evidence, and distinguishing legitimate actions from correct outputs. The proposed contribution is a composition of established techniques: a versioned oracle baseline, an eight-stage activity flow with recovery paths, a three-plane responsibility model, and a falsifiable evaluation protocol. Neither global novelty nor superior effectiveness is established.

Section 2 positions the method. Section 3 defines its contracts, activity flow, controls, and intended application scope; Section 4 explains the responsibility and information-flow model that supports those activities. Section 5 defines the current synthetic check protocol, research questions, and planned comparison before Section 6 separates a reasoned example from recorded synthetic observations. Sections 7 and 8 discuss validity and future work.

## 2. Foundations and Related Work

Oracle techniques include specifications, models, and contracts [@barr2015oracle]. Mutation testing injects faults to assess discrimination [@jia2011mutation]; metamorphic testing checks relations between executions when individual outputs are difficult to specify [@segura2016metamorphic]. TODM does not invent these techniques. Specification-driven development (SDD), including GitHub Spec Kit [@github2026speckit], organizes intent-to-implementation workflows. Test-driven and behavior-driven development (TDD/BDD), including Gherkin examples [@cucumber2026], express executable expectations. TODM is complementary: vetted specifications and examples can become oracles, and these workflows can already incorporate independent approval and qualification. Their absence is a configuration risk, not an inherent deficiency of SDD/TDD/BDD.

Legacy characterization records observed behavior [@feathers2004legacy], which may include defects. The Strangler Fig pattern concerns incremental deployment rather than establishing business truth [@fowler2004strangler]. TODM accordingly distinguishes approved requirements, legacy observations, and inferred hypotheses, independently of migration strategy.

OMG standards address processes (BPMN), cases (CMMN), decisions (DMN), vocabulary and rules (SBVR), and constraints (OCL) [@omg2014bpmn; @omg2016cmmn; @omg2024dmn; @omg2019sbvr; @omg2014ocl]; engines such as Flowable execute substantial BPMN/CMMN/DMN subsets [@flowable2026]. TODM proposes adapters with declared semantic profiles, not new universal standards implementations. Its research question is whether explicitly combining human-authorized baselines, evaluator separation, qualification, and controlled delegation improves acceptance. Distinctiveness and effectiveness remain open to comparative study and prior-art challenge.

## 3. Proposed Method

### 3.1. Contracts and evidence

::: definition
**Definition 1** (Behavioral oracle). *A behavioral oracle is the tuple
$o=(id, v, r, a, i, e, s, c)$, where $id$ identifies the control, $v$
its version, $r$ the approved behavioral rule, $a$ the accountable
approving authority, $i$ required inputs and observations, $e$ an
evaluator with declared semantics, $s$ its severity and scope, and $c$
its provenance and supporting evidence. A textual rule without an
evaluator or observable binding is an *oracle candidate*, not an
executable oracle.*
:::

::: definition
**Definition 2** (Oracle baseline). *An approved oracle baseline
$B_v=\{o_1,\dots,o_n\}$ is a uniquely versioned and integrity-protected
collection of approved oracles, together with model profiles, required
evidence, owner decisions, and an immutable release manifest. Integrity
protection may use cryptographic hashes and digitally recorded
approvals; it does not prove a rule semantically correct.*
:::

::: definition
**Definition 3** (Construction mandate). *A construction mandate $M$
defines the scope and permitted operations of delegated agents,
execution environments, allowed dependencies, escalation conditions,
change boundaries, and the baseline version against which the candidate
must be evaluated. The mandate grants engineering autonomy but never the
right to approve a new baseline.*
:::

**Independence is an architectural property, not an adjective.**

The agent authoring a candidate must lack write/approval access to the
protected baseline and the production verification configuration. It may
submit a proposed change, but approval requires an authorized human
role; the evaluator runs against the approved immutable version.
Independence is partial when generation and evaluation share the same
source evidence, language model, or erroneous business premise;
diversification and external evidence reduce, but cannot eliminate,
common-mode error.

**Evidence classes.**

Every extracted rule is tagged [NORMATIVE]{.sans-serif} (approved policy
or requirement), [OBSERVED]{.sans-serif} (system behavior or logged
outcome), or [INFERRED]{.sans-serif} (AI-derived hypothesis). Conflicts
are surfaced rather than resolved silently. A documented legacy result
is a useful comparator, not automatic truth. Every critical rule has an
owner, provenance, uncertainty record, and escalation path.

**Risk-proportionate controls.**

Small changes may need a DMN decision table and an invariant, but not a
full case-management engine. All five model families are available, yet
selection is justified by behavior and risk rather than compliance
theater. Controls must not create unverified claims of exhaustive
coverage.

### 3.2. Lifecycle and recovery

Figure 1 presents the activity lifecycle as a flowchart, not a reference architecture or an executable BPMN model. Gates are evidence checks rather than a rigid temporal sequence: production events can reopen discovery while bounded implementation repairs continue. Authority and baseline constraints persist across iterations. Section 4 separately describes the responsibility and information-flow model used to support these activities.

![Figure 1. The eight TODM gates and principal rework loops. Reverse transitions are deliberate, not methodological failures.](source/figures/todm_method.pdf)

**Table 1. Lifecycle activities, gate evidence, and recovery. Missing evidence holds advancement.**

| Gate / activity | Evidence required to advance | Recovery on failure |
| --- | --- | --- |
| G0 Frame | Scope, accountable owner, observable behavior, risks and access plan | Clarify boundaries and critical risks. |
| G1 Discover | Traced rule catalog; classified evidence, contradictions and unknowns with owners and stop conditions | Investigate; confidence alone is not authority. |
| G2 Approve | Typed models, effective dates, observation bindings and approval of the exact baseline manifest | Revisit discovery or human interpretation; never edit an approved version in place. |
| G3 Qualify | Known-correct controls pass; designated critical seeded faults are detected; missing evidence is INCONCLUSIVE | Repair the evaluator or return to G2; repeat qualification. |
| G4 Construct | Reproducible build, commit, dependencies, tests, instrumentation and logs within the mandate | Repair within bounds or escalate scope changes. |
| G5 Verify | Executed applicable critical oracles all pass; traces and counterexamples identify candidate and baseline | Implementation deviation returns to G4; oracle or semantic defects to G2/G3. |
| G6 Authorize | Human go/no-go tied to exact versions, residual risk, deployment and reconciliation/contingency plan | No-go, restrict exposure or delay. |
| G7 Observe | Operational ownership, actionable alerts, freshness and baseline-evolution record | Incidents trigger repair; policy changes G2; new capabilities G0. |

Qualification challenges boundary values, stale or missing observations, event ordering, idempotence, evaluator outages, and baseline tampering. It measures fault detection and false alarms without proving business semantics correct. Independent verification binds decisions, events, case states, object snapshots, and pertinent static-analysis evidence to the approved baseline; differential, metamorphic, property-based, security, or process-conformance checks can supplement it. Delivery may use canaries, migration waves, parallel runs, or a single cutover. Production observations propose changes but never automatically redefine normative behavior.

### 3.3. Operational controls and acceptance semantics

Domain owners approve business meaning; oracle stewards qualify evaluators; analysts propose evidence; builders implement; verifier services issue findings without normative edits; release owners authorize delivery. Roles may overlap only if the remaining separation is documented and meaningful. Baseline changes propose $B_{v+1}$ with a diff, rationale, provenance, owner approval, and requalification; a construction pull request cannot approve its own acceptance criteria.

For candidate $S$ and observations $X$, the result of an applicable oracle $o$ is

$$
R(o,S,X)=\begin{cases}
\textsf{FAIL}, & \text{a supported rule is violated};\\
\textsf{PASS}, & \text{the rule is exercised and satisfied with valid evidence};\\
\textsf{INCONCLUSIVE}, & \text{otherwise (missing, ambiguous, or invalid evidence).}
\end{cases}
$$

A non-executed control, timed-out evaluator, unsupported construct, or unverifiable baseline must not pass. For applicable critical oracles $C\subseteq B_v$ and release scope $D$,

$$
\operatorname{eligible}(D)=\bigwedge_{o\in C}(R(o,S,X)=\textsf{PASS})
\land\operatorname{integrity}(B_v)\land\operatorname{evidenceComplete}(D)
\land\operatorname{authorized}(D).
$$

Critical risks without applicable controls hold the release rather than passing through an empty conjunction. Eligibility is necessary, not sufficient: G6 requires a separate human go/no-go. A deterministic policy, not an LLM summary, enforces these conditions. Noncritical exceptions require scoped, dated risk acceptance; emergency releases use a separately approved path with compensating controls, never a fabricated pass.

Each verification record binds the candidate commit/build digest, baseline digest, mandate, model profile/evaluator version, correlated inputs, timestamp/environment, raw observations, verdict, counterexample, and any exception owner. Order-dependent checks require an explicit evidence-completeness or watermark criterion; clocks and cross-system correlation cannot be assumed reliable. Only implementation deviations route automatically to builders. Oracle defects require requalification, semantic disputes require domain owners, and integrity violations require independent revalidation. Missing evidence, unsupported semantics, and evaluator outages hold release.

Authorization and conformance answer different questions: $\operatorname{Authorized}(a,M,E)$ concerns action $a$ under mandate $M$ in context $E$; $\operatorname{Conformant}(x,B_v,\mathcal{O})$ concerns behavior $x$ against baseline $B_v$ and evidence $\mathcal{O}$. Correct outputs cannot legitimize restricted-data access; a valid mandate cannot excuse faulty outputs. The proposed integration requires no self-approval, mandate/baseline linkage, revocation blocking new execution and promotion, no pass overriding a denial, and no grant overriding critical FAIL/INCONCLUSIVE. These are requirements, not demonstrated production controls.

A minimal interface conveys `mandateId`, `principalId`, `scope`, `expiresAt`, `baselineDigest`, and `authorizationDecision`. An authorization service owns identity, privilege, and revocation; the verifier owns bindings, verdicts, and counterexamples. Neither rewrites the other's authoritative record. The author's non-peer-reviewed constitutional and polycentric agent governance (CPAG) essay[^1] offers compatible framing, not a required runtime, standard, or evidence of effectiveness. Ordinary repository permissions, protected CI, and human review can implement the same separation.

### 3.4. Application scope and tailoring

These profiles describe intended use, not evaluated organizational cases or evidence of generalization. **Greenfield** work derives authority from approved new policy and scenarios; it lacks a legacy differential reference. **Brownfield** work classifies characterized behavior as preserve, correct, or redesign before approval. Coexistence adds data authority, at-most-once effects, routing, and reconciliation checks; single cutovers need contingency for post-switch writes, not merely rollback. **Application Management Services (AMS)** reuse baselines for regression and treat incidents as observed evidence; hotfixes require documented emergency governance and retrospective reconciliation.

All profiles retain authority separation, immutable baselines, qualification, tri-valued evaluation, recovery, and human release rights. These are process-level adoption criteria, not certification or OMG conformance. A small pilot can use one approved decision, boundary controls, a wrong-threshold mutant, and a builder without baseline-write permission. Add model families only for uncovered risks. Where automation cannot supply a meaningful oracle, record the gap and human evaluation criteria rather than claim automated coverage.

## 4. Responsibility and Information-Flow Model

Figure 2 is an operational model of responsibilities and information flows, not a domain-wide reference architecture. It complements the activity flow in Figure 1 by showing which role owns each decision and what evidence crosses plane boundaries. The authority plane owns approved baselines and mandates; the construction plane produces candidate artifacts; the verification plane binds observations to protected oracles and reports evidence for release decisions. File storage, version control, CI jobs, a candidate application, and one functioning adapter can implement a small deployment; distributed orchestration is optional. The diagram is intentionally non-prescriptive about deployment technology and should not be read as a reusable physical or logical architecture for every domain.

![Figure 2. A tool-neutral model of responsibilities and information flows. Protected approval and oracle evaluation are separate from AI construction.](source/figures/todm_planes_v1.6.pdf)

**Table 2. Risk-selected model families and their executable obligations.**

| Model | Governs | Binding and evidence obligation |
| --- | --- | --- |
| SBVR | Vocabulary and normative business rules | typed terms, business approval, unambiguous operational translation, policy provenance |
| DMN | Input-to-decision logic | typed decision inputs, rule hit policy, expected output, decision trace |
| BPMN | Ordered business activity | correlated events, mandatory activities, allowed paths, sequencing checks |
| CMMN | Case milestones and exceptions | case identity, state transitions, sentries, completion evidence |
| OCL | Invariants and pre-/postconditions | object snapshots, required predicates, scope and evaluator semantics |

**Executability is conditional.** SBVR semantics may be modeled
independently from a code generator; its operational mapping must be
explicit, typed, reviewed, and tested. OCL expressions require a
compatible model and evaluator. BPMN and CMMN XML are not sufficient
without correlating the observed process/case events to model elements.
DMN decision tables require defined input mappings, hit policies, and
expression semantics. Supported model versions and subsets belong in
each adapter's conformance manifest. These caveats prevent the category
error of claiming that five document types automatically constitute five
functioning oracles.

An adapter must validate model syntax, normalize observations, evaluate deterministically under pinned versions/configuration, produce counterexamples and evidence, declare capability limits, and report failures. A machine-readable manifest binds rule identity/version, normative source, approval, severity, semantic profile, required observations, and evaluator version. A TODM-specific JSON encoding is not an OMG encoding; standards-based adapters retain the underlying model and declare supported constructs.

Traceability links requirements, model nodes, oracles, observations, source artifacts, and verdicts, potentially using W3C PROV-O [@w3c2013prov] and KDM [@omg2020kdm]. An optional ontology/knowledge graph can aid retrieval and impact analysis but cannot certify expected behavior, override verdicts, or own approval authority.

## 5. Evaluation Method and Research Questions

The ACM SIGSOFT Engineering Research standard calls for an explicit empirical method and comparative evaluation, or a convincing justification when comparison is impractical [@sigsoftEngineering]. The present work is an *engineering-research proposal with bounded deterministic synthetic checks*, not full compliance with that standard, an organizational case study, a controlled experiment, or comparative effectiveness evidence. Comparison is feasible and planned; the fixtures are not a substitute or an impracticality argument.

### 5.1. Current synthetic check protocol

The executed artifact-preparation protocol evaluates deterministic gate behavior using author-selected, fixed fixtures: known-correct controls, deliberately faulty candidates, incomplete observations, static mandate violations, and demonstration-signature failures. Selection targets explicit acceptance branches, not representative sampling. Expected outcomes come from the artifact's declared rules and fixture assertions, which share a repository and authorship with the evaluator; this supplies a repeatable test reference, not an independently adjudicated business oracle. Repeated checks and overlapping fixture views are not independent observations.

From the historical `demo/` working directory, the first three recorded commands below exercise baseline qualification, signed assurance, and adversarial release gating respectively; the last two check an allow and an expected denial.

```text
python3 scripts/verify_all.py
python3 scripts/verify_signed.py
python3 scripts/test_audit_release.py
python3 scripts/audit_release.py --case GF-01-greenfield-approved --json
python3 scripts/audit_release.py --case GF-03-wrong-threshold --json
```

Assertions compare evaluator verdicts and CLI exits with declared fixture expectations; hashes bind the recorded baseline and outputs. The preserved `demo/results/reproducibility-v0.4.json` records the commands, environment, exits, and hashes. Section 6 reports its historical counts and outcomes; no new execution, randomization, independent assessment, or comparative measurement is claimed.

### 5.2. Questions, rationale, and measures

- **RQ1: Independent fault detection.** Do separately approved oracles reveal shared-specification faults missed by tests derived from the same generated specification? This targets the acceptance gap; compare fault recall on held-out cross-artifact faults, with false positives and inconclusive attempts reported separately.
- **RQ2: Oracle qualification.** Does mutation qualification reduce false confidence relative to unqualified baselines? Evaluators can themselves be wrong; compare non-equivalent mutant detection, false-positive rate, and inconclusive rate on the same held-out set, not the qualification training set.
- **RQ3: Scope and transfer.** Which controls and limitations transfer across greenfield, brownfield, and AMS? Their evidence sources and observation bindings differ; stratify coverage, escapes, and unresolved outcomes by profile rather than assuming generality from fixture labels.
- **RQ4: Governed autonomy.** Can bounded delegation retain acceptance quality without unauthorized baseline edits? Measure independently accepted autonomous work, approval integrity, repair convergence, and severity-stratified escapes; more autonomous work alone is not success.
- **RQ5: Human interpretation.** How often, and why, does human review reverse AI-inferred rules? Approval is a proposed defense against common-mode error; record reviewed proposals, reversals, disagreements, and adjudicated reasons, including mistaken human decisions.
- **RQ6: Authorization boundary.** Does independent mandate enforcement block unauthorized-but-conformant candidates? Behavioral correctness cannot authorize an action; test expired, revoked, and over-scoped mandates separately from oracle failures.

The falsifiable expectations are higher shared-fault recall with independent approval (RQ1), lower false-positive and inconclusive rates after qualification (RQ2), fewer unauthorized baseline changes under protected approval and accepted autonomy without increased critical escapes (RQ4), and blocked unauthorized-but-conformant candidates under independent enforcement (RQ6). Null or adverse outcomes constrain these claims. RQ3 and RQ5 investigate transfer and interpretation rather than presuppose benefit. No economic or demonstrated percentage-autonomy claim is made.

Table 3 operationalizes the planned research questions, not a set of measured outcomes in this paper. The current evaluation reports fixture verdicts and test exits only. Production defect density, human review effects, and accepted autonomous work cannot be inferred from those counts.

**Table 3. Operational metrics. Denominators and exclusions must be declared before evaluation.**

| Metric | Operational definition and interpretation |
| --- | --- |
| Critical rule coverage | Applicable critical rules with executed evaluators divided by all approved applicable critical rules. Disclose exclusions. |
| Oracle mutation detection (OMD) | Correctly detected non-equivalent, executed seeded faults divided by all non-equivalent, executed faults. Disclose unexecuted mutants. |
| False-positive rate (FPR) | Known-correct controls flagged FAIL divided by all known-correct controls executed. |
| Inconclusive rate (IR) | Applicable oracle attempts returning INCONCLUSIVE divided by all applicable attempts; separate data loss from evaluator failure. |
| Traceability completeness | Issued verdicts linked to rule, evidence, build and baseline divided by all issued verdicts. |
| Escaped defect density | Confirmed production defects per predefined capability or change unit, stratified by severity and exposure. |
| Human approval integrity | Baseline changes with independent recorded approval divided by all changes. |
| Mandate conformance | Delegated actions within approved scope and validity divided by all observed delegated actions; report unknown/unobserved actions separately. |
| Revocation enforcement | Attempts to execute or promote after mandate revocation that are correctly blocked divided by all controlled revocation test attempts. |
| Autonomous accepted work share | Eligible accepted work items completed without direct human code edits divided by all eligible accepted items. |
| Repair convergence | Detected candidate violations subsequently repaired and reverified within the mandate; report unresolved items and iteration count. |

### 5.3. Comparative study design (not executed)

The planned mixed-method study uses matched capabilities across the three profiles, with the unexecuted `docs/COMPARATIVE_PROTOCOL.md` defining S1-A (Coupled), S1-B (Independent unqualified), and S1-C (Qualified). S1-A uses agent-assisted specification/tests and standard CI/review; S1-B adds independently approved oracles without mutation qualification; S1-C adds qualification. Hold tools, models, and configuration constant where applicable. Record comparator safeguards rather than treating SDD/TDD/BDD as intrinsically deficient. Rotate conditions across projects/practitioners, counterbalance learning, model versions, and seeds, prevent contamination, and blind assessors to pipeline identity. Separate adversarial mandate trials address RQ6.

Domain specialists will adjudicate expected behavior from approved documentation and counterexamples, independently of construction agents and oracle authors. Seed verified non-equivalent faults in decisions, ordering, case closure, persistence, temporal rules, authorization, and transformations; include known-correct decoys and a held-out fault set. Document exclusions and mutant equivalence decisions. Review logs supply proposal/reversal counts and qualitative disagreement analysis for RQ5.

A pilot-based power analysis will determine sample size; no sample or effect estimate is presently claimed. Repeated runs within a requirement/repository are correlated. Paired or hierarchical analyses and project-cluster interval estimates will report effect sizes, missing evidence, and severity-stratified outcomes. Publish versioned prompts, profiles, manifests, tools, scripts, anonymized evidence, all attempted cases, aborted runs, exceptions, exclusions, and negative results, subject to privacy/IP constraints. Engineering acceptance (compilation, parser checks, tamper/missing-evidence controls, seeded faults, and approval audit) precedes effectiveness evaluation. Independent replication needs an external baseline and assessors plus a fixed commit or archived identifier.

## 6. Illustration and Synthetic Observations

### 6.1. Reasoned shared-specification example

Suppose the authoritative business policy states: requests over EUR 10,000 require human authorization before approval or persistence as approved. A generated SDD specification incorrectly sets the review threshold at EUR 12,000; the generated tests confirm EUR 11,000 should be automatically approved.

Applying the proposed method would proceed as follows; this sequence is illustrative, not a record of a human or agent trial.

1. Frame the approval capability and locate the authoritative EUR 10,000 policy (G0-G1); record its conflict with the generated specification.
2. Have the accountable owner resolve that conflict and approve the exact oracle baseline; qualify it using boundary controls and wrong-threshold mutants (G2-G3).
3. Construct within the mandate and evaluate the candidate's EUR 11,000 decision against the approved baseline (G4-G5). Incorrect automatic approval yields FAIL and returns to construction, without changing the oracle to accommodate the defect.
4. Reverify the repair before a separate human release decision (G6); subsequent operational observations can reopen discovery but cannot silently rewrite the baseline (G7).

**Table 4. Illustrative example; these are reasoned expected outcomes, not experimental results.**

| Control | Relevant observation | Oracle response |
| --- | --- | --- |
| Specification-based tests | 11,000 automatically approved against 12,000 rule | PASS relative to wrong generated specification |
| SBVR-derived norm | policy defines review above 10,000 | semantic mismatch / re-review |
| DMN decision | 11,000 should yield HUMAN_REVIEW | FAIL if automatically approved |
| BPMN process | mandatory review event is absent | FAIL with correlated trace |
| CMMN case | case closed without required review evidence | FAIL when case semantics apply |
| OCL invariant | approved state with no authorizing approval | FAIL against object snapshot |

For a stateless API, DMN plus an invariant may suffice; long-running approvals add process/case obligations. SBVR supplies governed language, whose reviewed operational mapping makes predicates testable. Decision coverage must include amounts at or below the threshold, nulls, currency conversion, re-submissions, priorities, and effective dates. Mapping the wrong threshold into every oracle still permits coherent failure: independent policy evidence and knowledgeable review are essential.

Proposed qualification mutants change the threshold to EUR 12,000, omit review, persist approval before review, duplicate approvals, or close an incomplete case. Controls include EUR 9,999, EUR 10,000, malformed inputs, and missing observations. Record survivors, detections, false alarms, and inconclusive outcomes. This is a reasoned protocol illustration, not a claim that the recorded suite implements every listed scenario.

### 6.2. Recorded engineering checks and provenance

The public [TODM GitHub repository](https://github.com/jmfloreszazo/TODM) puts the article's mechanism into executable, synthetic practice. It contains five limited JSON semantic profiles associated with SBVR, DMN, BPMN, CMMN, and OCL; a deterministic Python evaluator and C#/.NET 10 candidate/scaffold; synthetic greenfield, brownfield, and AMS fixtures; static mandates; demonstration attestations; and a fail-closed release gate. This artifact exercises the proposed gate composition and selected failure modes, not full OMG languages, production identity/enforcement, or industrial effectiveness.

The companion artifact is archived as v1.5.0 at [doi:10.5281/zenodo.23725201](https://doi.org/10.5281/zenodo.23725201), with source revision `61354abc03e73fbf258b6e8d66e35678da134ef8`. This identifies the artifact snapshot, not the original execution commit or an archive of manuscript v1.6.

The preserved `demo/results/reproducibility-v0.4.json` records Python 3.13.5 on `Linux-6.18.55-x86_64-with-glibc2.41`. At artifact preparation, `verify_all.py`, `verify_signed.py`, and `test_audit_release.py` completed nine baseline/qualification, ten signed-assurance, and seven adversarial release-gate tests respectively, each with exit code 0. Across 16 deterministic fixtures, five have passing behavioral and authority controls plus the requisite G6 demonstration signature; eleven are blocked. The behavioral totals are eleven PASS, four FAIL, and one INCONCLUSIVE; five fixtures fail mandate checks. The reference suite's five known-correct controls pass, four seeded mutants violate at least one oracle family, and one incomplete observation is inconclusive. These are overlapping views of selected fixtures, not independent samples.

The recorded CLI invocation for `GF-01-greenfield-approved` returned `DEMO_SIGNED_ALLOW` and exit code 0; `GF-03-wrong-threshold` returned the expected denial, exit code 2. Companion records are `reference-execution.json`, `governance-execution.json`, and `signed-assurance-execution.json` under `demo/results/`. The provenance record retains exact commands, raw output, and SHA-256 hashes of the manifest, attestations, fixtures, mandates, and results. It does not identify a source commit or CI run, so these observations must not be attributed to an invented execution identity. Its original paths and version strings are historical provenance, not a new v1.5 execution.

G2 Ed25519 demonstration signatures bind the manifest digest and model hashes; G6 signatures bind individual fixtures to that digest. Thus neither a conformant unsigned fixture nor a signed but nonconformant or unauthorized fixture is allowed. Public demonstration keys do not establish human identity. Mandates are unsigned static fixtures; no production enforcement point, credential revocation service, protected deployment, or organizational separation is demonstrated. Fixtures and evaluators share a repository and do not establish epistemic independence.

From `demo/`, `python3 scripts/reproduce.py` is the documented reproduction entry point, requiring Python 3.12+ and OpenSSL Ed25519 support. No new execution is claimed here. The historical record states `dotnetCompiledHere=false`; supplied .NET 10 CI configuration is not evidence of local compilation or parity in that preparation environment. These bounded checks leave the effectiveness questions in Section 5 unanswered.

**Interpretation against the research questions.** The seeded-fault checks illustrate mechanisms relevant to RQ1-RQ2, but contain no matched comparison or independent held-out assessment. The mandate fixtures exercise a decision predicate relevant to RQ6, not real enforcement. Profile labels alone do not answer RQ3, and no autonomous-work or human-review study addresses RQ4-RQ5. The practical result is an inspectable demonstration of selected acceptance decisions, not confirmation of the six research questions.

## 7. Threats to Validity

**Construct validity.** Fixture verdicts operationalize selected gate behavior, not business correctness, full OMG semantics, real human approval, or autonomous productivity. Executed missing-evidence and seeded-fault controls distinguish selected failure classes, and explicit JSON-profile limits narrow the claim. They do not establish complete observability, temporal/security coverage, or semantic truth. Independent domain adjudication, richer bindings, and production identity checks remain pending.

**Internal validity.** Author-controlled rules, fixtures, and evaluators share premises and may reproduce the same error; fallible human approval cannot eliminate circularity. Recorded tamper, signature-binding, and fail-closed tests mitigate selected integrity faults, not this common-mode bias. Static mandate checks are not demonstrated enforcement or revocation. Held-out faults, assessor blinding, counterbalancing, independent rule approval, and protected enforcement tests are planned, not executed mitigations.

**External validity.** Sixteen synthetic fixtures and a threshold illustration do not represent organizational modernization or maintenance. Neither real agents nor production systems participate in the recorded checks; asynchronous effects, emergency changes, drift, jurisdictional policy, and probabilistic outputs remain untested. Stating these limits prevents scope inflation but does not solve transfer. Multi-profile organizational studies, cross-runtime replication, and longitudinal observation remain necessary.

**Conclusion validity.** The nine, ten, and seven test counts and fixture outcomes are deterministic checks, not independent trials, recall estimates, or evidence of causal improvement. Exact commands, exits, and hashes support auditability, but the historical record lacks commit/run identity and no comparative baseline or statistical analysis was executed. Power analysis, clustered uncertainty estimates, all-case reporting, and independent replication are prospective safeguards. No production-defect reduction or percentage-autonomy conclusion follows.

## 8. Conclusion and Future Work

TODM specifies an acceptance method built from independently governed oracles, bounded construction, eight recovery-aware gates, three-valued verdicts, and separate authorization and conformance checks. It complements existing development and assurance practices rather than replacing them. The synthetic artifact demonstrates selected deterministic gate behavior only; the comparative research questions remain open.

Future work should progress from protected manifests and reproducible evidence (M0), through decision/invariant adapters (M1), process traces (M2), case controls (M3), and governed vocabulary mappings (M4), to cross-adapter qualification, independent audit, and multi-profile comparison (M5). These are research milestones, not completion claims for full standards engines. Each must publish supported versions, unsupported constructs, deterministic outputs, qualification evidence, and a completion decision. Optional ontology support follows demonstrated need. Cross-platform and organizational replication must establish whether the proposed separation detects consequential defects and sustains accepted autonomy; until then it remains a falsifiable methodological proposal.

## Ethics, Transparency, and Author Responsibility

The reported evidence comes from internal engineering tests of the companion artifact using synthetic scenarios for software modernization, new development, and maintenance. These are not studies involving human participants or production customers. Generative AI assisted drafting, language editing, literature organization, and document production. The author retains responsibility for the technical claims, references, originality, and final manuscript; no AI system is credited as an author.

## Data and Code Availability

Source code, synthetic examples, and reproduction instructions are publicly available in the [TODM GitHub repository](https://github.com/jmfloreszazo/TODM). The repository lets readers inspect and run selected TODM mechanisms in practice, illustrating how the methodology applies to modernization, new development, and maintenance. It is a synthetic demonstrator, not a complete production implementation.

[^1]: *De Leviatán al Autopilot* (2026):
    <https://jmfloreszazo.com/de-leviatan-al-autopilot/>. This
    conceptual essay is not independent empirical validation of CPAG or
    TODM.

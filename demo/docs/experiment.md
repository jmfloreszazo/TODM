# TODM reference experiment — pre-registered-style protocol draft

## Research question
Can an independent, human-governed oracle baseline detect a semantic authorization defect that a deliberately incorrect self-consistent generated test fails to detect?

## Demonstration (not a controlled scientific study)
The business rule is: requests strictly greater than EUR 10,000 require manual review. The `wrong-threshold` mutant uses EUR 12,000. A synthetic request of EUR 11,000 is therefore incorrectly approved. `tests/Todm.Baseline` deliberately asserts the wrong expectation (approval); TODM compares observed behavior to its separate, demo-approved contract and flags the deviation. The baseline test is intentionally constructed and must not be described as representative of SDD/TDD/BDD in general.

## Cases
- 5 nonmutated controls: greenfield, brownfield, AMS, exact threshold, high risk.
- 4 mutants: wrong threshold, skipped manual review, premature case closure, approval of an inactive customer.
- 1 missing-evidence check: remove amount, expect `INCONCLUSIVE`.
- Baseline integrity: modify one byte in any oracle model without updating its manifest SHA-256, expect hard failure.

## Outcome and metrics
The reference Python evaluator was run on these synthetic inputs. The committed `results/reference-execution.json` contains individual observations and findings. Do not infer external validity, statistical power, precision, or industrial defect recall from this constructed sample.

- Synthetic mutant detection: 4/4 (only these seeded mutants).
- Known-correct synthetic controls: 5/5 (only these five controls).
- Missing evidence: `INCONCLUSIVE`.
- No measured effect on real defect rates, human autonomy, model performance, or modernization outcomes.

## To turn this into empirical research
1. Freeze policy sources and oracle models before generating mutants.
2. Create a blind corpus of realistic defects and non-defective changes, reviewed by independent domain experts.
3. Randomize and balance baseline vs TODM conditions; preserve model/tool versions and budgets.
4. Measure per-family and overall recall, precision, false positives, abstentions, gate coverage, traceability, and human interventions.
5. Publish per-case raw observations, adjudications, seeds, model versions, hashes, and limitations.
6. Include both greenfield, brownfield, and AMS projects with external reviewers.

## Extension v0.2: separation of authority and correctness

Sixteen synthetic fixtures in `governance/fixtures.json` cover three application profiles, four seeded behavioral defects, one missing-evidence condition, revoked/out-of-scope/expired/unknown principals, unauthorized actions, and denied release approval. Both Python and .NET runners consume the same fixed fixture set and synthetic evaluation instant.

The key test is a **2 × 2 logical separation**: authorized-but-wrong and correct-but-unauthorized must both block. A third condition requires explicit G6 release approval even if both controls pass. The dashboard visualizes these distinctions, and `scripts/compare_dotnet.py` asserts verdict parity when the SDK is available.

**No industrial claims:** The fixture distribution was intentionally chosen, so the observed blocked count (11/16) is not a field failure rate or measured improvement. A full empirical protocol requires unseen defects, correct decoys, blinded adjudication, independent teams, mutation equivalence review, and project-clustered statistics. See `docs/paper-companion.md`.

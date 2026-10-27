# TODM — Preregisterable empirical evaluation protocol

## Claims under test (NOT established by this demo)

H1: Relative to a matched AI-assisted SDD/TDD/BDD baseline, TODM reduces the rate of independently adjudicated *business-rule* defects escaping release gates. H2: TODM's independently qualified oracle baseline improves detection of policy-drift mutations. H3: Mandatory G2/G6 separation reduces unauthorized acceptance events. H4: TODM may increase inconclusive outcomes; quantify rather than suppress these.

## Unit, design, and preregistration

Register the hypotheses, primary endpoint, inclusion/exclusion criteria, stopping rule, and analysis script **before** running. Use paired tasks on the same codebase and requirements, randomized order, blinded human adjudicators, and controlled agent models/tool versions. Stratify greenfield, brownfield incremental/big-bang, and AMS. Include *known-correct decoys*, ambiguous requirements, and equivalent/non-equivalent mutants. Do not infer generalizability from the synthetic demonstration.

## Independent ground truth

A separate expert panel adjudicates requirements and seeded defects without seeing the candidate oracles. Record disagreements and consensus rules. No builder or oracle author can silently modify ground truth. Maintain immutable versioned evidence of human decisions. Assess both *oracle circularity* and model extraction error.

## Endpoints

Primary: escaped independently adjudicated business-rule defect rate per task, with confidence intervals and paired differences. Secondary: recall, precision, false-positive rate, inconclusive rate, mutation detection for adjudicated non-equivalent mutants, rule/trace coverage, unauthorized release attempts blocked, adjudication burden and trace completeness. **Costs are outside scope.** Report denominators, uncertainty and failure cases.

## Release criteria for research claims

No superiority claim until a preregistered paired experiment with independently adjudicated ground truth has been executed and published, including raw anonymized fixtures, code, checksums, negative outcomes and reproducibility instructions. Demo pass counts are implementation acceptance checks only.

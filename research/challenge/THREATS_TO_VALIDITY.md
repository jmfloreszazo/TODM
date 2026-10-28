# Threats to validity — research challenge

This is a risk register for future studies, **not** a claim that these risks have been eliminated.

| Threat | Why it matters | Proposed mitigation |
| --- | --- | --- |
| Synthetic-only fixtures | May not represent real systems | Independently sampled tasks and transfer studies |
| Oracle author bias | Expected results may encode the same mistake | Independent baseline authors and adjudicators |
| Test leakage | Agents may see the answers | Isolate evaluation material and log access |
| Equivalent mutations | Some mutations do not change behavior | Adjudicate mutation equivalence |
| Missing clean controls | Recall alone hides false positives | Include valid non-defective candidates |
| Unbalanced budgets | More compute may explain gains | Match or disclose time, token and tool budgets |
| Nondeterministic agents | Single runs may mislead | Predefine repeated runs and uncertainty |
| Selection and publication bias | Positive results overrepresented | Publish failures, exclusions and negative results |
| Inconclusive verdicts | Forced binary scoring distorts evidence | Report inconclusive separately and disclose treatment |
| Incomplete ground truth | False positives/negatives may be misclassified | Independent panel and disagreement resolution |
| External validity | One stack/domain may not generalize | Stratify domains and platforms |
| Demo keys and synthetic mandates | Not production trust | Do not claim identity or deployment enforcement |

A challenge submission should identify which threats apply and any residual limitations.

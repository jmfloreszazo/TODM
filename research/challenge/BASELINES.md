# Baselines and comparison controls

This document defines **proposed** comparison arms, not results.

- **A — Conventional:** developer implementation and developer-authored tests, without an independently approved oracle baseline.
- **B — AI-assisted:** agent-generated implementation and tests; log prompts, model versions, harness configuration, and tool usage.
- **C — TODM:** separately approved oracle baseline, oracle qualification, bounded construction, independent evaluation, and separate release authorization.

Follow the canonical [comparative preregistration template](../../docs/COMPARATIVE_PROTOCOL.md). For every arm, use matched tasks, controlled time/tool budgets where feasible, randomized order, and independent adjudication. Keep clean controls as well as faulty cases; assess equivalent mutations. Record failed runs and abstentions. Never infer superiority from the existing synthetic demo.

## Minimum comparison record

| Field | Required |
| --- | --- |
| Task and frozen specification | Yes |
| Arm and evaluator identity | Yes |
| Tool/model version and settings | If applicable |
| Baseline hash and code commit | Yes |
| Ground-truth adjudication method | Yes |
| Seeded defects and clean controls | Yes |
| TP, FP, FN, TN or explicit N/A | Yes |
| Inconclusive and excluded runs | Yes |
| Time and actual cost | Yes |
| Reproducibility commands | Yes |

Preregister the primary endpoint, analysis unit, sample size and stopping criteria **before** measuring outcomes.

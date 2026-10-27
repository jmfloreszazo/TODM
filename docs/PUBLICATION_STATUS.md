# Research verification status — 2026-10-27

## Independently confirmed GitHub Actions

- **Success:** [16-case Python/.NET 10 JSON-policy parity, run 40596778676](https://github.com/jmfloreszazo/TODM/actions/runs/40596778676). This is a **narrow policy subset**, not the full 16-case five-family governance suite.

- **Success:** [TODM cross-language CI, run 40596270705](https://github.com/jmfloreszazo/TODM/actions/runs/40596270705)
- Commit: `ba20a842328285a727fe3608c7f1b131504035b4`
- Python reference: success.
- .NET 10: build and synthetic acceptance tests succeeded.
- Regression fixed: manually constructed JSON integer amounts no longer produce spurious `INCONCLUSIVE`.

## Scope of this confirmation

This proves **the minimal public seed**, not the complete v0.4 prototype. The complete research package includes five limited oracle model profiles, 16 governance scenarios, synthetic signed G2/G6 controls, full academic paper and a Python/C# parity script. Those assets have been prepared separately but **are not yet all present in GitHub**.

## Publication checklist

- [x] Repository public
- [x] MIT license and citation metadata
- [x] Minimal Python/.NET CI green
- [ ] Full research package uploaded and reviewed
- [x] Minimal JSON-policy 16-scenario Python/.NET parity green
- [ ] Full five-family v0.4 16-scenario Python/.NET parity green
- [ ] Versioned release and permanent archive DOI
- [ ] Full paper source linked to exact immutable artifact
- [ ] Independent comparative evaluation

**Research boundary:** The synthetic fixtures are not an industrial study. No production identity, complete OMG semantics or empirical superiority is claimed.

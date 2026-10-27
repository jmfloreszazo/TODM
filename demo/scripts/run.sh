#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! command -v dotnet >/dev/null 2>&1; then echo 'Requires .NET 10 SDK. For reference-only execution: python3 scripts/reference.py experiment' >&2; exit 127; fi
dotnet build src/Todm.Cli/Todm.Cli.csproj -c Release
dotnet build samples/Todm.Candidate/Todm.Candidate.csproj -c Release
dotnet build src/Todm.Governance/Todm.Governance.csproj -c Release
dotnet run --project tests/Todm.Baseline/Todm.Baseline.csproj -c Release
dotnet run --project tests/Todm.Smoke/Todm.Smoke.csproj -c Release
mkdir -p results/evidence results/reports
for name in greenfield brownfield ams; do
  dotnet run --project samples/Todm.Candidate -c Release -- --scenario "scenarios/$name.json" --output "results/evidence/$name.json"
  dotnet run --project src/Todm.Cli -c Release -- verify --contracts contracts/v1 --evidence "results/evidence/$name.json" --report "results/reports/$name.json" --allow-demo-approval >/dev/null
  echo "PASS $name"
done
# A failure is EXPECTED; do not mask unexpected PASS or errors.
dotnet run --project samples/Todm.Candidate -c Release -- --scenario scenarios/brownfield.json --mutation skip-review --output results/evidence/brownfield-mutated.json
set +e
dotnet run --project src/Todm.Cli -c Release -- verify --contracts contracts/v1 --evidence results/evidence/brownfield-mutated.json --report results/reports/brownfield-mutated.json --allow-demo-approval >/dev/null
code=$?
set -e
if [ "$code" -ne 2 ]; then echo "ERROR: expected FAIL exit 2, got $code" >&2; exit 1; fi
echo 'EXPECTED FAIL: brownfield mutant blocked by independent oracle gate'

# Cross-check the synthetic authority plane against the Python reference.
python3 scripts/verify_all.py
dotnet run --project src/Todm.Governance -c Release
python3 scripts/compare_dotnet.py
python3 scripts/build_dashboard.py
echo 'TODM v0.2: reference, .NET and governance verdict parity PASS'

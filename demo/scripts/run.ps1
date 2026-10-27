$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) { throw 'Requires .NET 10 SDK' }
dotnet build src/Todm.Cli/Todm.Cli.csproj -c Release
if ($LASTEXITCODE -ne 0) { throw 'Build failed' }
dotnet run --project tests/Todm.Smoke -c Release
if ($LASTEXITCODE -ne 0) { throw 'Smoke tests failed' }
New-Item -ItemType Directory -Force results/evidence, results/reports | Out-Null
foreach ($name in @('greenfield','brownfield','ams')) {
  dotnet run --project samples/Todm.Candidate -c Release -- --scenario "scenarios/$name.json" --output "results/evidence/$name.json"
  if ($LASTEXITCODE -ne 0) { throw 'Candidate failed' }
  dotnet run --project src/Todm.Cli -c Release -- verify --contracts contracts/v1 --evidence "results/evidence/$name.json" --report "results/reports/$name.json" --allow-demo-approval
  if ($LASTEXITCODE -ne 0) { throw "Unexpected oracle gate failure for $name" }
}
Write-Host 'All three controls PASS. For negative tests see tests/Todm.Smoke.'

python scripts/verify_all.py
if ($LASTEXITCODE -ne 0) { throw 'Reference qualification failed' }
dotnet run --project src/Todm.Governance -c Release
if ($LASTEXITCODE -ne 0) { throw 'Governance fixture validation failed' }
python scripts/compare_dotnet.py
if ($LASTEXITCODE -ne 0) { throw 'Reference/.NET parity failed' }
python scripts/build_dashboard.py

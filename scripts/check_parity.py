#!/usr/bin/env python3
"""Cross-language parity for 16 synthetic JSON-policy fixtures (not full OMG semantics)."""
from __future__ import annotations
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from todm_demo import load_baseline, evaluate, release_gate

def reference():
    policy, digest = load_baseline()
    fixtures = json.loads((ROOT / "tests/fixtures/policy-cases.json").read_text())
    assert fixtures["kind"] == "TODM_SYNTHETIC_POLICY_PARITY_V1"
    results = []
    for case in fixtures["cases"]:
        oracle = evaluate(case["observation"], policy)["verdict"]
        gate = release_gate({"verdict": oracle},
                            mandate_active=case["mandateActive"],
                            approval_g6=case["g6Approved"],
                            baseline_sha256="tampered" if case["tamperBaseline"] else digest,
                            approved_baseline_sha256=digest)["decision"]
        assert (oracle, gate) == (case["expectedOracle"], case["expectedRelease"]), case["id"]
        results.append({"id": case["id"], "oracle": oracle, "release": gate})
    assert len(results) == 16
    return results

def main():
    expected = reference()
    print(f"Python reference: {len(expected)} synthetic policy cases PASS")
    if "--dotnet" not in sys.argv:
        print("C# parity not checked (pass --dotnet to run .NET 10)")
        return
    proc = subprocess.run(["dotnet", "run", "--project",
                           "dotnet/Todm.Seed/Todm.Seed.csproj", "-c", "Release",
                           "--no-build", "--", "--batch"],
                          cwd=ROOT, capture_output=True, text=True)
    if proc.returncode:
        raise RuntimeError("C# batch failed:\n" + proc.stdout + proc.stderr)
    result = json.loads(proc.stdout)
    assert result["kind"] == "TODM_SYNTHETIC_POLICY_PARITY_V1"
    assert result["mismatches"] == 0
    assert result["cases"] == expected, "Python/C# verdict mismatch"
    print(f"Python/.NET 10 parity: {len(expected)}/{len(expected)} synthetic policy cases PASS")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Compare C# and Python verdicts, not implementation-specific diagnostic wording."""
import json
from pathlib import Path
from reference import ROOT

python=json.loads((ROOT/'results/governance-execution.json').read_text())
net=json.loads((ROOT/'results/governance-dotnet.json').read_text())
a={x['caseId']:x for x in python['cases']}
b={x['caseId']:x for x in net['cases']}
assert a.keys()==b.keys(),(a.keys()-b.keys(),b.keys()-a.keys())
for case_id in a:
    for key in ('oracleVerdict','authorityVerdict','releaseOutcome'):
        assert a[case_id][key]==b[case_id][key],(case_id,key,a[case_id][key],b[case_id][key])
    assert a[case_id]['oracleFamilies']==b[case_id]['oracleFamilies'],(case_id,'oracleFamilies')
assert python['summary']==net['summary'],(python['summary'],net['summary'])
print(f'Python/.NET verdict parity: {len(a)} fixtures × 3 control verdicts + five oracle families + summary = PASS')

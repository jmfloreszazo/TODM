#!/usr/bin/env python3
"""Fail-closed, offline G2+G5+mandate+G6 gate. No deployment, no real identity."""
import argparse, hashlib, json, sys
from pathlib import Path
from signed_assurance import baseline_attested, gate
from governance import ROOT, run_case


def evaluate(case_id):
    fixtures=json.loads((ROOT/'governance/fixtures.json').read_text())['cases']
    fixture=next((f for f in fixtures if f['id']==case_id),None)
    if fixture is None:
        return {'caseId':case_id,'outcome':'BLOCK','reason':'Unknown case ID'}
    try:
        models,digest=baseline_attested()
        mandates=json.loads((ROOT/'governance/mandates.json').read_text())
        case=run_case(fixture,models,mandates,digest)
        result=gate(case_id,case['oracleVerdict'],case['authorityVerdict'],digest)
        return {'caseId':case_id,'outcome':result,'oracle':case['oracleVerdict'],
                'authority':case['authorityVerdict'],'baselineManifestSha256':digest,
                'reason':'Synthetic cryptographic gate; NOT a real deployment approval',
                'g2Attested':True,'g6SignatureVerified':result=='DEMO_SIGNED_ALLOW'}
    except (ValueError,KeyError,TypeError,AssertionError,OSError) as e:
        return {'caseId':case_id,'outcome':'BLOCK','reason':'Fail-closed: '+str(e)}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',required=True,help='Exact fixture caseId')
    p.add_argument('--json',action='store_true')
    a=p.parse_args(); result=evaluate(a.case)
    print(json.dumps(result,indent=2) if a.json else f"{result['caseId']}: {result['outcome']} ({result['reason']})")
    sys.exit(0 if result['outcome']=='DEMO_SIGNED_ALLOW' else 2)

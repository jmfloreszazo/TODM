#!/usr/bin/env python3
"""Detached Ed25519 attestation and two-plane fail-closed gate. DEMO identities only."""
import hashlib,json,pathlib,subprocess,sys
from governance import ROOT, run_case
from reference import load_baseline
BASE=ROOT/'assurance'

def signed_json(name,role):
    payload=BASE/'signed'/(name+'.json')
    signature=BASE/'signed'/(name+'.sig')
    public=BASE/'public'/(role+'.pem')
    if not all(p.is_file() for p in (payload,signature,public)):
        raise ValueError('Missing attestation/signature/trust anchor')
    p=subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(public),'-rawin','-in',str(payload),'-sigfile',str(signature)],capture_output=True,text=True)
    if p.returncode!=0:raise ValueError('Invalid Ed25519 signature')
    data=json.loads(payload.read_text())
    if payload.read_bytes() != (json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode():
        raise ValueError('Noncanonical attestation')
    return data

def baseline_attested():
    # Verify content hashes first and separately authenticate the manifest digest.
    manifest,models=load_baseline()
    digest=hashlib.sha256((ROOT/'contracts/v1/manifest.json').read_bytes()).hexdigest()
    att=signed_json('g2-baseline','g2-owner')
    if att.get('kind')!='TODM_G2_DEMO_ATTESTATION' or att.get('manifestSha256')!=digest or att.get('approverRole')!='oracle-owner':
        raise ValueError('G2 attestation does not match baseline')
    return models,digest

def gate(case,oracle,authority,digest):
    if oracle!='PASS' or authority!='PASS':return 'BLOCK'
    try:att=signed_json('g6-'+case,'g6-owner')
    except (ValueError,FileNotFoundError):return 'BLOCK'
    if (att.get('kind')!='TODM_G6_DEMO_APPROVAL' or att.get('caseId')!=case or
        att.get('manifestSha256')!=digest or att.get('approverRole')!='release-owner'):
        return 'BLOCK'
    return 'DEMO_SIGNED_ALLOW'

def experiment():
    models,digest=baseline_attested()
    mandates=json.loads((ROOT/'governance/mandates.json').read_text())
    fixtures=json.loads((ROOT/'governance/fixtures.json').read_text())['cases']
    records=[]
    for f in fixtures:
        case=run_case(f,models,mandates,digest)
        result=gate(f['id'],case['oracleVerdict'],case['authorityVerdict'],digest)
        expected='DEMO_SIGNED_ALLOW' if f['expectedOutcome']=='SIMULATED_ALLOW' else 'BLOCK'
        if result!=expected:raise AssertionError((f['id'],result,expected))
        records.append({'caseId':f['id'],'oracle':case['oracleVerdict'],'authority':case['authorityVerdict'],'signedGate':result})
    result={'kind':'SYNTHETIC_CRYPTOGRAPHIC_ASSURANCE_NOT_REAL_HUMAN_IDENTITY','version':'0.3.0',
            'summary':{'cases':len(records),'signedAllows':sum(x['signedGate']=='DEMO_SIGNED_ALLOW' for x in records),'blocks':sum(x['signedGate']=='BLOCK' for x in records)},'cases':records}
    (ROOT/'results/signed-assurance-execution.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TODM v0.3 signed assurance:',result['summary'])
    return result
if __name__=='__main__':experiment()

#!/usr/bin/env python3
"""Reproduce all synthetic reference controls and write a provenance manifest."""
import hashlib,json,os,pathlib,platform,subprocess,sys,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
COMMANDS=[['python3','scripts/verify_all.py'],['python3','scripts/verify_signed.py'],
          ['python3','scripts/test_audit_release.py'],
          ['python3','scripts/audit_release.py','--case','GF-01-greenfield-approved','--json']]

def main():
    commands=[]
    for cmd in COMMANDS:
        p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        commands.append({'command':' '.join(cmd),'exitCode':p.returncode,'stdoutTail':p.stdout[-800:], 'stderrTail':p.stderr[-800:]})
        if p.returncode:raise RuntimeError('Reproduction failed: '+ ' '.join(cmd)+'\n'+p.stderr[-1500:])
    # Expected denial must return exit code 2, not 0.
    denied=subprocess.run(['python3','scripts/audit_release.py','--case','GF-03-wrong-threshold','--json'],cwd=ROOT,capture_output=True,text=True)
    if denied.returncode!=2 or json.loads(denied.stdout)['outcome']!='BLOCK':
        raise RuntimeError('Negative-control release gate failed')
    commands.append({'command':'python3 scripts/audit_release.py --case GF-03-wrong-threshold --json', 'exitCode':denied.returncode,'expectedDenial':True})
    files=['contracts/v1/manifest.json','assurance/signed/g2-baseline.json','assurance/signed/g2-baseline.sig',
           'governance/fixtures.json','governance/mandates.json','results/reference-execution.json',
           'results/governance-execution.json','results/signed-assurance-execution.json']
    hashes={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}
    result={'kind':'TODM_SYNTHETIC_REPRODUCIBILITY_RECORD','version':'1.4.0','profileSchemaVersion':'0.4.0',
            'warning':'These are deterministic synthetic engineering tests, not industrial outcomes or real human identity.',
            'pythonVersion':platform.python_version(),'platform':platform.platform(),
            'commands':commands,'sha256':hashes,'allExpectedChecksPassed':True,
            'dotnetCompiledHere':False}
    dest=ROOT/'results/reproducibility-v1.4.json';dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('TODM v1.4: reference, signed controls, adversarial tests and fail-closed CLI verified')
    print('Evidence:',dest)
if __name__=='__main__':main()

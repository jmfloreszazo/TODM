#!/usr/bin/env python3
"""Executable Python reference for TODM demonstration profiles; no external dependencies.
Not a standards-conformant OMG interpreter or a substitute for .NET compilation.
"""
import argparse, hashlib, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
FAMILIES=('sbvr','dmn','bpmn','cmmn','ocl')

def load_baseline(path=ROOT/'contracts/v1'):
    path=pathlib.Path(path)
    manifest=json.loads((path/'manifest.json').read_text())
    assert manifest['approvalKind']=='DEMO_SIMULATED', 'Only simulated approval supported'
    models={}
    for family in FAMILIES:
        name=f'{family}.json'
        raw=(path/name).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=manifest['sha256'][name]:
            raise ValueError(f'Baseline integrity failed: {name}')
        models[family]=json.loads(raw)
    return manifest,models

def candidate(s,mutation='none'):
    threshold=12000 if mutation=='wrong-threshold' else 10000
    decision=('REJECT' if not s['customerActive'] and mutation!='approve-inactive' else
              'REVIEW' if s['risk']=='high' or s['amount']>threshold else 'APPROVE')
    events=['start','validate','decide']
    if decision=='REVIEW': events+=['review','wait_approval']
    elif decision=='APPROVE': events+=['approve','complete']
    else: events+=['reject','complete']
    closed=decision!='REVIEW';approved=decision=='APPROVE';review=decision=='REVIEW'
    if mutation=='skip-review' and decision=='REVIEW':
        events=['start','validate','decide','approve','complete'];closed=True;approved=True;review=False
    if mutation=='close-pending' and decision=='REVIEW':
        events.append('complete');closed=True
    return {**s,'scenario':s['id'],'decision':decision,'events':events,'caseClosed':closed,
            'caseStage':'completed' if closed else 'awaiting_approval',
            'approved':approved,'manualReview':review,'humanApproval':False,
            'decisionRecorded':True,'mutation':mutation}

def pred(p,obs):
    if 'and' in p:
        vals=[pred(v,obs) for v in p['and']]
        return False if False in vals else None if None in vals else True
    field=p['field'];v=obs.get(field)
    if v is None:return None
    if 'equals' in p:return v==p['equals']
    if 'notEquals' in p:return v!=p['notEquals']
    if 'gt' in p:return v>p['gt'] if isinstance(v,(float,int)) else None
    raise ValueError('Unsupported predicate')

def verify(models,obs):
    results={k:[] for k in FAMILIES}
    def record(family,id_,passed,message):
        if passed is not True:results[family].append({'ruleId':id_,'verdict':'INCONCLUSIVE' if passed is None else 'FAIL','message':message})
    for rule in models['sbvr']['rules']:
        trigger=pred(rule['when'],obs)
        outcome=True if trigger is False else None if trigger is None else pred(rule['require'],obs)
        record('sbvr',rule['id'],outcome,'Business rule')
    expected=None
    for rule in models['dmn']['rules']:
        checks=[]
        for field,value in rule['when'].items():
            if field=='amountGt':checks.append(obs['amount']>value if isinstance(obs.get('amount'),(float,int)) else None)
            else:checks.append(obs.get(field)==value if field in obs and obs[field] is not None else None)
        if None in checks and False not in checks:
            record('dmn','DMN-INPUT',None,'Missing decision input');break
        if all(checks):expected=rule['result'];break
    if expected is not None:record('dmn','DMN-DECISION',obs.get('decision')==expected if 'decision' in obs else None,f'Expected {expected}, got {obs.get("decision")}')
    trace=obs.get('events')
    if not isinstance(trace,list):record('bpmn','BPMN-EVENTS',None,'Missing events')
    else:
        record('bpmn','BPMN-START',len(trace)>0 and trace[0]=='start','Invalid start')
        allowed={tuple(x) for x in models['bpmn']['transitions']}
        for a,b in zip(trace,trace[1:]):record('bpmn','BPMN-EDGE',(a,b) in allowed,f'Invalid transition {a}->{b}')
        required=models['bpmn']['requiredByDecision'].get(obs.get('decision'))
        if required is None:record('bpmn','BPMN-DECISION',None,'Missing/unknown decision')
        else:
            for event in required:record('bpmn','BPMN-REQUIRED',event in trace,f'Missing {event}')
    for family,key in [('cmmn','constraints'),('ocl','invariants')]:
        for rule in models[family][key]:
            trigger=pred(rule['when'],obs)
            outcome=True if trigger is False else None if trigger is None else pred(rule['require'],obs)
            record(family,rule['id'],outcome,'Constraint violated')
    verdicts={f:'FAIL' if any(x['verdict']=='FAIL' for x in findings) else 'INCONCLUSIVE' if findings else 'PASS' for f,findings in results.items()}
    overall='FAIL' if 'FAIL' in verdicts.values() else 'INCONCLUSIVE' if 'INCONCLUSIVE' in verdicts.values() else 'PASS'
    return {'scenario':obs.get('scenario'),'verdict':overall,'families':verdicts,'findings':results}

def experiment():
    _,models=load_baseline()
    cases=[('greenfield','none','PASS'),('brownfield','none','PASS'),('ams','none','PASS'),
           ('boundary','none','PASS'),('highrisk','none','PASS'),
           ('greenfield','wrong-threshold','FAIL'),('brownfield','skip-review','FAIL'),
           ('brownfield','close-pending','FAIL'),('ams','approve-inactive','FAIL')]
    reports=[]
    for name,mutation,expected in cases:
        s=json.loads((ROOT/'scenarios'/f'{name}.json').read_text())
        if mutation=='wrong-threshold':s['amount']=11000
        obs=candidate(s,mutation);r=verify(models,obs)
        if r['verdict']!=expected:raise AssertionError((name,mutation,expected,r))
        reports.append({'scenario':name,'mutation':mutation,'expected':expected,**r})
    incomplete=candidate(json.loads((ROOT/'scenarios/greenfield.json').read_text()))
    del incomplete['amount']
    assert verify(models,incomplete)['verdict']=='INCONCLUSIVE'
    result={'kind':'SYNTHETIC_REFERENCE_EXECUTION_NOT_DOTNET','caseCount':len(cases),
            'passControls':sum(x['verdict']=='PASS' for x in reports),
            'failMutants':sum(x['verdict']=='FAIL' for x in reports),
            'inconclusiveMissingEvidence':True,'results':reports}
    out=ROOT/'results/reference-execution.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Python reference: 5 controls PASS; 4 seeded mutants FAIL; missing evidence INCONCLUSIVE')
    print('Wrote',out)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['experiment','check-baseline']);args=p.parse_args()
    if args.command=='experiment':experiment()
    else:load_baseline();print('Integrity OK. Simulated approval only.')

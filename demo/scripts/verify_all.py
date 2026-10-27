#!/usr/bin/env python3
"""Executable qualification controls for the Python reference implementation."""
import copy
import json
import pathlib
import shutil
import sys
import tempfile
import unittest
from reference import ROOT, candidate, load_baseline, verify, experiment as oracle_experiment
from governance import authority_verdict, experiment as governance_experiment, release_verdict

class Qualification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _,cls.models=load_baseline()
        cls.mandates=json.loads((ROOT/'governance/mandates.json').read_text())
    def test_baseline_integrity(self):
        with tempfile.TemporaryDirectory() as temp:
            path=pathlib.Path(temp)
            shutil.copytree(ROOT/'contracts/v1',path/'v1')
            target=path/'v1/dmn.json'
            target.write_text(target.read_text().replace('10000','12000'))
            with self.assertRaisesRegex(ValueError,'integrity failed'):
                load_baseline(path/'v1')
    def test_manifest_only_tamper(self):
        with tempfile.TemporaryDirectory() as temp:
            path=pathlib.Path(temp)
            shutil.copytree(ROOT/'contracts/v1',path/'v1')
            target=path/'v1/manifest.json'
            target.write_text(target.read_text().replace('1.0.0-demo','forged-demo'))
            # The manifest is not signed; this change is NOT detected by model-file hashes.
            manifest,_=load_baseline(path/'v1')
            self.assertEqual(manifest['version'],'forged-demo')
    def test_incomplete_evidence(self):
        s=json.loads((ROOT/'scenarios/greenfield.json').read_text())
        o=candidate(s);del o['amount']
        self.assertEqual(verify(self.models,o)['verdict'],'INCONCLUSIVE')
    def test_unknown_mandate(self):
        req={'principal':'unknown','action':'modify-service','scope':'approvals-service','at':'2026-10-27T12:00:00Z'}
        self.assertEqual(authority_verdict(self.mandates,req)['verdict'],'FAIL')
    def test_missing_authorization_field(self):
        self.assertEqual(authority_verdict(self.mandates,{'principal':'agent-01'})['verdict'],'INCONCLUSIVE')
    def test_release_cannot_bypass_fail(self):
        approved={'kind':'DEMO_SIMULATED','approved':True,'approverRole':'release-owner'}
        for a,b in [('FAIL','PASS'),('PASS','FAIL'),('INCONCLUSIVE','PASS'),('PASS','INCONCLUSIVE')]:
            with self.subTest(oracle=a,mandate=b):
                self.assertEqual(release_verdict(a,b,approved)['outcome'],'BLOCK')
    def test_release_requires_explicit_simulated_approval(self):
        self.assertEqual(release_verdict('PASS','PASS',None)['outcome'],'BLOCK')
    def test_each_oracle_family_exercised_by_a_seeded_mutant(self):
        from governance import run_case
        import hashlib
        fixtures=json.loads((ROOT/'governance/fixtures.json').read_text())
        digest=hashlib.sha256((ROOT/'contracts/v1/manifest.json').read_bytes()).hexdigest()
        failures=set()
        for fixture in fixtures['cases']:
            if fixture.get('mutation','none')=='none':
                continue
            case=run_case(fixture,self.models,self.mandates,digest)
            failures.update(family for family,v in case['oracleFamilies'].items() if v=='FAIL')
        self.assertEqual(failures,{'sbvr','dmn','bpmn','cmmn','ocl'})

    def test_qualification_suite(self):
        self.assertEqual(governance_experiment()['summary'],{
            'caseCount':16,'oraclePass':11,'oracleFail':4,'oracleInconclusive':1,
            'mandateFail':5,'simulatedAllow':5,'blocked':11})

if __name__=='__main__':
    oracle_experiment()
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""Adversarial checks for cryptographic demo. Restores all modified bytes."""
import json,sys,unittest
from pathlib import Path
from signed_assurance import ROOT,baseline_attested,gate,experiment,signed_json
class Tests(unittest.TestCase):
 def test_valid_signed_baseline(self):
  _,digest=baseline_attested();self.assertEqual(len(digest),64)
 def test_16_fixture_gate(self):
  self.assertEqual(experiment()['summary'],{'cases':16,'signedAllows':5,'blocks':11})
 def test_signed_g6_required(self):
  _,digest=baseline_attested();self.assertEqual(gate('nonexistent','PASS','PASS',digest),'BLOCK')
 def test_authority_denied_even_if_signed(self):
  _,digest=baseline_attested()
  allowed=json.loads((ROOT/'results/signed-assurance-execution.json').read_text())['cases']
  case=next(x['caseId'] for x in allowed if x['signedGate']=='DEMO_SIGNED_ALLOW')
  self.assertEqual(gate(case,'PASS','FAIL',digest),'BLOCK')
 def test_oracle_denied_even_if_signed(self):
  _,digest=baseline_attested()
  allowed=json.loads((ROOT/'results/signed-assurance-execution.json').read_text())['cases']
  case=next(x['caseId'] for x in allowed if x['signedGate']=='DEMO_SIGNED_ALLOW')
  self.assertEqual(gate(case,'FAIL','PASS',digest),'BLOCK')
 def test_g6_case_binding_no_replay(self):
  _,digest=baseline_attested()
  self.assertEqual(gate('GF-08-unapproved-release','PASS','PASS',digest),'BLOCK')
 def test_g6_wrong_digest(self):
  allowed=json.loads((ROOT/'results/signed-assurance-execution.json').read_text())['cases']
  case=next(x['caseId'] for x in allowed if x['signedGate']=='DEMO_SIGNED_ALLOW')
  self.assertEqual(gate(case,'PASS','PASS','0'*64),'BLOCK')
 def test_tamper_g2_signature(self):
  p=ROOT/'assurance/signed/g2-baseline.json';orig=p.read_bytes()
  try:
   p.write_bytes(orig.replace(b'oracle-owner',b'oracle-admin'))
   with self.assertRaises(ValueError):baseline_attested()
  finally:p.write_bytes(orig)
 def test_tamper_g6_signature(self):
  allowed=json.loads((ROOT/'results/signed-assurance-execution.json').read_text())['cases']
  case=next(x['caseId'] for x in allowed if x['signedGate']=='DEMO_SIGNED_ALLOW')
  p=ROOT/'assurance/signed'/('g6-'+case+'.json');orig=p.read_bytes()
  _,digest=baseline_attested()
  try:
   p.write_bytes(orig.replace(b'release-owner',b'release-admin'))
   self.assertEqual(gate(case,'PASS','PASS',digest),'BLOCK')
  finally:p.write_bytes(orig)
 def test_tamper_manifest_and_rehash_model(self):
  p=ROOT/'contracts/v1/manifest.json';orig=p.read_bytes()
  try:
   p.write_bytes(orig.replace(b'1.0.0-demo',b'2.0.0-demo'))
   with self.assertRaises(ValueError):baseline_attested()
  finally:p.write_bytes(orig)
if __name__=='__main__':unittest.main(verbosity=2)

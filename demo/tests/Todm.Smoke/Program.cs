using System.Text.Json.Nodes;
using Todm.Engine;
using Todm.Candidate;

var baseline=OracleBaseline.Load("contracts/v1",true);
var cases=new[]{
 ("scenarios/greenfield.json","none","PASS"),
 ("scenarios/brownfield.json","none","PASS"),
 ("scenarios/ams.json","none","PASS"),
 ("scenarios/boundary.json","none","PASS"),
 ("scenarios/highrisk.json","none","PASS"),
 ("scenarios/greenfield.json","wrong-threshold","FAIL"),
 ("scenarios/brownfield.json","skip-review","FAIL"),
 ("scenarios/brownfield.json","close-pending","FAIL"),
 ("scenarios/ams.json","approve-inactive","FAIL")
};
var passed=0;
foreach(var (path,mutation,expected) in cases)
{
 var input=OracleBaseline.ParseObject(File.ReadAllText(path));
 if(mutation=="wrong-threshold") input["amount"]=11000m;
 var observation=Candidate.Run(input,mutation);
 var report=OracleEngine.Verify(baseline,observation);
 if(report.Verdict!=expected) throw new Exception($"{path}/{mutation}: expected {expected}, got {report.Verdict}");
 Console.WriteLine($"{path} [{mutation}]: {report.Verdict}");passed++;
}
var missing=Candidate.Run(OracleBaseline.ParseObject(File.ReadAllText("scenarios/greenfield.json")));
missing.Remove("amount");
if(OracleEngine.Verify(baseline,missing).Verdict!="INCONCLUSIVE") throw new Exception("Missing amount must be INCONCLUSIVE");
passed++;
Console.WriteLine($"PASS: {passed} smoke assertions");

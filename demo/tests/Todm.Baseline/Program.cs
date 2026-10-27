using System.Text.Json.Nodes;
using Todm.Candidate;
// Deliberately flawed test expectation from a hypothetical incorrect SDD spec.
// NOT an empirical comparison of real SDD/TDD/BDD workflows.
var scenario=JsonNode.Parse(File.ReadAllText("scenarios/greenfield.json"))!.AsObject();
scenario["amount"]=11000m;
var observed=Candidate.Run(scenario,"wrong-threshold");
if(observed["decision"]!.GetValue<string>()!="APPROVE") throw new Exception("Hypothetical generated test unexpectedly failed");
Console.WriteLine("BASELINE TEST PASS (WRONG): 11000 approved under incorrectly assumed 12000 threshold");
Console.WriteLine("The independent TODM oracle gate correctly rejects the same behavior.");

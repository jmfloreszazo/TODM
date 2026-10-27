using System.Text.Json;
using System.Text.Json.Nodes;
using Todm.Engine;

try
{
    string? Arg(string key) {var i=Array.IndexOf(args,key);return i>=0 && i+1<args.Length ? args[i+1] : null;}
    if(args.Length==0 || !new[]{"verify","check-baseline"}.Contains(args[0]))
        throw new ArgumentException("Usage: verify --contracts contracts/v1 --evidence evidence.json --allow-demo-approval [--report report.json]; or check-baseline --contracts contracts/v1 --allow-demo-approval");
    var baseline=OracleBaseline.Load(Arg("--contracts") ?? "contracts/v1",args.Contains("--allow-demo-approval"));
    if(args[0]=="check-baseline") {Console.WriteLine($"Baseline {baseline.Version}: integrity OK; approval is SIMULATED ONLY");return;}
    var evidencePath=Arg("--evidence") ?? throw new ArgumentException("Missing --evidence");
    var evidence=OracleBaseline.ParseObject(File.ReadAllText(evidencePath));
    var result=OracleEngine.Verify(baseline,evidence);
    var json=JsonSerializer.Serialize(result,new JsonSerializerOptions{WriteIndented=true});
    var output=Arg("--report");
    if(output is not null) {Directory.CreateDirectory(Path.GetDirectoryName(Path.GetFullPath(output))!);File.WriteAllText(output,json);}
    Console.WriteLine(json);
    Environment.ExitCode=result.Verdict switch {"PASS"=>0,"FAIL"=>2,_=>3};
}
catch(Exception ex) {Console.Error.WriteLine("TODM ERROR: "+ex.Message);Environment.ExitCode=4;}

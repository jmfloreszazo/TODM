using System.Text.Json.Nodes;
using Todm.Candidate;

try
{
    string? Arg(string key) {var i=Array.IndexOf(args,key);return i>=0 && i+1<args.Length ? args[i+1] : null;}
    var scenario=Arg("--scenario") ?? throw new ArgumentException("Use --scenario <file>");
    var mutation=Arg("--mutation") ?? "none";
    var input=JsonNode.Parse(File.ReadAllText(scenario)) as JsonObject ?? throw new InvalidDataException("Invalid scenario");
    var output=Candidate.Run(input,mutation).ToJsonString(new System.Text.Json.JsonSerializerOptions{WriteIndented=true});
    var path=Arg("--output");
    if(path is null) Console.WriteLine(output);
    else {Directory.CreateDirectory(Path.GetDirectoryName(Path.GetFullPath(path))!);File.WriteAllText(path,output);Console.WriteLine(path);}
}
catch(Exception ex) {Console.Error.WriteLine(ex.Message);Environment.ExitCode=4;}

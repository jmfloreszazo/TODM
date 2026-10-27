using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace Todm.Engine;

public sealed record Finding(string Family, string RuleId, string Verdict, string Message);
public sealed record FamilyResult(string Family, string Verdict, List<Finding> Findings);
public sealed record VerificationReport(string Scenario, string Baseline, string Verdict, List<FamilyResult> Families);

/// <summary>Demonstration JSON profiles, not conformant implementations of OMG SBVR/DMN/BPMN/CMMN/OCL.</summary>
public sealed class OracleBaseline
{
    public string Version { get; }
    public IReadOnlyDictionary<string, JsonObject> Models { get; }
    private OracleBaseline(string version, Dictionary<string, JsonObject> models) { Version=version; Models=models; }
    public static OracleBaseline Load(string directory, bool allowDemoApproval)
    {
        var manifest = ParseObject(File.ReadAllText(Path.Combine(directory,"manifest.json")));
        if (manifest["approvalKind"]?.GetValue<string>() != "DEMO_SIMULATED")
            throw new InvalidDataException("Unsupported approval kind. This prototype only supports explicit simulated approvals.");
        if (!allowDemoApproval)
            throw new InvalidDataException("Demo approval is not a real human signature. Pass --allow-demo-approval explicitly.");
        var version = manifest["version"]?.GetValue<string>() ?? throw new InvalidDataException("Missing version");
        var hashes = manifest["sha256"] as JsonObject ?? throw new InvalidDataException("Missing manifest hashes");
        var models = new Dictionary<string,JsonObject>(StringComparer.Ordinal);
        foreach (var family in new[]{"sbvr","dmn","bpmn","cmmn","ocl"})
        {
            var filename = family+".json";
            var expected = hashes[filename]?.GetValue<string>() ?? throw new InvalidDataException($"Missing digest for {filename}");
            var actual = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(Path.Combine(directory,filename)))).ToLowerInvariant();
            if (!string.Equals(actual,expected,StringComparison.Ordinal))
                throw new InvalidDataException($"Baseline integrity failed for {filename}");
            models[family] = ParseObject(File.ReadAllText(Path.Combine(directory,filename)));
        }
        return new OracleBaseline(version,models);
    }
    public static JsonObject ParseObject(string text) => JsonNode.Parse(text) as JsonObject ?? throw new InvalidDataException("Expected JSON object");
}

public static class OracleEngine
{
    private static string? String(JsonObject o, string field) => o[field] is JsonValue v && v.TryGetValue<string>(out var s) ? s : null;
    private static bool? Bool(JsonObject o, string field) => o[field] is JsonValue v && v.TryGetValue<bool>(out var b) ? b : null;
    private static decimal? Number(JsonObject o, string field) => o[field] is JsonValue v && decimal.TryParse(v.ToJsonString(), System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out var n) ? n : null;
    private static bool? Predicate(JsonObject condition, JsonObject observation)
    {
        if (condition["and"] is JsonArray parts)
        {
            var values=parts.Select(p=>Predicate(p as JsonObject ?? throw new InvalidDataException("Invalid AND predicate"),observation)).ToList();
            if (values.Any(v=>v==false)) return false;
            return values.Any(v=>v is null) ? null : true;
        }
        var field=String(condition,"field") ?? throw new InvalidDataException("Predicate missing field");
        if (!observation.ContainsKey(field) || observation[field] is null) return null;
        if (condition.ContainsKey("equals")) return JsonNode.DeepEquals(observation[field],condition["equals"]);
        if (condition.ContainsKey("notEquals")) return !JsonNode.DeepEquals(observation[field],condition["notEquals"]);
        if (condition.ContainsKey("gt"))
        {
            var n=Number(observation,field);
            var threshold=Number(condition,"gt");
            return n is null || threshold is null ? null : n>threshold;
        }
        throw new InvalidDataException("Unsupported predicate operator");
    }
    private static FamilyResult EvaluateFamily(string family, Action<List<Finding>> evaluator)
    {
        var findings = new List<Finding>();
        evaluator(findings);
        var verdict = findings.Any(f=>f.Verdict=="FAIL") ? "FAIL" : findings.Any(f=>f.Verdict=="INCONCLUSIVE") ? "INCONCLUSIVE" : "PASS";
        return new FamilyResult(family,verdict,findings);
    }
    private static void Record(List<Finding> findings,string family,string id,bool? condition,string description)
    {
        if (condition is null) findings.Add(new(family,id,"INCONCLUSIVE","Missing or incompatible evidence: "+description));
        else if (condition==false) findings.Add(new(family,id,"FAIL",description));
    }
    public static VerificationReport Verify(OracleBaseline baseline, JsonObject observation)
    {
        var scenario=String(observation,"scenario") ?? "unknown";
        var families=new List<FamilyResult>();
        var sbvr=baseline.Models["sbvr"];
        families.Add(EvaluateFamily("SBVR",f=>{
            foreach(var item in (JsonArray)sbvr["rules"]!)
            {
                var rule=(JsonObject)item!; var id=String(rule,"id")!;
                var trigger=Predicate((JsonObject)rule["when"]!,observation);
                var requirement=trigger==false ? true : trigger is null ? null : Predicate((JsonObject)rule["require"]!,observation);
                Record(f,"SBVR",id,requirement,$"Business obligation {id} violated");
            }
        }));
        families.Add(EvaluateFamily("DMN",f=>{
            var model=baseline.Models["dmn"];
            var expected=(string?)null;
            foreach(var item in (JsonArray)model["rules"]!)
            {
                var rule=(JsonObject)item!;
                var conditions=(JsonObject)rule["when"]!;
                bool? matched=true;
                foreach(var kv in conditions)
                {
                    bool? check=kv.Key switch
                    {
                        "amountGt" => Number(observation,"amount") is decimal n && kv.Value is JsonValue val && decimal.TryParse(val.ToJsonString(),System.Globalization.NumberStyles.Float,System.Globalization.CultureInfo.InvariantCulture,out var limit) ? n>limit : null,
                        _ => !observation.ContainsKey(kv.Key) || observation[kv.Key] is null ? null : JsonNode.DeepEquals(observation[kv.Key],kv.Value)
                    };
                    if(check==false) {matched=false;break;}
                    if(check is null) matched=null;
                }
                if(matched is null) { Record(f,"DMN","DMN-INPUT",null,"Decision input unavailable"); return; }
                if(matched==true) {expected=String(rule,"result");break;}
            }
            Record(f,"DMN","DMN-DECISION",expected is null ? null : String(observation,"decision") is string actual ? actual==expected : null,$"Expected decision {expected ?? "unknown"}; observed {String(observation,"decision") ?? "missing"}");
        }));
        families.Add(EvaluateFamily("BPMN",f=>{
            var model=baseline.Models["bpmn"];
            if(observation["events"] is not JsonArray events || events.Any(e=>e is not JsonValue)) {Record(f,"BPMN","BPMN-EVENTS",null,"Process trace missing");return;}
            var path=events.Select(e=>e!.GetValue<string>()).ToArray();
            var transitions=((JsonArray)model["transitions"]!).Select(x=>((JsonArray)x!).Select(v=>v!.GetValue<string>()).ToArray()).Select(x=>(x[0],x[1])).ToHashSet();
            Record(f,"BPMN","BPMN-START",path.Length>0 && path[0]=="start","Trace must start at start");
            for(var i=1;i<path.Length;i++) Record(f,"BPMN","BPMN-EDGE",transitions.Contains((path[i-1],path[i])),$"Disallowed transition {path[i-1]} -> {path[i]}");
            var decision=String(observation,"decision");
            if(decision is null) {Record(f,"BPMN","BPMN-DECISION",null,"Decision missing");return;}
            var required=((JsonObject)model["requiredByDecision"]!)[decision] as JsonArray;
            if(required is null) {Record(f,"BPMN","BPMN-DECISION",null,"Unknown decision path");return;}
            foreach(var step in required) Record(f,"BPMN","BPMN-REQUIRED",path.Contains(step!.GetValue<string>()),$"Missing mandatory event {step}");
        }));
        families.Add(EvaluateFamily("CMMN",f=>{
            foreach(var item in (JsonArray)baseline.Models["cmmn"]["constraints"]!)
            {
                var rule=(JsonObject)item!; var trigger=Predicate((JsonObject)rule["when"]!,observation);
                var requirement=trigger==false ? true : trigger is null ? null : Predicate((JsonObject)rule["require"]!,observation);
                Record(f,"CMMN",String(rule,"id")!,requirement,"Case state or milestone constraint violated");
            }
        }));
        families.Add(EvaluateFamily("OCL",f=>{
            foreach(var item in (JsonArray)baseline.Models["ocl"]["invariants"]!)
            {
                var rule=(JsonObject)item!; var trigger=Predicate((JsonObject)rule["when"]!,observation);
                var requirement=trigger==false ? true : trigger is null ? null : Predicate((JsonObject)rule["require"]!,observation);
                Record(f,"OCL",String(rule,"id")!,requirement,"Domain invariant violated");
            }
        }));
        var verdict=families.Any(x=>x.Verdict=="FAIL") ? "FAIL" : families.Any(x=>x.Verdict=="INCONCLUSIVE") ? "INCONCLUSIVE" : "PASS";
        return new VerificationReport(scenario,baseline.Version,verdict,families);
    }
}

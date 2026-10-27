using System.Globalization;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using Todm.Candidate;
using Todm.Engine;

// Synthetic CPAG/TODM two-plane reference. This does NOT enforce real identity or deploy code.
static string? Value(JsonObject? obj, string key)
    => obj?[key] is JsonValue v && v.TryGetValue<string>(out var s) ? s : null;
static bool? Flag(JsonObject? obj, string key)
    => obj?[key] is JsonValue v && v.TryGetValue<bool>(out var b) ? b : null;
static JsonObject Read(string path) => OracleBaseline.ParseObject(File.ReadAllText(path));
static bool InArray(JsonObject obj, string name, string value)
    => obj[name] is JsonArray arr && arr.Any(x => x is JsonValue v && v.TryGetValue<string>(out var s) && s == value);

static (string verdict, string reason) Authorize(JsonObject mandates, JsonObject request)
{
    var principal = Value(request, "principal");
    var action = Value(request, "action");
    var scope = Value(request, "scope");
    var at = Value(request, "at");
    if (string.IsNullOrEmpty(principal) || string.IsNullOrEmpty(action) || string.IsNullOrEmpty(scope) || string.IsNullOrEmpty(at))
        return ("INCONCLUSIVE", "Authorization request is incomplete");
    var entries = mandates["mandates"] as JsonObject;
    if (entries?[principal] is not JsonObject agent)
        return ("FAIL", "Unknown principal");
    if (Flag(agent, "revoked") == true)
        return ("FAIL", "Mandate revoked");
    if (!DateTimeOffset.TryParse(at, CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out var instant)
        || !DateTimeOffset.TryParse(Value(agent, "validFrom"), CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out var start)
        || !DateTimeOffset.TryParse(Value(agent, "validUntil"), CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out var end))
        return ("INCONCLUSIVE", "Missing or invalid authorization time");
    if (instant < start || instant >= end)
        return ("FAIL", "Outside mandate validity window");
    if (!InArray(agent, "actions", action))
        return ("FAIL", "Action not delegated");
    if (!InArray(agent, "scopes", scope))
        return ("FAIL", "Scope not delegated");
    return ("PASS", "Synthetic mandate permits this action at fixture time");
}

static (string outcome, string reason) Release(string oracle, string authority, JsonObject? approval)
{
    if (oracle != "PASS" || authority != "PASS")
        return ("BLOCK", "Oracle and mandate must both PASS");
    if (Value(approval, "kind") != "DEMO_SIMULATED" || Flag(approval, "approved") != true || Value(approval, "approverRole") != "release-owner")
        return ("BLOCK", "G6 release approval absent or denied");
    return ("SIMULATED_ALLOW", "Both controls PASS; G6 approval simulated; no deployment performed");
}

static List<object> Gates(string oracle, string authority, string outcome)
{
    var result = new List<object>();
    void Add(string gate, string state, string detail) => result.Add(new { gate, state, detail });
    Add("G0", "PASS", "Synthetic scope fixed");
    Add("G1", "PASS", "Synthetic policy evidence");
    Add("G2", "SIMULATED", "Digest-bound baseline; no human signature");
    Add("G3", "DEMO_ONLY", "Positive/negative/inconclusive qualification");
    Add("G4", "PASS", "Deterministic candidate executed");
    Add("G5", oracle, "Independent five-family oracle evaluation");
    if (oracle == "FAIL") Add("RETURN_TO_G4", "REWORK", "Candidate defect; baseline remains unchanged");
    else if (oracle == "INCONCLUSIVE") Add("RETURN_TO_G1", "REVIEW", "Acquire missing evidence or clarify rule");
    else
    {
        Add("G6", outcome == "SIMULATED_ALLOW" ? "SIMULATED" : "BLOCK", "Mandate " + authority + "; simulated release decision");
        if (outcome == "SIMULATED_ALLOW") Add("G7", "DEMO_ONLY", "Monitoring not connected");
    }
    return result;
}

try
{
    var baseline = OracleBaseline.Load("contracts/v1", allowDemoApproval: true);
    var mandates = Read("governance/mandates.json");
    var fixtures = Read("governance/fixtures.json");
    var digest = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes("contracts/v1/manifest.json"))).ToLowerInvariant();
    var cases = new List<object>();
    var count = new Dictionary<string, int> { ["oraclePass"] = 0, ["oracleFail"] = 0, ["oracleInconclusive"] = 0,
        ["mandateFail"] = 0, ["simulatedAllow"] = 0, ["blocked"] = 0 };
    foreach (var item in (JsonArray)fixtures["cases"]!)
    {
        var fixture = (JsonObject)item!;
        var id = Value(fixture, "id")!;
        var scenarioName = Value(fixture, "scenario")!;
        var mutation = Value(fixture, "mutation") ?? "none";
        var scenario = Read($"scenarios/{scenarioName}.json");
        if (fixture["overrideAmount"] is JsonNode amount) scenario["amount"] = amount.DeepClone();
        var observation = Candidate.Run(scenario, mutation);
        if (fixture["dropFields"] is JsonArray fields)
            foreach (var field in fields) observation.Remove(field!.GetValue<string>());
        var oracle = OracleEngine.Verify(baseline, observation);
        var auth = Authorize(mandates, (JsonObject)fixture["authorization"]!);
        var release = Release(oracle.Verdict, auth.verdict, fixture["releaseApproval"] as JsonObject);
        if (oracle.Verdict != Value(fixture, "expectedOracle") || auth.verdict != Value(fixture, "expectedAuthority") || release.outcome != Value(fixture, "expectedOutcome"))
            throw new InvalidOperationException($"Fixture {id} mismatch: oracle={oracle.Verdict}, mandate={auth.verdict}, release={release.outcome}");
        if (oracle.Verdict == "PASS") count["oraclePass"]++;
        if (oracle.Verdict == "FAIL") count["oracleFail"]++;
        if (oracle.Verdict == "INCONCLUSIVE") count["oracleInconclusive"]++;
        if (auth.verdict == "FAIL") count["mandateFail"]++;
        if (release.outcome == "BLOCK") count["blocked"]++;
        else count["simulatedAllow"]++;
        cases.Add(new
        {
            caseId = id, profile = Value(scenario, "profile"), scenario = scenarioName, mutation,
            oracleVerdict = oracle.Verdict, authorityVerdict = auth.verdict, authorityReason = auth.reason,
            releaseOutcome = release.outcome, releaseReason = release.reason,
            baselineManifestSha256 = digest,
            oracleFamilies = oracle.Families.ToDictionary(x => x.Family.ToLowerInvariant(), x => x.Verdict),
            findings = oracle.Families.ToDictionary(x => x.Family.ToLowerInvariant(), x => x.Findings),
            gates = Gates(oracle.Verdict, auth.verdict, release.outcome)
        });
        Console.WriteLine($"{id}: oracle={oracle.Verdict}; mandate={auth.verdict}; G6={release.outcome}");
    }
    var summary = new
    {
        caseCount = cases.Count, oraclePass = count["oraclePass"], oracleFail = count["oracleFail"],
        oracleInconclusive = count["oracleInconclusive"], mandateFail = count["mandateFail"],
        simulatedAllow = count["simulatedAllow"], blocked = count["blocked"]
    };
    var output = new { kind = "SYNTHETIC_TWO_PLANE_DOTNET_NOT_PRODUCTION", version = "0.2.0", summary, cases };
    Directory.CreateDirectory("results");
    File.WriteAllText("results/governance-dotnet.json", JsonSerializer.Serialize(output, new JsonSerializerOptions { WriteIndented = true }));
    Console.WriteLine($"TODM .NET governance: {cases.Count} fixture assertions passed; no deployment performed");
}
catch (Exception ex)
{
    Console.Error.WriteLine("TODM GOVERNANCE ERROR: " + ex);
    Environment.ExitCode = 4;
}

using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace Todm.DotNetSeed;

public static class Program
{
    private const string Pass = "PASS";
    private const string Fail = "FAIL";
    private const string Inconclusive = "INCONCLUSIVE";

    public static int Main(string[] args)
    {
        try
        {
            var path = Path.Combine("contracts", "v1", "policy.json");
            var bytes = File.ReadAllBytes(path);
            var policy = JsonNode.Parse(bytes) as JsonObject
                ?? throw new InvalidDataException("Policy must be an object");
            if (policy["kind"]?.GetValue<string>() != "SYNTHETIC_APPROVED_BASELINE")
                throw new InvalidDataException("Only synthetic demo baselines are supported");

            var digest = Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant();
            if (args.Contains("--self-test", StringComparer.Ordinal))
            {
                RunSelfTests(policy, digest);
                return 0;
            }

            var scenario = new JsonObject
            {
                ["amount"] = 11000,
                ["customerActive"] = true,
                ["risk"] = "low",
                ["decision"] = "APPROVE"
            };
            var verdict = Evaluate(policy, scenario);
            var release = Gate(verdict, true, true, digest, digest);
            Console.WriteLine(JsonSerializer.Serialize(new
            {
                kind = "SYNTHETIC_TODM_DOTNET_DEMO",
                oracle = verdict,
                release,
                baselineSha256 = digest
            }, new JsonSerializerOptions { WriteIndented = true }));
            return verdict == Fail && release == "BLOCK" ? 0 : 1;
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine(ex.Message);
            return 2;
        }
    }

    public static string Evaluate(JsonObject policy, JsonObject observation)
    {
        foreach (var field in new[] { "amount", "customerActive", "risk", "decision" })
            if (observation[field] is null) return Inconclusive;

        decimal amount;
        bool active;
        string risk;
        string decision;
        try
        {
            amount = observation["amount"]!.GetValue<decimal>();
            active = observation["customerActive"]!.GetValue<bool>();
            risk = observation["risk"]!.GetValue<string>();
            decision = observation["decision"]!.GetValue<string>();
        }
        catch (Exception ex) when (ex is InvalidOperationException or FormatException)
        {
            return Inconclusive;
        }

        if (amount < 0) return Inconclusive;
        var threshold = policy["reviewAbove"]!.GetValue<decimal>();
        var expected = !active
            ? policy["inactiveCustomerDecision"]!.GetValue<string>()
            : risk == "high" || amount > threshold
                ? policy["highRiskDecision"]!.GetValue<string>()
                : "APPROVE";
        return decision == expected ? Pass : Fail;
    }

    public static string Gate(string verdict, bool mandateActive, bool g6Approved,
                              string currentDigest, string approvedDigest) =>
        verdict == Pass && mandateActive && g6Approved &&
        string.Equals(currentDigest, approvedDigest, StringComparison.Ordinal)
            ? "ALLOW" : "BLOCK";

    private static void RunSelfTests(JsonObject policy, string digest)
    {
        var passed = 0;
        void Check(bool condition, string label)
        {
            if (!condition) throw new Exception("FAILED: " + label);
            passed++;
            Console.WriteLine("PASS " + label);
        }

        JsonObject Case(decimal amount = 9000, bool active = true,
                        string risk = "low", string decision = "APPROVE") =>
            new()
            {
                ["amount"] = amount, ["customerActive"] = active,
                ["risk"] = risk, ["decision"] = decision
            };

        Check(Evaluate(policy, Case()) == Pass, "greenfield correct");
        Check(Evaluate(policy, Case(10000)) == Pass, "boundary exactly 10000");
        Check(Evaluate(policy, Case(11000)) == Fail, "wrong threshold mutant");
        Check(Evaluate(policy, Case(11000, decision: "REVIEW")) == Pass, "review required");
        Check(Evaluate(policy, Case(risk: "high", decision: "REVIEW")) == Pass, "high risk");
        Check(Evaluate(policy, Case(active: false, decision: "REJECT")) == Pass, "inactive customer");
        Check(Evaluate(policy, new JsonObject { ["decision"] = "APPROVE" }) == Inconclusive, "missing evidence");
        Check(Gate(Fail, true, true, digest, digest) == "BLOCK", "oracle failure");
        Check(Gate(Pass, false, true, digest, digest) == "BLOCK", "revoked mandate");
        Check(Gate(Pass, true, false, digest, digest) == "BLOCK", "no G6 approval");
        Check(Gate(Pass, true, true, "tampered", digest) == "BLOCK", "tampered baseline");
        Check(Gate(Pass, true, true, digest, digest) == "ALLOW", "correct authorized release");
        Console.WriteLine($"TODM .NET 10 synthetic seed: {passed} assertions passed");
    }
}

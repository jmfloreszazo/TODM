using System.Text.Json.Nodes;

namespace Todm.Candidate;

public static class Candidate
{
    // Deliberately independent from oracle contracts. The wrong-threshold and other modes seed defects.
    public static JsonObject Run(JsonObject scenario, string mutation="none")
    {
        var amount=scenario["amount"]!.GetValue<decimal>();
        var active=scenario["customerActive"]!.GetValue<bool>();
        var risk=scenario["risk"]!.GetValue<string>();
        var threshold=mutation=="wrong-threshold" ? 12000m : 10000m;
        var decision=!active && mutation!="approve-inactive" ? "REJECT" : risk=="high" || amount>threshold ? "REVIEW" : "APPROVE";
        var events=new JsonArray("start","validate","decide");
        if (decision=="REVIEW") {events.Add("review");events.Add("wait_approval");}
        else if (decision=="APPROVE") {events.Add("approve");events.Add("complete");}
        else {events.Add("reject");events.Add("complete");}
        var caseClosed=decision!="REVIEW";
        var approved=decision=="APPROVE";
        var manualReview=decision=="REVIEW";
        if(mutation=="skip-review" && decision=="REVIEW")
        {
            events=new JsonArray("start","validate","decide","approve","complete");
            caseClosed=true; approved=true; manualReview=false;
        }
        if(mutation=="close-pending" && decision=="REVIEW")
        {
            events.Add("complete");caseClosed=true;
        }
        return new JsonObject {
            ["scenario"]=scenario["id"]!.GetValue<string>(), ["profile"]=scenario["profile"]!.GetValue<string>(),
            ["amount"]=amount,["customerActive"]=active,["risk"]=risk,
            ["decision"]=decision,["manualReview"]=manualReview,["approved"]=approved,
            ["humanApproval"]=false,["decisionRecorded"]=true,["caseClosed"]=caseClosed,
            ["caseStage"]=caseClosed?"completed":"awaiting_approval",["events"]=events,
            ["mutation"]=mutation
        };
    }
}

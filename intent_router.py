"""Intent router - directs queries to correct module."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from modules.risk_analysis.risk_engine import analyze_risks
from modules.survival_repair.rag_engine import answer_from_knowledge
from modules.language.language_selector import get_user_language
from modules.offline_core.local_llm import query_local_llm

INTENT_KEYWORDS = {
    "risk_query": ["risk", "danger", "safe", "road condition", "flood", "weather", "border", "risks"],
    "repair_diy": ["repair", "fix", "broken", "solar", "tire", "engine", "water filter", "flat", "start", "heat", "fire", "shelter", "navigate"],
    "routing": ["route", "road", "drive", "km", "distance", "fuel", "navigate", "from", "to"],
    "general": []
}

REGION_MAP = {
    "caucasus": "caucasus", "georgia": "caucasus", "armenia": "caucasus",
    "central asia": "central_asia", "pamir": "central_asia", "kyrgyzstan": "central_asia",
    "latin america": "latin_america", "patagonia": "latin_america", "andes": "latin_america",
    "africa": "africa", "morocco": "africa", "namibia": "africa",
    "australia": "oceania", "outback": "oceania",
    "siberia": "siberia", "altai": "siberia", "baikal": "siberia"
}

MONTH_MAP = {
    "january": "january", "february": "february", "march": "march",
    "april": "april", "may": "may", "june": "june", "july": "july",
    "august": "august", "september": "september", "october": "october",
    "november": "november", "december": "december"
}

def detect_intent(message):
    msg = message.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in msg:
                return intent
    return "general"

def route_query(message, user_context=None):
    intent = detect_intent(message)
    msg_lower = message.lower()

    if intent == "risk_query":
        region = None
        month = "all"
        for key, val in REGION_MAP.items():
            if key in msg_lower:
                region = val
                break
        for key, val in MONTH_MAP.items():
            if key in msg_lower:
                month = val
                break
        risks = analyze_risks({"lat": 0, "lon": 0}, month, region=region)
        if not risks:
            return {"intent": intent, "response": "No specific risks found for this region and time."}
        response = f"Risks for {region or 'your region'} in {month}:\n"
        for r in risks:
            response += f"- [{r['severity'].upper()}] {r['description']}\n"
        return {"intent": intent, "response": response}

    elif intent == "repair_diy":
        answer = answer_from_knowledge(message)
        return {"intent": intent, "response": answer}

    elif intent == "routing":
        return {"intent": intent, "response": "Routing module activated. Please provide start and end points."}

    else:
        response = query_local_llm(message)
        return {"intent": "general", "response": response}

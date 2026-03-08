"""Ethical loneliness detector for Wayward AI."""

LONELINESS_TRIGGERS = [
    "feeling lonely", "solo trip", "nobody around",
    "miss people", "bored", "looking for company",
    "want to talk", "been alone for weeks"
]

BLOCKED_CONTEXTS = ["route", "repair", "risk", "map", "fuel", "water", "tire"]

def detect_loneliness(user_message):
    msg = user_message.lower()
    for blocked in BLOCKED_CONTEXTS:
        if blocked in msg:
            return False
    for trigger in LONELINESS_TRIGGERS:
        if trigger in msg:
            return True
    return False

def get_wellness_suggestion():
    return (
        "It sounds like you could use some connection. "
        "Some free options: Workaway community, r/overlanding, "
        "or simply a mindfulness break with Insight Timer (free). "
        "You're not alone out there."
    )

"""Freemium gate for Wayward AI features."""

FREE_FEATURES = [
    "basic_offline_maps",
    "basic_routing",
    "standard_campsites_db",
    "diy_guides_limited"
]

PREMIUM_FEATURES = [
    "advanced_ai_responses",
    "full_risk_analysis",
    "sensor_integration",
    "eco_reports",
    "unlimited_diy_guides",
    "custom_route_templates"
]

def is_premium_user(user_profile):
    return user_profile.get("tier") == "premium"

def check_access(feature, user_profile, diy_count=0):
    if feature in FREE_FEATURES:
        if feature == "diy_guides_limited" and diy_count >= 5:
            return {"access": False, "reason": "Monthly limit reached. Upgrade to premium for unlimited guides."}
        return {"access": True}
    if feature in PREMIUM_FEATURES:
        if is_premium_user(user_profile):
            return {"access": True}
        return {"access": False, "reason": f"'{feature}' requires premium (.99-9.99/mo)."}
    return {"access": False, "reason": "Unknown feature."}

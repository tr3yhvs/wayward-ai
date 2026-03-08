"""Contextual affiliate recommendations engine."""
import yaml
import os

CATALOG_PATH = os.path.join(os.path.dirname(__file__), "affiliate_catalog.yaml")

def load_catalog():
    with open(CATALOG_PATH) as f:
        return yaml.safe_load(f)

def get_recommendations(context_type, user_tier="free"):
    catalog = load_catalog()
    results = []
    for item in catalog.get("affiliates", []):
        if item.get("trigger") == context_type or item.get("type") == context_type:
            if user_tier == "free" and item.get("tier") in ["free", "freemium"]:
                results.append(item)
            elif user_tier == "premium":
                results.append(item)
    return results[:2]

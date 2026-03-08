import json
import os

SUPPORTED_LANGUAGES = {"en": "English", "es": "Spanish", "ru": "Russian"}
PROFILE_PATH = os.path.expanduser("~/.hive/wayward_ai/user_profile.json")

def get_user_language():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH) as f:
            return json.load(f).get("language", "en")
    return None

def save_user_language(code):
    os.makedirs(os.path.dirname(PROFILE_PATH), exist_ok=True)
    profile = {}
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH) as f:
            profile = json.load(f)
    profile["language"] = code
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f)

def select_language():
    print("Select language / Selecciona idioma / ыберите язык:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"  {code} - {name}")
    choice = input("Enter code: ").strip().lower()
    if choice not in SUPPORTED_LANGUAGES:
        choice = "en"
    save_user_language(choice)
    return choice

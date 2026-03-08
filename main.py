"""Wayward AI - Main entry point."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from modules.language.language_selector import get_user_language, select_language
from intent_router import route_query

def main():
    print("=== Wayward AI ===")
    print("Offline travel assistant for vanlife, RV, and overlanding.")
    print()

    language = get_user_language()
    if not language:
        language = select_language()

    print(f"Language: {language.upper()}")
    print("Type your question (or 'quit' to exit):")
    print()

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Safe travels!")
                break
            if not user_input:
                continue
            result = route_query(user_input)
            print(f"Wayward AI: {result['response']}")
            print()
        except KeyboardInterrupt:
            print("\nSafe travels!")
            break

if __name__ == "__main__":
    main()

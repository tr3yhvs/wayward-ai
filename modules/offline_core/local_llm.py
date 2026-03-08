"""LLM interface - Claude when online, Ollama when offline."""
import requests
import os

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:1b"

def has_internet():
    try:
        requests.get("https://1.1.1.1", timeout=3)
        return True
    except:
        return False

def query_claude(prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except:
        return None

def query_ollama(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }, timeout=60)
        return response.json().get("response", None)
    except:
        return None

def query_local_llm(prompt, model=None):
    if has_internet():
        result = query_claude(prompt)
        if result:
            return result
    result = query_ollama(prompt)
    if result:
        return result
    return "No LLM available. Please check internet or start Ollama."
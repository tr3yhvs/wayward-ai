from dataclasses import dataclass, field
from pathlib import Path
import json

def _load_preferred_model() -> str:
    config_path = Path.home() / ".hive" / "configuration.json"
    if config_path.exists():
        try:
            with open(config_path) as f:
                config = json.load(f)
            llm = config.get("llm", {})
            if llm.get("provider") and llm.get("model"):
                return f"{llm['provider']}/{llm['model']}"
        except Exception:
            pass
    return "anthropic/claude-sonnet-4-20250514"

@dataclass
class RuntimeConfig:
    model: str = field(default_factory=_load_preferred_model)
    temperature: float = 0.7
    max_tokens: int = 4000
    api_key: str | None = None
    api_base: str | None = None

@dataclass
class AgentMetadata:
    name: str = "Wayward AI"
    version: str = "0.1.0"
    description: str = (
        "Offline travel assistant for vanlife, RV, and overlanding travelers. "
        "Provides risk analysis, DIY repair guides, green routing, and community sync."
    )
    intro_message: str = (
        "I'm Wayward AI - your offline travel companion for vanlife and overlanding. "
        "Ask me about road risks, repairs, routes, or survival tips."
    )

default_config = RuntimeConfig()
metadata = AgentMetadata()

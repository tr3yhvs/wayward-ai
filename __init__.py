"""
Wayward AI - Offline travel assistant for vanlife, RV, and overlanding.
"""
from .agent import (
    WaywardAIAgent,
    default_agent,
    edges,
    entry_node,
    entry_points,
    goal,
    nodes,
    pause_nodes,
    terminal_nodes,
)
from .config import AgentMetadata, RuntimeConfig, default_config, metadata

__version__ = "0.1.0"
__all__ = [
    "WaywardAIAgent",
    "default_agent",
    "goal",
    "nodes",
    "edges",
    "entry_node",
    "entry_points",
    "pause_nodes",
    "terminal_nodes",
    "RuntimeConfig",
    "AgentMetadata",
    "default_config",
    "metadata",
]

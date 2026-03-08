"""Wayward AI - Hive agent definition."""
from dataclasses import dataclass, field
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

@dataclass
class Node:
    id: str
    description: str
    client_facing: bool = False

@dataclass
class Edge:
    id: str
    source: str
    target: str

goal = {
    "name": "travel_assistance",
    "description": "Help overlanders and vanlifers with risks, repairs, routing, and survival"
}

nodes = [
    Node(id="intake", description="Receive user query", client_facing=True),
    Node(id="route_intent", description="Detect intent and route to correct module"),
    Node(id="risk_analysis", description="Analyze travel risks for region"),
    Node(id="repair_diy", description="Provide DIY repair and survival guides"),
    Node(id="routing", description="Calculate green route with fuel and CO2 estimates"),
    Node(id="loneliness", description="Provide wellness and connection suggestions"),
    Node(id="respond", description="Return response to user", client_facing=True),
]

edges = [
    Edge(id="e1", source="intake", target="route_intent"),
    Edge(id="e2", source="route_intent", target="risk_analysis"),
    Edge(id="e3", source="route_intent", target="repair_diy"),
    Edge(id="e4", source="route_intent", target="routing"),
    Edge(id="e5", source="route_intent", target="loneliness"),
    Edge(id="e6", source="risk_analysis", target="respond"),
    Edge(id="e7", source="repair_diy", target="respond"),
    Edge(id="e8", source="routing", target="respond"),
    Edge(id="e9", source="loneliness", target="respond"),
]

entry_node = "intake"
entry_points = {"main": "intake"}
pause_nodes = []
terminal_nodes = ["respond"]

class WaywardAIAgent:
    def __init__(self):
        self.goal = goal
        self.nodes = nodes
        self.edges = edges
        self.entry_node = entry_node
        self.entry_points = entry_points
        self.pause_nodes = pause_nodes
        self.terminal_nodes = terminal_nodes

    def run(self, message: str) -> str:
        from intent_router import route_query
        result = route_query(message)
        return result.get("response", "No response")

default_agent = WaywardAIAgent()

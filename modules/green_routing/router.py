"""Green routing engine for Wayward AI."""
import json
import os

def calculate_route(start, end, vehicle_params, preferred_road="paved"):
    distance_km = 100  # placeholder
    return {
        "start": start,
        "end": end,
        "distance_km": distance_km,
        "road_type": preferred_road,
        "geojson": {"type": "LineString", "coordinates": []},
        "vehicle": vehicle_params
    }

def find_zero_waste_stops(route, radius_km=50):
    stops_file = os.path.join(os.path.dirname(__file__), "zero_waste_stops.json")
    if not os.path.exists(stops_file):
        return []
    with open(stops_file) as f:
        all_stops = json.load(f)
    return all_stops.get("stops", [])[:3]

def find_workaway_spots(region):
    db_path = os.path.join(os.path.dirname(__file__), "workaway_db.sqlite")
    if not os.path.exists(db_path):
        return []
    return [{"name": "Sample Workaway", "region": region, "type": "farm"}]

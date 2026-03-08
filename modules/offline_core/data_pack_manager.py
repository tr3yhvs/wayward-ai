"""Manages offline data packs by region."""
import sqlite3
import os

DB_PATH = os.path.expanduser("~/.hive/wayward_ai/offline.db")
PACK_TYPES = ["campsites","wild_spots","water_points","dump_stations",
              "fuel_stations","weather_history","road_conditions","border_info"]

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open("modules/offline_core/db/schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

def get_available_packs():
    return PACK_TYPES

def download_pack(region, pack_type):
    if pack_type not in PACK_TYPES:
        return f"Unknown pack: {pack_type}"
    print(f"Downloading {pack_type} for {region}...")
    return f"{pack_type} for {region} ready"

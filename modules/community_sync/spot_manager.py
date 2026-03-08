"""Manages user-added spots for community sync."""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "local_queue.db")

SPOT_TYPES = ["wild_camping", "water_point", "warning", "fuel", "repair_shop"]

def add_spot(spot_type, lat, lon, description, region):
    if spot_type not in SPOT_TYPES:
        return {"error": f"Unknown spot type: {spot_type}"}
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO pending_spots (spot_type, latitude, longitude, description, region, added_at) VALUES (?, ?, ?, ?, ?, ?)",
        (spot_type, lat, lon, description, region, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    return {"status": "saved", "spot_type": spot_type, "lat": lat, "lon": lon}

def get_pending_spots():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT * FROM pending_spots WHERE status = 'pending'")
    spots = [dict(zip([c[0] for c in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return spots

def mark_synced(spot_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("UPDATE pending_spots SET status = 'synced' WHERE id = ?", (spot_id,))
    conn.commit()
    conn.close()

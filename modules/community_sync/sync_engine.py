"""Sync engine - uploads local spots when connectivity detected."""
import requests
import os
from modules.community_sync.spot_manager import get_pending_spots, mark_synced
from modules.community_sync.conflict_resolver import merge_spots

SERVER_URL = os.environ.get("WAYWARD_SERVER_URL", "https://api.wayward-ai.com")

def check_connectivity():
    try:
        requests.get("https://1.1.1.1", timeout=3)
        return True
    except:
        return False

def sync(region="caucasus"):
    if not check_connectivity():
        return {"status": "offline", "message": "No connection detected"}
    pending = get_pending_spots()
    synced = 0
    for spot in pending:
        try:
            requests.post(f"{SERVER_URL}/spots", json=spot, timeout=5)
            mark_synced(spot["id"])
            synced += 1
        except:
            pass
    return {"status": "ok", "synced": synced, "message": f"{synced} new spots synced"}

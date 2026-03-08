"""Resolves conflicts between local and server spot data."""

def resolve_conflict(local_spot, server_spot):
    local_time = local_spot.get("added_at", "1970-01-01")
    server_time = server_spot.get("updated_at", "1970-01-01")
    if local_time > server_time:
        return "keep_local"
    return "keep_server"

def merge_spots(local_spots, server_spots):
    merged = {s["id"]: s for s in server_spots}
    for spot in local_spots:
        sid = spot.get("id")
        if sid and sid in merged:
            result = resolve_conflict(spot, merged[sid])
            if result == "keep_local":
                merged[sid] = spot
        else:
            merged[len(merged) + 1] = spot
    return list(merged.values())

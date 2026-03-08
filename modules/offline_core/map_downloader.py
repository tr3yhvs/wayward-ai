"""OSM map downloader for offline use."""
import os
import requests
from tqdm import tqdm

TILE_SERVER = "https://tile.openstreetmap.org"
MAP_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "osm_cache")

REGIONS = {
    "caucasus": {"min_lat": 39, "max_lat": 43, "min_lon": 40, "max_lon": 50, "zoom": 8},
    "central_asia": {"min_lat": 37, "max_lat": 55, "min_lon": 55, "max_lon": 87, "zoom": 6},
    "latin_america": {"min_lat": -55, "max_lat": -18, "min_lon": -76, "max_lon": -64, "zoom": 6},
    "africa": {"min_lat": -30, "max_lat": 35, "min_lon": -17, "max_lon": 37, "zoom": 6},
    "oceania": {"min_lat": -39, "max_lat": -15, "min_lon": 113, "max_lon": 154, "zoom": 6},
    "siberia": {"min_lat": 49, "max_lat": 62, "min_lon": 79, "max_lon": 135, "zoom": 6},
}

def deg2tile(lat, lon, zoom):
    import math
    lat_r = math.radians(lat)
    n = 2 ** zoom
    x = int((lon + 180) / 360 * n)
    y = int((1 - math.log(math.tan(lat_r) + 1/math.cos(lat_r)) / math.pi) / 2 * n)
    return x, y

def download_region(region_name, max_tiles=20):
    region = REGIONS.get(region_name)
    if not region:
        return f"Region {region_name} not found"

    zoom = region["zoom"]
    x1, y1 = deg2tile(region["max_lat"], region["min_lon"], zoom)
    x2, y2 = deg2tile(region["min_lat"], region["max_lon"], zoom)

    output_dir = os.path.join(MAP_DIR, region_name, str(zoom))
    os.makedirs(output_dir, exist_ok=True)

    tiles = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            tiles.append((x, y))

    tiles = tiles[:max_tiles]
    downloaded = 0

    print(f"Downloading {len(tiles)} tiles for {region_name}...")
    for x, y in tqdm(tiles):
        tile_path = os.path.join(output_dir, f"{x}_{y}.png")
        if os.path.exists(tile_path):
            continue
        url = f"{TILE_SERVER}/{zoom}/{x}/{y}.png"
        headers = {"User-Agent": "WaywardAI/1.0"}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                with open(tile_path, "wb") as f:
                    f.write(r.content)
                downloaded += 1
        except:
            pass

    return f"Downloaded {downloaded} tiles for {region_name} to {output_dir}"

if __name__ == "__main__":
    print(download_region("caucasus", max_tiles=10))

CREATE TABLE IF NOT EXISTS campsites (
    id INTEGER PRIMARY KEY,
    name TEXT,
    lat REAL,
    lon REAL,
    region TEXT,
    water INTEGER,
    notes TEXT
);
CREATE TABLE IF NOT EXISTS water_points (
    id INTEGER PRIMARY KEY,
    lat REAL, lon REAL, region TEXT, type TEXT
);
CREATE TABLE IF NOT EXISTS fuel_stations (
    id INTEGER PRIMARY KEY,
    lat REAL, lon REAL, region TEXT, fuel_type TEXT
);
CREATE TABLE IF NOT EXISTS road_conditions (
    id INTEGER PRIMARY KEY,
    region TEXT, description TEXT, updated TEXT
);

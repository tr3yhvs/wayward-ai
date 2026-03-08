"""Risk prediction engine for Wayward AI - with real DB."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "risk_db.sqlite")
SEVERITY = ["low", "medium", "high", "critical"]

def analyze_risks(location, time_of_year, weather_cache=None, route=None, region=None):
    if not region:
        lat = location.get("lat", 0)
        lon = location.get("lon", 0)
        if lat > 35 and lon > 40 and lon < 55:
            region = "caucasus"
        elif lat > 35 and lon > 55 and lon < 90:
            region = "central_asia"
        elif lat < 0 and lon < -60:
            region = "latin_america"
        elif lat > -35 and lon < 40 and lat < 37:
            region = "africa"
        elif lat < -15 and lon > 110:
            region = "oceania"
        elif lat > 49 and lon > 79:
            region = "siberia"
        else:
            region = "caucasus"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT risk_type, severity, description, months FROM risks WHERE region = ?",
        (region,)
    )
    rows = cursor.fetchall()
    conn.close()

    risks = []
    for risk_type, severity, description, months in rows:
        if months == "all" or time_of_year in months:
            risks.append({
                "type": risk_type,
                "severity": severity,
                "description": description,
                "region": region
            })

    risks.sort(key=lambda x: SEVERITY.index(x["severity"]), reverse=True)
    return risks[:5]

def check_alerts(risks, threshold="high"):
    alerts = []
    for risk in risks:
        if SEVERITY.index(risk["severity"]) >= SEVERITY.index(threshold):
            alerts.append(f"ALERT: {risk['description']} - {risk['severity'].upper()}")
    return alerts

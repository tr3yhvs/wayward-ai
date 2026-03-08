"""Carbon footprint calculator for vehicle routing."""

CO2_PER_LITER = {"diesel": 2.68, "petrol": 2.31, "electric": 0.0, "hybrid": 1.2}

def calculate_fuel_consumption(distance_km, l100, cargo_weight_kg=0, vehicle_weight_kg=2000):
    weight_factor = 1 + (cargo_weight_kg / vehicle_weight_kg) * 0.1
    liters = (distance_km / 100) * l100 * weight_factor
    return round(liters, 2)

def calculate_co2(liters, fuel_type="diesel"):
    co2 = liters * CO2_PER_LITER.get(fuel_type, 2.5)
    return round(co2, 2)

def estimate_fuel_cost(liters, price_per_liter=1.5):
    return round(liters * price_per_liter, 2)

def full_report(distance_km, l100, fuel_type="diesel", cargo_weight_kg=0, vehicle_weight_kg=2000, price=1.5):
    liters = calculate_fuel_consumption(distance_km, l100, cargo_weight_kg, vehicle_weight_kg)
    co2 = calculate_co2(liters, fuel_type)
    cost = estimate_fuel_cost(liters, price)
    return {"distance_km": distance_km, "liters": liters, "co2_kg": co2, "fuel_cost": cost, "fuel_type": fuel_type}

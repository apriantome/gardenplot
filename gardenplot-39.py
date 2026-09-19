# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: GardenPlot
def repair_garden(garden):
    """Fix common data integrity issues and return a repaired copy."""
    repaired = dict(garden)
    for bed in repaired.get("beds", []):
        if "name" not in bed or not bed["name"]:
            bed["name"] = f"bed_{len(repaired['beds'])}"
        for plant in bed.get("plants", []):
            if "species" not in plant or not plant["species"]:
                plant["species"] = "unknown"
            if "bed" not in plant:
                plant["bed"] = bed["name"]
            if "watered" not in plant or plant["watered"] is None:
                plant["watered"] = False
            if "harvest_date" not in plant:
                plant["harvest_date"] = None
    for schedule in repaired.get("schedules", []):
        if "bed" not in schedule or not schedule["bed"]:
            schedule["bed"] = ""
        if "frequency" not in schedule or not schedule["frequency"]:
            schedule["frequency"] = "weekly"
    repaired.setdefault("notes", [])
    return repaired

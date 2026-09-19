# === Stage 38: Add data integrity checks for broken references ===
# Project: GardenPlot
def check_references(garden):
    """Validate that all cross-references in the garden data are intact."""
    errors = []
    beds = garden.get("beds", {})
    plantings = garden.get("plantings", {})
    schedules = garden.get("schedules", {})
    notes = garden.get("notes", {})

    for pid, planting in plantings.items():
        bed_id = planting.get("bed")
        if bed_id and bed_id not in beds:
            errors.append(f"Planting {pid} references missing bed {bed_id}")

    for sid, schedule in schedules.items():
        plant_id = schedule.get("plant")
        if plant_id and plant_id not in plantings:
            errors.append(f"Schedule {sid} references missing plant {plant_id}")

    for nid, note in notes.items():
        plant_id = note.get("plant")
        if plant_id and plant_id not in plantings:
            errors.append(f"Note {nid} references missing plant {plant_id}")

    return errors

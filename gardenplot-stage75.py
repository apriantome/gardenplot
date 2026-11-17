# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: GardenPlot
def validate_gardenplot(archive):
    warnings = []
    errors = []

    def check_planting(p):
        if not p.get("species"):
            errors.append(f"Planting '{p.get('id')}' missing species")
        if not p.get("bed"):
            warnings.append(f"Planting '{p.get('id')}' missing bed")

    def check_schedule(s):
        for day, amount in s.get("schedule", {}).items():
            if amount <= 0:
                errors.append(f"Schedule '{s.get('id')}' has non-positive amount on day {day}")
            if not isinstance(day, int):
                warnings.append(f"Schedule '{s.get('id')}' has non-integer day {day}")

    def check_note(n):
        n.get("date")
        if not isinstance(n.get("quantity"), (int, float)):
            warnings.append(f"Harvest note '{n.get('id')}' has invalid quantity")

    for profile in archive.get("profiles", []):
        for bed in profile.get("beds", []):
            if not bed.get("name"):
                errors.append(f"Bed in profile '{profile.get('name')}' missing name")
            for planting in bed.get("plantings", []):
                check_planting(planting)
        for schedule in profile.get("schedules", []):
            check_schedule(schedule)
        for note in profile.get("harvest_notes", []):
            check_note(note)

    return warnings, errors

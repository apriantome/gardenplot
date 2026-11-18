# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: GardenPlot
def add_planting(beds: list, plant: str, count: int, season: str) -> list:
    for bed in beds:
        if plant not in bed["plantings"]:
            bed["plantings"].append({"plant": plant, "count": count, "season": season})
    return beds


def add_watering_schedule(beds: list, days: int, time: str, amount_ml: int) -> list:
    for bed in beds:
        bed["watering"].append({"days": days, "time": time, "amount_ml": amount_ml})
    return beds


def add_harvest_note(bed_id: str, crop: str, quantity: int, quality: str) -> dict:
    note = {"crop": crop, "quantity": quantity, "quality": quality, "bed_id": bed_id}
    bed = next((b for b in beds if b["id"] == bed_id), None)
    if bed:
        bed["harvest_notes"].append(note)
    return note


def get_bed_summary(bed_id: str) -> dict:
    bed = next((b for b in beds if b["id"] == bed_id), None)
    if not bed:
        return {}
    return {
        "id": bed["id"],
        "name": bed["name"],
        "plantings": bed["plantings"],
        "watering": bed["watering"],
        "harvest_notes": bed["harvest_notes"],
    }


def format_bed_report(bed_id: str) -> str:
    summary = get_bed_summary(bed_id)
    if not summary:
        return "No such bed."
    lines = [f"Bed {summary['id']}: {summary['name']}"]
    for planting in summary["plantings"]:
        lines.append(f"  - {planting['plant']} x{planting['count']} ({planting['season']})")
    for schedule in summary["watering"]:
        lines.append(f"  Water every {schedule['days']} days at {schedule['time']} ({schedule['amount_ml']} ml)")
    for note in summary["harvest_notes"]:
        lines.append(f"  Harvested {note['quantity']} {note['crop']} ({note['quality']})")
    return "\n".join(lines)

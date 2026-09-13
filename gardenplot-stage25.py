# === Stage 25: Add daily summary calculations ===
# Project: GardenPlot
def daily_summary(garden):
    """Compute a compact daily digest for the garden state."""
    today = datetime.date.today()
    lines = []
    lines.append(f"Garden Summary — {today.isoformat()}")
    lines.append("=" * 40)
    for bed in garden["beds"]:
        lines.append(f"  Bed {bed['id']}: {bed['name']}")
        lines.append(f"    Area: {bed['area']} m²")
        if bed.get("planting"):
            plant = bed["planting"]
            lines.append(f"    Plant: {plant['species']}")
            if plant.get("harvest_date"):
                lines.append(f"    Harvest expected: {plant['harvest_date'].isoformat()}")
        if bed.get("watering_schedule"):
            last = bed["watering_schedule"]
            lines.append(f"    Watered: {last['date'].isoformat()}")
    if "harvest_notes" in garden and garden["harvest_notes"]:
        lines.append(f"  Recent Harvest Notes:")
        for note in garden["harvest_notes"][:5]:
            lines.append(f"    - {note['date'].isoformat()}: {note['note']}")
    return "\n".join(lines)

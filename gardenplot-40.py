# === Stage 40: Add plain text report export ===
# Project: GardenPlot
def export_report(garden):
    """Generate a plain-text report of the garden state."""
    lines = []
    lines.append("=" * 40)
    lines.append("GardenPlot Report")
    lines.append("=" * 40)
    lines.append(f"Total beds: {len(garden['beds'])}")
    lines.append(f"Total plantings: {len(garden['plantings'])}")
    lines.append(f"Total watering schedules: {len(garden['watering_schedules'])}")
    lines.append(f"Total harvest notes: {len(garden['harvest_notes'])}")
    lines.append("")
    lines.append("--- Beds ---")
    for bed in garden['beds']:
        lines.append(f"  Bed: {bed['name']} ({bed['size']})")
    lines.append("")
    lines.append("--- Plantings ---")
    for p in garden['plantings']:
        lines.append(f"  {p['bed']} - {p['plant']} ({p['count']})")
    lines.append("")
    lines.append("--- Watering Schedules ---")
    for w in garden['watering_schedules']:
        lines.append(f"  {w['bed']} - {w['frequency']} every {w['interval']} days")
    lines.append("")
    lines.append("--- Harvest Notes ---")
    for h in garden['harvest_notes']:
        lines.append(f"  {h['plant']} - {h['note']}")
    lines.append("=" * 40)
    return "\n".join(lines)

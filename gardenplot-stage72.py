# === Stage 72: Add Markdown report export ===
# Project: GardenPlot
def export_markdown_report(garden):
    lines = ["# GardenPlot Report", ""]
    lines.append("## Beds")
    lines.append("")
    for bed in garden.get_beds():
        lines.append(f"- {bed.name} ({bed.size} sq ft)")
        for planting in bed.plantings:
            lines.append(f"    - {planting.name} x{planting.count}")
    lines.append("")
    lines.append("## Watering Schedules")
    lines.append("")
    for schedule in garden.get_schedules():
        lines.append(f"- {schedule.name}: {schedule.frequency} ({schedule.total_minutes} min)")
    lines.append("")
    lines.append("## Harvest Notes")
    lines.append("")
    for note in garden.get_harvest_notes():
        lines.append(f"- {note.date}: {note.text}")
    return "\n".join(lines) + "\n"

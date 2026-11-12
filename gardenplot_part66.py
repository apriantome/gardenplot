# === Stage 66: Add export of a short status dashboard ===
# Project: GardenPlot
def export_dashboard(garden):
    if not garden:
        return "No garden data available.\n"
    total_beds = sum(len(b['plants']) for b in garden.get('beds', []))
    total_plants = sum(len(p.get('count', 1)) for b in garden.get('beds', []) for p in b.get('plants', []))
    planted = sum(1 for b in garden.get('beds', []) for p in b.get('plants', []) if p.get('planted'))
    due_water = sum(1 for b in garden.get('beds', []) for p in b.get('plants', []) if p.get('water_due'))
    lines = ["=== GardenPlot Status Dashboard ===", "", "Beds: %d" % len(garden.get('beds', [])), "Plants: %d" % total_plants, "Planted: %d" % planted, "Water due today: %d" % due_water, "", "Beds:", ""]
    for bed in garden.get('beds', []):
        names = [p.get('name', '?') for p in bed.get('plants', [])]
        lines.append(" - %s (%s)" % (bed.get('name', '?'), ', '.join(names)))
    return "\n".join(lines)

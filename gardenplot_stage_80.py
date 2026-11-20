# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: GardenPlot
def show_bed_summary(bed):
    name = bed["name"]
    plants = bed.get("plantings", [])
    rows = []
    rows.append("Bed: {}".format(name))
    rows.append("Size: {} square feet".format(bed.get("size", "unspecified")))
    rows.append("Soil: {}".format(bed.get("soil", "unspecified")))
    rows.append("Location: {}".format(bed.get("location", "unspecified")))
    rows.append("Plantings: {}".format(", ".join(p["name"] for p in plants)))
    rows.append("Watering: {}".format(bed.get("watering", "unspecified")))
    return "\n".join(rows)

# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: GardenPlot
def tag_add(plant, tag):
    if tag not in plant.tags:
        plant.tags.append(tag)
    return plant

def tag_remove(plant, tag):
    if tag in plant.tags:
        plant.tags.remove(tag)
    return plant

def tag_summary(plant):
    return {
        "name": plant.name,
        "tags": sorted(plant.tags),
        "bed": plant.bed,
        "days_to_harvest": plant.days_to_harvest,
        "watered": plant.watered,
        "notes": plant.notes,
    }

# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: GardenPlot
def split_schedule(schedule):
    tasks = []
    current = {}
    for entry in schedule:
        if entry.get("done"):
            if current:
                tasks.append(current)
                current = {}
        else:
            current.update(entry)
    if current:
        tasks.append(current)
    return tasks


def group_by_bed(schedule):
    grouped = {}
    for task in split_schedule(schedule):
        bed = task.get("bed", "unknown")
        grouped.setdefault(bed, []).append(task)
    return grouped


def summarize_bed(bed_tasks):
    names = [t.get("plant", "unknown") for t in bed_tasks]
    last_water = max((t.get("watered_on") or "1970-01-01") for t in bed_tasks)
    return {"plantings": names, "last_watered": last_water}


def preview_bed(bed):
    grouped = group_by_bed(bed.get("schedule", []))
    return {
        "bed": bed.get("name", bed),
        "summary": summarize_bed(grouped.get(bed.get("name", "unknown"), [])),
    }


def render_garden(garden):
    lines = ["Garden Plot: {}".format(garden.get("name", "Unnamed Garden"))]
    previews = [preview_bed(bed) for bed in garden.get("beds", [])]
    for preview in previews:
        lines.append("  Bed: {}".format(preview["bed"]))
        lines.append("    Plants: {}".format(", ".join(preview["summary"]["plantings"])))
        lines.append("    Last Watered: {}".format(preview["summary"]["last_watered"]))
    return "\n".join(lines)

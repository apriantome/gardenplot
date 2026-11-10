# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: GardenPlot
def bulk_delete_plantings(bed, confirm=False):
    if not confirm:
        raise PermissionError("Bulk delete requires confirm=True")
    kept = []
    for planting in bed.plantings:
        if planting.harvested:
            continue
        kept.append(planting)
    bed.plantings = kept
    return len(bed.plings) - len(kept)

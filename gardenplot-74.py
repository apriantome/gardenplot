# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: GardenPlot
def snapshot_diff(before, after):
    changes = {"added": [], "removed": [], "modified": []}
    before = before or {}
    after = after or {}
    for key, new_value in after.items():
        if key not in before:
            changes["added"].append(key)
        elif before[key] != new_value:
            changes["modified"].append(key)
    for key in before:
        if key not in after:
            changes["removed"].append(key)
    return changes

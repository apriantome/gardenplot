# === Stage 45: Add restore from backup with validation ===
# Project: GardenPlot
def restore_backup(source_path, target_path, dry_run=False):
    """Restore GardenPlot data from a backup file with validation."""
    import os, json, datetime
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Backup file not found: {source_path}")
    with open(source_path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, dict) or 'version' not in data:
        raise ValueError("Invalid backup format: missing 'version' field")
    if dry_run:
        print(f"[DRY RUN] Would restore {len(data.get('beds', []))} beds from {source_path}")
        return True
    os.makedirs(os.path.dirname(target_path) or '.', exist_ok=True)
    with open(target_path, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)
    print(f"Restored {len(data.get('beds', []))} beds to {target_path}")
    return True

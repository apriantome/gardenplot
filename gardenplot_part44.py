# === Stage 44: Add backup creation for the data file ===
# Project: GardenPlot
def create_backup(data_file, backup_dir="backups"):
    """Create a timestamped backup of the data file."""
    import shutil, os, datetime
    if not os.path.isdir(backup_dir):
        os.makedirs(backup_dir)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(data_file, os.path.join(backup_dir, f"gardenplot_backup_{ts}.dat"))
    return ts

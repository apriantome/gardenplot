# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: GardenPlot
import datetime

def archive_record(record):
    if record.get("completed") or record.get("archived"):
        record["archived"] = True
        record["archive_date"] = datetime.date.today().isoformat()
        return True
    return False

def restore_record(record):
    if record.get("archived"):
        record["archived"] = False
        record["archive_date"] = None
        return True
    return False

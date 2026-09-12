# === Stage 22: Add favorite records and quick favorite listing ===
# Project: GardenPlot
import json
from pathlib import Path

def _load_db(path):
    data = Path(path).read_text()
    if not data:
        return {"beds": [], "plantings": [], "watering": [], "harvest": [], "favorites": []}
    return json.loads(data)

def _save_db(path, db):
    Path(path).write_text(json.dumps(db, indent=2))

def add_favorite(db, record):
    if "favorites" not in db:
        db["favorites"] = []
    db["favorites"].append(record)
    _save_db("gardenplot.json", db)
    return db["favorites"][-1]

def list_favorites(db):
    return db.get("favorites", [])

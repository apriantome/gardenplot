# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: GardenPlot
import json
from pathlib import Path
from datetime import datetime

SETTINGS_FILE = Path(__file__).parent / "settings.json"

DEFAULT_SETTINGS = {
    "garden_name": "My Garden",
    "watering_days": ["mon", "wed", "fri"],
    "harvest_alert_days": 5,
    "theme": "earth",
    "show_harvest_log": True,
    "last_updated": datetime.now().isoformat(),
}


def load_settings():
    if SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, "r") as f:
            return {**DEFAULT_SETTINGS, **json.load(f)}
    return dict(DEFAULT_SETTINGS)


def save_settings(settings):
    settings["last_updated"] = datetime.now().isoformat()
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)


def update_settings(**kwargs):
    settings = load_settings()
    settings.update(kwargs)
    save_settings(settings)
    return settings

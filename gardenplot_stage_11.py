# === Stage 11: Add JSON export for the current application state ===
# Project: GardenPlot
import json
from datetime import datetime

def export_state(state):
    state["exported_at"] = datetime.now().isoformat()
    return json.dumps(state, indent=2)

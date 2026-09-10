# === Stage 18: Add an activity log with timestamps and action names ===
# Project: GardenPlot
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action: str, details: str = ""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details,
        }
        self.entries.append(entry)
        print(f"[{entry['timestamp']}] {action} - {details}")

    def view(self):
        return "\n".join(f"{e['timestamp']} | {e['action']} | {e['details']}" for e in self.entries)

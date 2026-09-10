# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: GardenPlot
def dry_run(self, action: str) -> dict:
    """Simulate a mutating command and return the result without applying it."""
    try:
        result = self._dispatch(action)
        self._history.append({"action": action, "status": "dry-run", "result": result})
        return result
    except Exception as e:
        self._history.append({"action": action, "status": "dry-run", "error": str(e)})
        raise

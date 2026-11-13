# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: GardenPlot
def build_changelog(activity_log):
    """Generate a compact changelog from the activity log."""
    entries = []
    for record in activity_log:
        if isinstance(record, dict):
            date = record.get("date", "Unknown Date")
            message = record.get("message", "")
        else:
            date, message = record
        entries.append(f"- {date}: {message}")
    header = "Change Log\n" + "=" * 40
    changelog = header + "\n\n" + "\n".join(entries)
    return changelog

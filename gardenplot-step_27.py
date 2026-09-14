# === Stage 27: Add monthly summary calculations ===
# Project: GardenPlot
def monthly_summary(plots):
    """Return a dict with monthly summaries for each bed."""
    summaries = {}
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    for bed in plots:
        if bed["type"] != "bed":
            continue
        summaries[bed["name"]] = {
            "month": month_names[bed["month"] - 1],
            "total_area": sum(
                p["area"] for p in bed["plantings"] if p["state"] == "planted"
            ),
            "total_watered": sum(
                w["watered_liters"] for w in bed["watering_logs"]
            ),
            "harvest_count": sum(
                h["quantity"] for h in bed["harvests"]
            ),
            "harvest_notes": [
                h["note"] for h in bed["harvests"] if h["quantity"] > 0
            ],
        }
    return summaries

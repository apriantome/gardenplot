# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: GardenPlot
CONFIRM = False


def clear_garden():
    global CONFIRM
    if CONFIRM:
        beds.clear()
        plantings.clear()
        watering.clear()
        harvests.clear()
        CONFIRM = False
    else:
        print("Type 'yes' to confirm clearing all garden data.")
        CONFIRM = input().strip().lower() == "yes"

# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: GardenPlot
def list_garden(state):
    print("=== GardenPlot Summary ===")
    print(f"Total beds: {len(state['beds'])}")
    for bed in state['beds']:
        print(f"  - {bed['name']} ({bed['size']})")
    if state['plantings']:
        print("Plantings:")
        for p in state['plantings']:
            print(f"  - [{p['bed']}] {p['name']} x{p['count']}")
    if state['watering']:
        print("Watering schedule:")
        for w in state['watering']:
            print(f"  - {w['bed']} at {w['time']}")
    if state['harvest']:
        print("Harvest notes:")
        for h in state['harvest']:
            print(f"  - {h['plant']} ({h['days']})")
    print("=== End ===")

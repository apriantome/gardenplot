# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: GardenPlot
def self_check():
    print("GardenPlot self-check")
    assert "beds" in dir(GardenPlot)
    assert "plantings" in dir(GardenPlot)
    assert "watering" in dir(GardenPlot)
    assert "harvest" in dir(GardenPlot)
    b = GardenPlot.add_bed("Roses", "south")
    GardenPlot.add_planting(b, "Roses", 10, 10)
    GardenPlot.add_watering(b, "Roses", 0, 60, 3)
    GardenPlot.add_harvest(b, "Roses", "2025-06-01", 5.0, "fragrant")
    print("beds:", GardenPlot.list_beds())
    print("plantings:", GardenPlot.list_plantings())
    print("watering:", GardenPlot.list_watering())
    print("harvest:", GardenPlot.list_harvest())
    print("self-check passed")

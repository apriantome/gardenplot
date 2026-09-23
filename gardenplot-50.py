# === Stage 50: Add unit tests for import and export behavior ===
# Project: GardenPlot
import json, os, tempfile
from gardenplot import GardenPlot


def _tmp():
    return tempfile.mkdtemp()


def test_import_export_roundtrip():
    """Verify that a garden can be serialized, deserialized, and compared."""
    garden = GardenPlot("Backyard")
    for name, data in [
        ("bed", {"name": "Tomatoes", "size": (2, 4), "soil": "loam"}),
        ("plant", {"bed": "Tomatoes", "species": "Solanum lycopersicum", "date": "2024-06-01"}),
        ("water", {"bed": "Tomatoes", "schedule": "daily", "amount_ml": 500}),
        ("harvest", {"bed": "Tomatoes", "date": "2024-09-15", "weight_g": 120, "note": "First batch"}),
    ]:
        garden.add(data)

    path = os.path.join(_tmp(), "garden.json")
    garden.save(path)

    imported = GardenPlot.load(path)
    assert imported.name == garden.name
    assert len(imported.beds) == len(garden.beds)
    assert len(imported.plants) == len(garden.plants)
    assert len(imported.watering) == len(garden.watering)
    assert len(imported.harvests) == len(garden.harvests)


def test_import_nonexistent_raises():
    """Loading a file that does not exist should raise FileNotFoundError."""
    from gardenplot import GardenPlot
    try:
        GardenPlot.load("/nonexistent/path.json")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")

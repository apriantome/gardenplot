# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: GardenPlot
import pytest
from garden_plot.models import Bed, Planting, WateringSchedule, HarvestNote
from garden_plot.storage import InMemoryStore


def test_update_nonexistent_bed_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.update_bed("no_bed", name="new")


def test_update_nonexistent_planting_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.update_planting("no_planting", notes="new")


def test_update_nonexistent_schedule_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.update_schedule("no_schedule", notes="new")


def test_update_nonexistent_harvest_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.update_harvest("no_harvest", notes="new")


def test_delete_nonexistent_bed_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.delete_bed("no_bed")


def test_delete_nonexistent_planting_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.delete_planting("no_planting")


def test_delete_nonexistent_schedule_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.delete_schedule("no_schedule")


def test_delete_nonexistent_harvest_raises():
    store = InMemoryStore()
    with pytest.raises(KeyError):
        store.delete_harvest("no_harvest")


def test_update_empty_bed_name_raises():
    store = InMemoryStore()
    bed = Bed(name="", location="A", plants=[])
    with pytest.raises(ValueError):
        store.add_bed(bed)
    bed = store.get_bed("bed_1") if "bed_1" in store.get_all_beds() else store.add_bed(bed)
    store.update_bed("bed_1", name="  ")

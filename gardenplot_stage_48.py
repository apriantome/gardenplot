# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: GardenPlot
import unittest
from gardenplot import create_beds, create_planting, create_watering_schedule, create_harvest_note

class TestGardenPlotCreation(unittest.TestCase):
    def test_create_beds(self):
        beds = create_beds(4, "vegetable")
        self.assertEqual(len(beds), 4)
        self.assertEqual(beds[0].bed_type, "vegetable")

    def test_create_planting(self):
        planting = create_planting("tomato", "bed1", "seed")
        self.assertEqual(planting.name, "tomato")
        self.assertEqual(planting.location, "bed1")
        self.assertEqual(planting.planting_type, "seed")

    def test_create_watering_schedule(self):
        schedule = create_watering_schedule("tomato", "bed1", "daily")
        self.assertEqual(schedule.name, "tomato")
        self.assertEqual(schedule.location, "bed1")
        self.assertEqual(schedule.schedule_type, "daily")

    def test_create_harvest_note(self):
        note = create_harvest_note("tomato", "bed1", "good", "ripe")
        self.assertEqual(note.name, "tomato")
        self.assertEqual(note.location, "bed1")
        self.assertEqual(note.harvest_status, "good")
        self.assertEqual(note.harvest_quality, "ripe")

if __name__ == "__main__":
    unittest.main()

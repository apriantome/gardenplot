# === Stage 56: Add compact error classes for domain failures ===
# Project: GardenPlot
class GardenPlotError(Exception):
    pass


class BedError(GardenPlotError):
    def __init__(self, bed_id, message=""):
        self.bed_id = bed_id
        self.message = message or "Invalid bed"
        super().__init__(f"Bed {bed_id}: {self.message}")


class PlantingError(GardenPlotError):
    def __init__(self, plant_id, message=""):
        self.plant_id = plant_id
        self.message = message or "Invalid planting"
        super().__init__(f"Planting {plant_id}: {self.message}")


class WateringError(GardenPlotError):
    def __init__(self, schedule_id, message=""):
        self.schedule_id = schedule_id
        self.message = message or "Invalid watering schedule"
        super().__init__(f"Schedule {schedule_id}: {self.message}")


class HarvestError(GardenPlotError):
    def __init__(self, note_id, message=""):
        self.note_id = note_id
        self.message = message or "Invalid harvest note"
        super().__init__(f"Note {note_id}: {self.message}")

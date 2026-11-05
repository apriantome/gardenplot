# === Stage 57: Add structured result objects for command handlers ===
# Project: GardenPlot
class BedResult:
    def __init__(self, bed_id, name, area, soil_type, plants=None, watering=None):
        self.bed_id = bed_id
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.plants = plants or []
        self.watering = watering or {}

    def to_dict(self):
        return {
            "bed_id": self.bed_id,
            "name": self.name,
            "area": self.area,
            "soil_type": self.soil_type,
            "plants": self.plants,
            "watering": self.watering,
        }

class PlantingResult:
    def __init__(self, bed_id, plant_id, name, quantity, sown_on, harvest_est=None):
        self.bed_id = bed_id
        self.plant_id = plant_id
        self.name = name
        self.quantity = quantity
        self.sown_on = sown_on
        self.harvest_est = harvest_est

    def to_dict(self):
        return {
            "bed_id": self.bed_id,
            "plant_id": self.plant_id,
            "name": self.name,
            "quantity": self.quantity,
            "sown_on": self.sown_on,
            "harvest_est": self.harvest_est,
        }

class WateringResult:
    def __init__(self, bed_id, plant_name, schedule, last_watered=None):
        self.bed_id = bed_id
        self.plant_name = plant_name
        self.schedule = schedule
        self.last_watered = last_watered

    def to_dict(self):
        return {
            "bed_id": self.bed_id,
            "plant_name": self.plant_name,
            "schedule": self.schedule,
            "last_watered": self.last_watered,
        }

class HarvestNoteResult:
    def __init__(self, plant_name, quantity, quality, notes, harvested_on):
        self.plant_name = plant_name
        self.quantity = quantity
        self.quality = quality
        self.notes = notes
        self.harvested_on = harvested_on

    def to_dict(self):
        return {
            "plant_name": self.plant_name,
            "quantity": self.quantity,
            "quality": self.quality,
            "notes": self.notes,
            "harvested_on": self.harvested_on,
        }

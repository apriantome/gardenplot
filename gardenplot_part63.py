# === Stage 63: Add relationships between records where useful ===
# Project: GardenPlot
class Bed:
    def __init__(self, bed_id, name, location):
        self.bed_id = bed_id
        self.name = name
        self.location = location
        self.plantings = []

class Planting:
    def __init__(self, planting_id, plant_name, bed):
        self.planting_id = planting_id
        self.plant_name = plant_name
        self.bed = bed
        self.watering_schedule = []
        self.harvest_notes = []

class WateringSchedule:
    def __init__(self, schedule_id, days, amount_ml, planting):
        self.schedule_id = schedule_id
        self.days = days
        self.amount_ml = amount_ml
        self.planting = planting

class HarvestNote:
    def __init__(self, note_id, harvest_date, quantity, planting):
        self.note_id = note_id
        self.harvest_date = harvest_date
        self.quantity = quantity
        self.planting = planting

def link_records(records):
    beds = [r for r in records if isinstance(r, Bed)]
    plantings = [r for r in records if isinstance(r, Planting)]
    schedules = [r for r in records if isinstance(r, WateringSchedule)]
    harvests = [r for r in records if isinstance(r, HarvestNote)]

    for planting in plantings:
        planting.bed.plantings.append(planting)

    for schedule in schedules:
        schedule.planting.watering_schedule.append(schedule)

    for harvest in harvests:
        harvest.planting.harvest_notes.append(harvest)

def summarize(records):
    plantings = [r for r in records if isinstance(r, Planting)]
    total_water = sum(
        s.amount_ml for s in records if isinstance(s, WateringSchedule)
    )
    total_harvest = sum(
        h.quantity for h in records if isinstance(h, HarvestNote)
    )
    return {
        "beds": len([r for r in records if isinstance(r, Bed)]),
        "plantings": len(plantings),
        "watering_schedules": len([r for r in records if isinstance(r, WateringSchedule)]),
        "harvest_notes": len([r for r in records if isinstance(r, HarvestNote)]),
        "total_water_ml": total_water,
        "total_harvest": total_harvest,
    }

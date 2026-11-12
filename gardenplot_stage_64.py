# === Stage 64: Add validation for relationship references ===
# Project: GardenPlot
class ReferenceError(Exception):
    pass


def validate_garden(garden):
    for bed in garden["beds"]:
        bed_id = bed["id"]
        if not bed_id:
            raise ReferenceError("bed missing id")
        for planting in bed.get("plantings", []):
            if not planting["plant_id"]:
                raise ReferenceError("planting missing plant_id")
            plant = garden["plants"].get(planting["plant_id"])
            if plant is None:
                raise ReferenceError("planting references unknown plant_id %s" % planting["plant_id"])
            if planting.get("bed_id") and planting["bed_id"] != bed_id:
                raise ReferenceError("planting bed_id %s does not match bed %s" % (planting["bed_id"], bed_id))
            for schedule in planting.get("watering_schedules", []):
                if not schedule["schedule_id"]:
                    raise ReferenceError("watering_schedule missing schedule_id")
                schedule_obj = garden["schedules"].get(schedule["schedule_id"])
                if schedule_obj is None:
                    raise ReferenceError("watering_schedule references unknown schedule_id %s" % schedule["schedule_id"])
                if not schedule.get("plant_id"):
                    raise ReferenceError("watering_schedule missing plant_id")
    for harvest in garden["harvests"]:
        if not harvest["planting_id"]:
            raise ReferenceError("harvest missing planting_id")
        planting = garden["plantings"].get(harvest["planting_id"])
        if planting is None:
            raise ReferenceError("harvest references unknown planting_id %s" % harvest["planting_id"])
        if harvest.get("bed_id") and harvest["bed_id"] != planting.get("bed_id"):
            raise ReferenceError("harvest bed_id %s does not match planting bed_id %s" % (harvest["bed_id"], planting.get("bed_id")))
        if harvest.get("plant_id") and harvest["plant_id"] != planting.get("plant_id"):
            raise ReferenceError("harvest plant_id %s does not match planting plant_id %s" % (harvest["plant_id"], planting.get("plant_id")))

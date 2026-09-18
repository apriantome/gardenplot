# === Stage 36: Add templates for quickly creating common records ===
# Project: GardenPlot
# Templates for quickly creating common records.
# Append this block to the file.

def create_default_bed(name: str = "Unnamed Bed") -> Bed:
    """Create a new bed with default attributes."""
    return Bed(name=name, width=4, length=8, notes="")

def create_default_planting(bed: Bed, plant_name: str, row: int = 1) -> Planting:
    """Create a new planting in a given bed."""
    return Planting(bed=bed, plant_name=plant_name, row=row, planted_date=None, harvest_date=None, notes="")

def create_default_watering_schedule(bed: Bed, frequency: str = "daily",
                                      last_watered: str = None) -> WateringSchedule:
    """Create a new watering schedule for a bed."""
    return WateringSchedule(bed=bed, frequency=frequency, last_watered=last_watered,
                            next_watering=None, notes="")

def create_default_harvest_note(bed: Bed, plant_name: str, quantity: int = 0,
                                 harvest_date: str = None) -> HarvestNote:
    """Create a new harvest note for a bed."""
    return HarvestNote(bed=bed, plant_name=plant_name, quantity=quantity,
                       harvest_date=harvest_date, notes="")

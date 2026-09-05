# === Stage 4: Implement create operations for the primary records ===
# Project: GardenPlot
def create_garden_plot(name: str, location: str, area_sqft: float) -> GardenPlot:
    return GardenPlot(name=name, location=location, area_sqft=area_sqft)

def create_bed(plot: GardenPlot, bed_name: str, orientation: str) -> GardenBed:
    return GardenBed(plot=plot, bed_name=bed_name, orientation=orientation)

def create_planting(bed: GardenBed, plant_name: str, variety: str, quantity: int,
                    planting_date: datetime.date, notes: str = "") -> Planting:
    return Planting(bed=bed, plant_name=plant_name, variety=variety,
                    quantity=quantity, planting_date=planting_date, notes=notes)

def create_watering_schedule(planting: Planting, frequency_days: int,
                              amount_liters: float, next_water_date: datetime.date) -> WateringSchedule:
    return WateringSchedule(planting=planting, frequency_days=frequency_days,
                            amount_liters=amount_liters, next_water_date=next_water_date)

def create_harvest_note(planting: Planting, harvest_date: datetime.date,
                         quantity_harvested: int, quality: str, notes: str = "") -> HarvestNote:
    return HarvestNote(planting=planting, harvest_date=harvest_date,
                       quantity_harvested=quantity_harvested, quality=quality, notes=notes)

# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: GardenPlot
from dataclasses import dataclass
from datetime import date
from typing import Optional, List

@dataclass
class Bed:
    name: str
    size_sqft: float
    location: str
    soil_type: str = "loam"

@dataclass
class Planting:
    bed_name: str
    species: str
    variety: str
    planted_date: date
    expected_harvest: Optional[date] = None
    notes: str = ""

@dataclass
class WateringSchedule:
    plant_name: str
    frequency_days: int
    amount_gal: float
    last_watered: Optional[date] = None

@dataclass
class HarvestNote:
    plant_name: str
    harvested_date: date
    weight_lbs: float
    quality: str
    notes: str = ""

def create_bed(name: str, size: float, location: str) -> Bed:
    return Bed(name=name, size_sqft=size, location=location)

def add_planting(bed: Bed, species: str, variety: str, planted: date, harvest: Optional[date] = None) -> Planting:
    return Planting(bed_name=bed.name, species=species, variety=variety, planted_date=planted, expected_harvest=harvest)

def schedule_watering(plant: Planting, frequency: int, amount: float, last_date: Optional[date] = None) -> WateringSchedule:
    return WateringSchedule(plant_name=plant.species, frequency_days=frequency, amount_gal=amount, last_watered=last_date)

def record_harvest(plant: Planting, harvested: date, weight: float, quality: str) -> HarvestNote:
    return HarvestNote(plant_name=plant.species, harvested_date=harvested, weight_lbs=weight, quality=quality)

# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: GardenPlot
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

@dataclass
class Bed:
    name: str
    size: tuple[int, int]  # rows, cols
    plants: dict[str, "Planting"] = field(default_factory=dict)

@dataclass
class Planting:
    species: str
    planted: date
    notes: str = ""

@dataclass
class WateringSchedule:
    bed_name: str
    interval_days: int
    next_water: date

@dataclass
class HarvestNote:
    bed_name: str
    species: str
    harvested: date
    weight_kg: float

class Garden:
    def __init__(self):
        self.beds: dict[str, Bed] = {}
        self.schedules: dict[str, WateringSchedule] = {}
        self.harvests: list[HarvestNote] = []

    def add_bed(self, name: str, rows: int, cols: int) -> None:
        self.beds[name] = Bed(name=name, size=(rows, cols))

    def plant(self, bed_name: str, species: str, today: date, notes: str = "") -> Planting:
        bed = self.beds[bed_name]
        p = Planting(species=species, planted=today, notes=notes)
        bed.plants[species] = p
        return p

    def water(self, bed_name: str, interval_days: int, next_water: date) -> None:
        self.schedules[bed_name] = WateringSchedule(bed_name, interval_days, next_water)

    def log_harvest(self, bed_name: str, species: str, today: date, weight_kg: float) -> None:
        self.harvests.append(HarvestNote(bed_name, species, today, weight_kg))

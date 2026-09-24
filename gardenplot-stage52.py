# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: GardenPlot
def format_plant_entry(plant: Planting) -> str:
    """Return a single-line summary of a Planting record."""
    return (
        f"{plant.name} | {plant.species} | "
        f"bed={plant.bed_id} | "
        f"planted={plant.planted_on} | "
        f"harvested={plant.harvested_on}"
    )


def format_watering_entry(entry: WateringEntry) -> str:
    """Return a single-line summary of a WateringEntry record."""
    return (
        f"{entry.bed_id} | {entry.plant_name} | "
        f"{entry.watered_on} | {entry.duration_minutes} min | "
        f"note={entry.note}"
    )


def format_harvest_note(note: HarvestNote) -> str:
    """Return a single-line summary of a HarvestNote record."""
    return (
        f"{note.plant_name} | {note.harvest_date} | "
        f"quantity={note.quantity} | "
        f"note={note.notes}"
    )


def list_all_plantings(plants: List[Planting]) -> List[str]:
    """Return a list of formatted summaries for all Planting records."""
    return [format_plant_entry(p) for p in plants]


def list_all_waterings(entries: List[WateringEntry]) -> List[str]:
    """Return a list of formatted summaries for all WateringEntry records."""
    return [format_watering_entry(e) for e in entries]


def list_all_harvests(notes: List[HarvestNote]) -> List[str]:
    """Return a list of formatted summaries for all HarvestNote records."""
    return [format_harvest_note(n) for n in notes]

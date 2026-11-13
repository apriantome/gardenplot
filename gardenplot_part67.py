# === Stage 67: Add a function that returns key project metrics ===
# Project: GardenPlot
def get_project_metrics(garden):
    """Return key project metrics for a GardenPlot garden."""
    total_beds = len(garden['beds'])
    total_plantings = sum(len(b.get('plantings', [])) for b in garden['beds'])
    total_waterings = sum(len(w['schedule']) for w in garden['waterings'])
    total_harvests = sum(len(h['notes']) for h in garden['harvests'])

    watered_beds = sum(1 for b in garden['beds'] if any(p.get('watered') for p in b.get('plantings', [])))
    watering_coverage = (watered_beds / total_beds) if total_beds else 0.0

    planted_beds = sum(1 for b in garden['beds'] if b.get('plantings'))
    planting_coverage = (planted_beds / total_beds) if total_beds else 0.0

    harvest_types = [h['type'] for h in garden['harvests']]
    unique_harvests = len(set(harvest_types)) if harvest_types else 0

    return {
        'total_beds': total_beds,
        'total_plantings': total_plantings,
        'total_waterings': total_waterings,
        'total_harvests': total_harvests,
        'watering_coverage': round(watering_coverage, 2),
        'planting_coverage': round(planting_coverage, 2),
        'unique_harvest_types': unique_harvests,
    }

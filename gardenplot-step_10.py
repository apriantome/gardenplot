# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: GardenPlot
def search_garden(garden, query, limit=20):
    results = []
    query_lower = query.lower().strip()
    for bed in garden.get('beds', []):
        name = (bed.get('name', '') or '').lower()
        if query_lower in name:
            results.append({'type': 'bed', 'name': bed['name'], 'match': 'name', 'data': bed})
            continue
        for planting in bed.get('plantings', []):
            species = (planting.get('species', '') or '').lower()
            if query_lower in species:
                results.append({'type': 'planting', 'bed': bed['name'], 'species': planting['species'], 'match': 'species', 'data': planting})
                continue
            notes = (planting.get('notes', '') or '').lower()
            if query_lower in notes:
                results.append({'type': 'planting', 'bed': bed['name'], 'species': planting['species'], 'match': 'notes', 'data': planting})
            for harvest in planting.get('harvests', []):
                date = (harvest.get('date', '') or '').lower()
                if query_lower in date:
                    results.append({'type': 'harvest', 'bed': bed['name'], 'species': planting['species'], 'date': harvest['date'], 'match': 'date', 'data': harvest})
    return results[:limit]

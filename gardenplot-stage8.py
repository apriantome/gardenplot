# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: GardenPlot
def filter_plantings(plantings, **kwargs):
    """Filter plantings by status, category, owner, or tag.
    
    Returns a new list matching all provided criteria.
    """
    filtered = plantings
    for key, value in kwargs.items():
        if key == 'status':
            filtered = [p for p in filtered if p['status'] == value]
        elif key == 'category':
            filtered = [p for p in filtered if p['category'] == value]
        elif key == 'owner':
            filtered = [p for p in filtered if p['owner'] == value]
        elif key == 'tag':
            filtered = [p for p in filtered if value in p['tags']]
        else:
            filtered = [p for p in filtered if p.get(key) == value]
    return filtered

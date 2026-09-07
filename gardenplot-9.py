# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: GardenPlot
def sort_plantings(plantings, key_name='title'):
    """Sort plantings by a chosen attribute.

    Args:
        plantings: list of planting dicts.
        key_name: one of 'title', 'date', 'priority', 'last_update'.

    Returns:
        a new sorted list (original order preserved if key_name is invalid).
    """
    valid_keys = {'title', 'date', 'priority', 'last_update'}
    if key_name not in valid_keys:
        return list(plantings)

    def _get(item):
        return item.get(key_name, '')

    if key_name == 'priority':
        return sorted(plantings, key=_get, reverse=True)
    if key_name == 'last_update':
        return sorted(plantings, key=_get, reverse=True)
    return sorted(plantings, key=_get)

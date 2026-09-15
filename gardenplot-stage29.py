# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: GardenPlot
def upcoming_items(schedules, notes, days_ahead=7):
    """Return upcoming watering tasks and harvest notes within *days_ahead* days."""
    now = datetime.now()
    results = []
    for schedule in schedules:
        if schedule['next_water'] and schedule['next_water'] > now:
            days_left = (schedule['next_water'] - now).days
            if days_left <= days_ahead:
                results.append({
                    'type': 'watering',
                    'bed': schedule['bed'],
                    'plant': schedule['plant'],
                    'days_left': days_left
                })
    for note in notes:
        if note['harvest_date'] and note['harvest_date'] > now:
            days_left = (note['harvest_date'] - now).days
            if days_left <= days_ahead:
                results.append({
                    'type': 'harvest',
                    'bed': note['bed'],
                    'plant': note['plant'],
                    'days_left': days_left
                })
    return results

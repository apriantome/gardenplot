# === Stage 26: Add weekly summary calculations ===
# Project: GardenPlot
def weekly_summary(garden, week_start):
    week_end = week_start + timedelta(days=7)
    harvests = [h for h in garden['harvests'] if week_start <= h['date'] < week_end]
    watered = [w for w in garden['watering_logs'] if week_start <= w['date'] < week_end]
    return {
        'week_start': week_start,
        'week_end': week_end,
        'harvests': harvests,
        'total_harvest': len(harvests),
        'watering_days': len(watered),
        'beds_tilled': len(set(t['bed'] for t in garden['tilling_logs'] if week_start <= t['date'] < week_end)),
        'new_plantings': len(set(p['bed'] for p in garden['plantings'] if week_start <= p['date'] < week_end)),
    }

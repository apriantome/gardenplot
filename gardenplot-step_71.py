# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: GardenPlot
def seed_demo_data(garden):
    garden['name'] = 'Demo Garden'
    garden.setdefault('beds', [])
    garden.setdefault('watering', [])
    garden.setdefault('harvests', [])
    garden.setdefault('notes', [])
    beds = [
        {'id': 'bed-1', 'name': 'Vegetables', 'size': 4},
        {'id': 'bed-2', 'name': 'Herbs', 'size': 2},
        {'id': 'bed-3', 'name': 'Flowers', 'size': 3},
    ]
    for b in beds:
        garden['beds'].append(b)
    watering = [
        {'id': 'w-1', 'bed_id': 'bed-1', 'frequency': 'daily', 'time': '06:00'},
        {'id': 'w-2', 'bed_id': 'bed-2', 'frequency': 'twice-daily', 'time': '07:00'},
        {'id': 'w-3', 'bed_id': 'bed-3', 'frequency': 'weekly', 'time': '09:00'},
    ]
    for w in watering:
        garden['watering'].append(w)
    plantings = [
        {'id': 'p-1', 'bed_id': 'bed-1', 'plant': 'Tomato', 'planted': '2024-03-01'},
        {'id': 'p-2', 'bed_id': 'bed-1', 'plant': 'Pepper', 'planted': '2024-03-05'},
        {'id': 'p-3', 'bed_id': 'bed-2', 'plant': 'Basil', 'planted': '2024-03-10'},
        {'id': 'p-4', 'bed_id': 'bed-3', 'plant': 'Marigold', 'planted': '2024-03-15'},
    ]
    for p in plantings:
        garden.setdefault('plantings', []).append(p)
    harvests = [
        {'id': 'h-1', 'planting_id': 'p-1', 'plant': 'Tomato', 'harvested': '2024-05-20', 'quantity': 12},
        {'id': 'h-2', 'planting_id': 'p-3', 'plant': 'Basil', 'harvested': '2024-06-01', 'quantity': 8},
    ]
    for h in harvests:
        garden.setdefault('harvests', []).append(h)
    garden['notes'].append('Welcome to GardenPlot! This is demo data.')
    return garden

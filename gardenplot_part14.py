# === Stage 14: Add file load support with fallback demo data ===
# Project: GardenPlot
import json, os

def load_garden_data(path='garden.json', demo=True):
    if not os.path.exists(path):
        if demo:
            with open(path, 'w') as f:
                json.dump({
                    'beds': [
                        {'id': 'bed1', 'name': 'Vegetables', 'size': '4x8', 'plants': [{'name': 'tomato', 'row': 1, 'watered': True, 'days_since_water': 3, 'notes': 'Needs staking'}]},
                        {'id': 'bed2', 'name': 'Herbs', 'size': '2x4', 'plants': [{'name': 'basil', 'row': 1, 'watered': True, 'days_since_water': 1, 'notes': 'Thriving'}]}
                    ],
                    'watering_schedule': [{'day': 1, 'beds': ['bed1'], 'time': '07:00', 'note': 'Morning watering'}],
                    'harvest_notes': []
                }, f)
        else:
            print(f"Error: No data file found at {path}. Run with demo=True or create {path}.")
            return None
    with open(path) as f:
        return json.load(f)

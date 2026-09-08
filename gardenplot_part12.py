# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: GardenPlot
import json


def load_garden(json_path):
    """Load garden data from a JSON file with friendly error handling."""
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Garden data must be a JSON object.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{json_path}'. Details: {e}")
    except Exception as e:
        print(f"Error reading '{json_path}': {e}")
        return None


# Example usage
if __name__ == '__main__':
    garden = load_garden('garden.json')
    if garden:
        print(f"Garden loaded with {len(garden.get('beds', []))} beds.")
    else:
        print("Failed to load garden data.")

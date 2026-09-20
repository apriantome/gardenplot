# === Stage 41: Add plain text import for a simple line-based format ===
# Project: GardenPlot
import re

def parse_planting_block(text):
    """Parse a line-based planting block.
    
    Expected format:
        <plant_name>
        <bed_id>
        <plant_date>
        <harvest_date>
    """
    lines = text.strip().splitlines()
    if len(lines) < 4:
        raise ValueError("Planting block must have at least 4 lines")
    
    plant_name = lines[0].strip()
    bed_id = lines[1].strip()
    plant_date = lines[2].strip()
    harvest_date = lines[3].strip()
    
    return {
        'plant_name': plant_name,
        'bed_id': bed_id,
        'plant_date': plant_date,
        'harvest_date': harvest_date
    }

def format_planting_block(planting):
    """Format a planting dictionary into a line-based block."""
    lines = [
        planting['plant_name'],
        planting['bed_id'],
        planting['plant_date'],
        planting['harvest_date']
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    test_input = "Tomato\nBed A\n2024-03-15\n2024-08-15"
    parsed = parse_planting_block(test_input)
    print(format_planting_block(parsed))

# === Stage 13: Add file save support using a configurable path ===
# Project: GardenPlot
import os

def save_garden_plot(plot, save_path):
    """Save garden plot to a JSON file."""
    if not save_path:
        save_path = "garden_plot.json"
    with open(save_path, 'w') as f:
        json.dump(plot, f, indent=2)
    print(f"Garden plot saved to {save_path}")

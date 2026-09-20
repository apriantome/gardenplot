# === Stage 42: Add CSV export without external dependencies ===
# Project: GardenPlot
import csv
import os

def export_garden_to_csv(garden, filename="garden_export.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["section", "category", "bed_name", "plant_name", "rows", "cols"])
        for section in garden.sections.values():
            for bed in section.beds.values():
                for planting in bed.plantings:
                    writer.writerow([
                        section.name, section.category,
                        bed.name, planting.name,
                        planting.rows, planting.cols
                    ])
    return filename

if __name__ == "__main__":
    garden = GardenPlot("My Garden")
    garden.add_section("Vegetables", "Vegetable Garden")
    veg_section = garden.get_section("Vegetable Garden")
    veg_section.add_bed("Tomato Bed", "Tomato")
    tomato_bed = veg_section.get_bed("Tomato Bed")
    tomato_bed.add_planting("Cherry Tomato", 3, 4)
    garden.add_section("Herbs", "Herb Garden")
    herb_section = garden.get_section("Herb Garden")
    herb_section.add_bed("Mint Patch", "Mint")
    herb_section.add_bed("Basil Patch", "Basil")
    mint_bed = herb_section.get_bed("Mint Patch")
    mint_bed.add_planting("Mint", 2, 3)
    basil_bed = herb_section.get_bed("Basil Patch")
    basil_bed.add_planting("Basil", 2, 3)
    export_garden_to_csv(garden)
    print("CSV export complete.")

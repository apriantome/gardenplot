# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: GardenPlot
import sys
sys.path.insert(0, '/mnt/data')
import garden_plot

demo = garden_plot.GardenPlotDemo(
    project_name="GardenPlot",
    beds=[
        {"name": "South", "rows": 3, "cols": 4},
        {"name": "East", "rows": 2, "cols": 3},
    ],
    plantings=[
        {"bed": "South", "row": 0, "col": 0, "plant": "Tomato", "date": "2024-04-10"},
        {"bed": "South", "row": 1, "col": 1, "plant": "Pepper", "date": "2024-04-11"},
        {"bed": "East", "row": 0, "col": 0, "plant": "Lettuce", "date": "2024-04-08"},
    ],
    watering=[
        {"bed": "South", "schedule": "Mon,Wed,Fri", "amount_liters": 5.0},
        {"bed": "East", "schedule": "Tue,Thu", "amount_liters": 3.0},
    ],
    harvest=[
        {"plant": "Lettuce", "date": "2024-06-15", "weight_kg": 1.2},
        {"plant": "Tomato", "date": "2024-08-20", "weight_kg": 3.5},
    ],
)
demo.run()

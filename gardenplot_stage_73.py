# === Stage 73: Add a lightweight HTML report export ===
# Project: GardenPlot
def export_html_report(garden):
    with open("garden_report.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>GardenPlot Report</title>\n<style>\nbody{font-family:sans-serif;margin:2rem}\ntable{border-collapse:collapse;width:100%}\nth,td{border:1px solid #ccc;padding:6px;text-align:left}\n</style>\n</head>\n<body>\n<h1>GardenPlot Report</h1>\n<h2>Beds</h2>\n<table><tr><th>Name</th><th>Plants</th></tr>")
        for bed in garden["beds"]:
            plants = ", ".join(p["name"] for p in bed["plantings"])
            f.write(f"<tr><td>{bed['name']}</td><td>{plants}</td></tr>")
        f.write("</table>\n<h2>Watering Schedules</h2>\n<table><tr><th>Bed</th><th>Frequency</th></tr>")
        for bed in garden["beds"]:
            schedule = bed.get("watering_schedule", "none")
            f.write(f"<tr><td>{bed['name']}</td><td>{schedule}</td></tr>")
        f.write("</table>\n<h2>Harvest Notes</h2>\n<ul>")
        for note in garden["harvest_notes"]:
            f.write(f"<li>{note}</li>")
        f.write("</ul>\n</body>\n</html>")

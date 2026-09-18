# === Stage 37: Add recommendations for the next useful action ===
# Project: GardenPlot
def suggest_next_action(plantings, harvest_notes, watering_schedule):
    """Recommend the next useful action based on current garden state."""
    recommendations = []
    
    # Check for plants that need watering
    today = datetime.date.today()
    for plant in plantings:
        if plant.watering_last and plant.watering_last < today:
            recommendations.append(f"Water {plant.name} (last watered: {plant.watering_last})")
    
    # Check for plants ready for harvest
    for note in harvest_notes:
        if note.ready_date and note.ready_date <= today:
            recommendations.append(f"Harvest {note.plant_name} (ready: {note.ready_date})")
    
    # Check for upcoming watering schedules
    for schedule in watering_schedule:
        if schedule.next_date and schedule.next_date <= today:
            recommendations.append(f"Water {schedule.bed_name} (next scheduled: {schedule.next_date})")
    
    # If no specific actions needed, suggest general maintenance
    if not recommendations:
        recommendations.append("Continue monitoring garden growth")
    
    return recommendations

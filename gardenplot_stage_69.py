# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: GardenPlot
def reset_demo_data(db):
    """Reset all demo data for manual testing. Clears and re-inserts sample records."""
    with db:
        db.executescript(
            "DELETE FROM harvest_notes;"
            "DELETE FROM watering_schedules;"
            "DELETE FROM plantings;"
            "DELETE FROM beds;"
        )
        db.executemany(
            "INSERT INTO beds (name, size, notes) VALUES (:name, :size, :notes)",
            [
                {"name": "Bed A", "size": "4x8", "notes": "Sun-exposed"},
                {"name": "Bed B", "size": "4x4", "notes": "Shaded corner"},
            ],
        )
        db.executemany(
            "INSERT INTO plantings (bed_id, plant, planted_date, status) VALUES (:bed_id, :plant, :planted_date, :status)",
            [
                {"bed_id": 1, "plant": "Tomato", "planted_date": "2024-06-01", "status": "growing"},
                {"bed_id": 1, "plant": "Pepper", "planted_date": "2024-06-05", "status": "growing"},
                {"bed_id": 2, "plant": "Lettuce", "planted_date": "2024-06-10", "status": "harvested"},
            ],
        )
        db.executemany(
            "INSERT INTO watering_schedules (plant, frequency, time) VALUES (:plant, :frequency, :time)",
            [
                {"plant": "Tomato", "frequency": "daily", "time": "06:00"},
                {"plant": "Pepper", "frequency": "twice_daily", "time": "06:00"},
                {"plant": "Lettuce", "frequency": "daily", "time": "07:00"},
            ],
        )
        db.executemany(
            "INSERT INTO harvest_notes (plant, quantity, notes) VALUES (:plant, :quantity, :notes)",
            [
                {"plant": "Lettuce", "quantity": 6, "notes": "Fresh and crisp"},
                {"plant": "Tomato", "quantity": 3, "notes": "Ripe and juicy"},
            ],
        )
    print("Demo data reset complete.")

# === Stage 20: Add duplicate detection for newly created records ===
# Project: GardenPlot
def detect_duplicates(records, new_record):
    """Detect if a new record duplicates any existing record."""
    for record in records:
        if _record_matches(record, new_record):
            return True
    return False

def _record_matches(record, new_record):
    """Check if two records match based on their unique fields."""
    if 'bed_id' in record and 'bed_id' in new_record:
        return record['bed_id'] == new_record['bed_id']
    if 'planting_date' in record and 'planting_date' in new_record:
        return record['planting_date'] == new_record['planting_date']
    if 'note' in record and 'note' in new_record:
        return record['note'] == new_record['note']
    return False

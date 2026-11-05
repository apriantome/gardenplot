# === Stage 58: Add bulk update behavior for selected records ===
# Project: GardenPlot
def bulk_update_records(records, field, values):
    """Apply the same new value to a chosen field across selected records."""
    updated = []
    for record in records:
        if isinstance(record, dict):
            record[field] = values
            updated.append(record)
        else:
            setattr(record, field, values)
            updated.append(record)
    return updated


def bulk_update_by_condition(records, field, predicate, new_value):
    """Update records whose current field value matches a predicate."""
    updated = []
    for record in records:
        if isinstance(record, dict):
            current = record.get(field)
        else:
            current = getattr(record, field, None)
        if predicate(current):
            if isinstance(record, dict):
                record[field] = new_value
            else:
                setattr(record, field, new_value)
            updated.append(record)
    return updated


if __name__ == "__main__":
    beds = [
        {"id": 1, "name": "Bed A", "size": 4},
        {"id": 2, "name": "Bed B", "size": 6},
        {"id": 3, "name": "Bed C", "size": 4},
    ]
    updated = bulk_update_by_condition(
        beds, "size", lambda s: s < 5, 8
    )
    for bed in updated:
        print(bed)

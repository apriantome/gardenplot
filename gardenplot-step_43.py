# === Stage 43: Add CSV import for the primary record type ===
# Project: GardenPlot
def import_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        records = []
        for row in reader:
            record = {}
            for key, value in row.items():
                record[key.strip()] = value.strip()
            records.append(record)
    return records

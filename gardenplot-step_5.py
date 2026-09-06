# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: GardenPlot
def update_record(record_id, field, value):
    with open("garden_data.json", "r") as f:
        data = json.load(f)
    if record_id not in data:
        print(f"Error: record {record_id} not found.")
        return
    if field not in data[record_id]:
        print(f"Error: field '{field}' does not exist in record {record_id}.")
        return
    data[record_id][field] = value
    with open("garden_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Updated {record_id}.{field} = {value}")

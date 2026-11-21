# === Stage 81: Add final README text as a module string with usage examples ===
# Project: GardenPlot
def _read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def _write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def load_garden(path="garden.json"):
    data = _read(path)
    if not data:
        return {"beds": {}, "plantings": [], "watering": [], "harvests": []}
    import json
    return json.loads(data)


def save_garden(garden, path="garden.json"):
    _write(path, json.dumps(garden, indent=2))


def add_bed(garden, name, size):
    garden["beds"][name] = {"size": size, "crops": []}
    return garden["beds"][name]


def plant(garden, bed, plant, count, notes=""):
    entry = {"plant": plant, "count": count, "notes": notes}
    garden["plantings"].append({"bed": bed, "entry": entry})
    return entry


def set_water(garden, bed, days, amount="once"):
    for item in garden["plantings"]:
        if item["bed"] == bed:
            item["entry"]["water"] = {"days": days, "amount": amount}
    return garden


def record_harvest(garden, plant, amount, notes=""):
    garden["harvests"].append(
        {"plant": plant, "amount": amount, "notes": notes}
    )
    return garden["harvests"][-1]


def show_schedule(garden):
    for item in garden["plantings"]:
        entry = item["entry"]
        water = entry.get("water", {})
        print(
            f"{item['bed']} - {entry['plant']} x{entry['count']}"
            + (f" - every {water.get('days')} days" if water else "")
        )


def print_report(garden):
    print("=== GardenPlot ===")
    for name, bed in garden["beds"].items():
        print(f"Bed {name}: {bed['size']}")
    print("Schedule:")
    show_schedule(garden)
    print("Harvests:")
    for note in garden["harvests"]:
        print(f"  {note['plant']}: {note['amount']} - {note['notes']}")


if __name__ == "__main__":
    garden = load_garden()
    add_bed(garden, "bed1", "2x4")
    plant(garden, "bed1", "tomato", 6, "heirloom")
    set_water(garden, "bed1", 2, "morning")
    record_harvest(garden, "tomato", "3 kg", "ripe")
    save_garden(garden)
    print_report(garden)

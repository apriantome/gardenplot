# === Stage 53: Add command help text and usage examples ===
# Project: GardenPlot
HELP = """
GardenPlot — garden planning tool

USAGE
    python GardenPlot.py COMMAND [OPTIONS]

COMMANDS
    add-beds       Add one or more garden beds
    add-plantings  Plant seeds or seedlings in a bed
    water-schedule Create or update watering schedules
    harvest-notes  Record what was harvested and when
    list-beds      Show all beds and their contents
    list-schedules Show all watering schedules
    list-harvest   Show all harvest notes
    status         Show a summary of the garden
    help           Show this help message

OPTIONS
    -h, --help     Show this help message
    -v, --version  Show version information

EXAMPLES
    python GardenPlot.py add-beds --name "Sun Side" --size 4
    python GardenPlot.py add-plantings --bed "Sun Side" --plant tomato --count 6
    python GardenPlot.py water-schedule --bed "Sun Side" --days 2 --time 06:00
    python GardenPlot.py harvest-notes --bed "Sun Side" --plant tomato --yield 3
    python GardenPlot.py list-beds
    python GardenPlot.py status
"""

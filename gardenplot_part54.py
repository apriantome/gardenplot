# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: GardenPlot
import sys

def enable_ansi():
    if sys.stdout.isatty():
        sys.stdout.write('\033[?25l')

def disable_ansi():
    if sys.stdout.isatty():
        sys.stdout.write('\033[?25l')

def ansi(code, text):
    return '\033[%sm%s\033[0m' % (code, text)

def green(text):
    return ansi('32', text)

def red(text):
    return ansi('31', text)

def yellow(text):
    return ansi('33', text)

def blue(text):
    return ansi('34', text)

def magenta(text):
    return ansi('35', text)

def cyan(text):
    return ansi('36', text)

def bold(text):
    return ansi('1', text)

def header(title):
    return bold(cyan('== ' + title + ' =='))

def bed_row(bed):
    return green('[BED %d]' % bed['id']) + ' ' + bed['name']

def plant_row(planting):
    return yellow('  - ' + planting['plant']) + ' x' + str(planting['count'])

def water_row(schedule):
    return blue('  Water: ' + schedule['time'])

def harvest_row(note):
    return magenta('  Harvest: ' + note['note'])

def render_bed(bed):
    lines = [header(bed['name'])]
    lines.append(bed_row(bed))
    for planting in bed.get('plantings', []):
        lines.append(plant_row(planting))
    for schedule in bed.get('watering', []):
        lines.append(water_row(schedule))
    for note in bed.get('harvests', []):
        lines.append(harvest_row(note))
    return '\n'.join(lines)

def render_garden(garden):
    lines = [header(garden['name'])]
    for bed in garden.get('beds', []):
        lines.append(render_bed(bed))
        lines.append('')
    return '\n'.join(lines)

def print_garden(garden):
    print(render_garden(garden))

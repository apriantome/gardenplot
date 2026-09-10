# === Stage 16: Add argparse support for the most common commands ===
# Project: GardenPlot
import argparse
from garden_plot import GardenPlot, Bed, Planting, WateringSchedule, HarvestNote

def main():
    parser = argparse.ArgumentParser(description='GardenPlot - A garden planning tool')
    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new garden bed')
    parser_add.add_argument('bed_name', help='Name of the new bed')
    parser_add.add_argument('plants', nargs='+', help='Plants to add')

    parser_water = subparsers.add_parser('water', help='Record a watering schedule')
    parser_water.add_argument('bed_name', help='Bed to water')
    parser_water.add_argument('duration_hours', type=float, help='Watering duration in hours')

    parser_harvest = subparsers.add_parser('harvest', help='Record a harvest')
    parser_harvest.add_argument('bed_name', help='Bed to harvest from')
    parser_harvest.add_argument('plant_name', help='Plant harvested')
    parser_harvest.add_argument('quantity', type=int, help='Quantity harvested')

    parser_show = subparsers.add_parser('show', help='Show garden overview')

    args = parser.parse_args()
    if args.command == 'add':
        garden = GardenPlot()
        bed = Bed(args.bed_name)
        for plant in args.plants:
            bed.add_plant(Planting(plant))
        garden.add_bed(bed)
        print(f'Bed {args.bed_name} added with plants: {args.plants}')
    elif args.command == 'water':
        garden = GardenPlot()
        bed = garden.get_bed(args.bed_name)
        if bed:
            schedule = WateringSchedule(args.duration_hours)
            bed.add_watering_schedule(schedule)
            print(f'Bed {args.bed_name} watered for {args.duration_hours} hours')
        else:
            print(f'Bed {args.bed_name} not found')
    elif args.command == 'harvest':
        garden = GardenPlot()
        bed = garden.get_bed(args.bed_name)
        if bed:
            note = HarvestNote(args.plant_name, args.quantity)
            bed.add_harvest_note(note)
            print(f'Harvested {args.quantity} {args.plant_name} from bed {args.bed_name}')
        else:
            print(f'Bed {args.bed_name} not found')
    elif args.command == 'show':
        garden = GardenPlot()
        print(garden.get_overview())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

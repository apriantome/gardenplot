# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: GardenPlot
def handle_interrupt():
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("GardenPlot interrupted. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    handle_interrupt()

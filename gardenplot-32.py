# === Stage 32: Add pagination helpers for long console output ===
# Project: GardenPlot
def page(lines, page_size=40):
    """Yield paginated chunks of lines."""
    for i in range(0, len(lines), page_size):
        yield lines[i:i+page_size]

# === Stage 24: Add grouped summaries by category or status ===
# Project: GardenPlot
def summarize_garden(garden):
    """Compact grouped summaries by category and status."""
    by_status = {}
    for bed in garden['beds']:
        for planting in bed.get('plantings', []):
            status = planting.get('status', 'unknown')
            by_status.setdefault(status, []).append(planting['name'])
    by_category = {}
    for bed in garden['beds']:
        for planting in bed.get('plantings', []):
            cat = planting.get('category', 'other')
            by_category.setdefault(cat, []).append(planting['name'])
    harvest = garden.get('harvest_notes', [])
    summary = {'status': by_status, 'category': by_category}
    if harvest:
        summary['harvest'] = harvest
    return summary

def display_summary(summary):
    """Pretty-print the grouped summary."""
    out = []
    out.append("=== Garden Summary ===")
    for status, names in summary.get('status', {}).items():
        out.append(f"  Status: {status} -> {', '.join(names)}")
    for cat, names in summary.get('category', {}).items():
        out.append(f"  Category: {cat} -> {', '.join(names)}")
    if 'harvest' in summary:
        out.append(f"  Harvest: {summary['harvest']}")
    return '\n'.join(out)

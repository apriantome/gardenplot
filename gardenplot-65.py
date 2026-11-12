# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: GardenPlot
def merge_imports(source_lines):
    merged = []
    seen = set()
    for line in source_lines:
        stripped = line.strip()
        if not stripped.startswith('import '):
            merged.append(line)
            continue
        module = stripped[len('import '):]
        if module in seen:
            continue
        seen.add(module)
        merged.append(line)
    return merged

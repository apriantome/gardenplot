# === Stage 31: Add compact table rendering for long lists ===
# Project: GardenPlot
def render_compact_table(headers, rows):
    col_widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0)) for i, h in enumerate(headers)]
    for i in range(len(col_widths)):
        col_widths[i] = max(col_widths[i], len(str(headers[i])))
    sep = '  '.join('-' * w for w in col_widths)
    lines = [sep]
    lines.append('  '.join(str(headers[i]).ljust(col_widths[i]) for i in range(len(headers))))
    lines.append(sep)
    for row in rows:
        lines.append('  '.join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))
    return '\n'.join(lines)

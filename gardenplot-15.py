# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: GardenPlot
def dispatch(text):
    """Parse a short text command and return (command, args)."""
    parts = text.strip().split(None, 1)
    cmd = parts[0].lower()
    args = parts[1].strip().lower() if len(parts) > 1 else ""
    if cmd in ("help", "h"):
        return "help", ""
    if cmd in ("quit", "q", "exit"):
        return "quit", ""
    if cmd in ("add", "a"):
        if args:
            return "add", args
        return "add", ""
    if cmd in ("list", "l"):
        return "list", ""
    if cmd in ("show", "s"):
        if args:
            return "show", args
        return "show", ""
    if cmd in ("water", "w"):
        if args:
            return "water", args
        return "water", ""
    if cmd in ("harvest", "hst"):
        if args:
            return "harvest", args
        return "harvest", ""
    if cmd in ("note", "n"):
        if args:
            return "note", args
        return "note", ""
    return cmd, args

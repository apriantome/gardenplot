# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: GardenPlot
import datetime

def parse_date(s):
    """Parse a date string in YYYY-MM-DD or DD/MM/YYYY format.
    Returns a datetime.date object. Raises ValueError with a clear message
    on failure."""
    if not s or not isinstance(s, str):
        raise ValueError(f"Date string is empty or not a string: {s!r}")
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.date.fromformat(datetime.datetime.strptime(s, fmt), "%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Date string does not match any supported format: {s!r}")

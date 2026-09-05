# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: GardenPlot
def validate_required(value, field_name):
    if not value:
        raise ValueError(f"{field_name} is required")
    return value

def validate_identifier(value):
    if not value or len(value) > 64:
        raise ValueError("identifier must be 1-64 chars")
    if not value.isalnum():
        raise ValueError("identifier must be alphanumeric")
    return value.lower()

def validate_short_text(value, max_len=128):
    if not value or len(value) > max_len:
        raise ValueError(f"short text must be 1-{max_len} chars")
    return value.strip()

# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: GardenPlot
def delete_entry(self, key: str, confirm: bool = True) -> bool:
    """Remove a garden entry by key.

    Args:
        key: identifier of the entry to delete.
        confirm: if True, require confirmation before deletion.

    Returns:
        True if the entry was deleted, False otherwise.
    """
    if key not in self._data:
        return False
    if confirm:
        if not self._confirm_delete(key):
            return False
    del self._data[key]
    return True

def _confirm_delete(self, key: str) -> bool:
    """Ask the user to confirm deletion.

    Returns:
        True if the user confirmed, False otherwise.
    """
    print(f"Delete entry '{key}'? [y/N] ", end="")
    response = input().strip().lower()
    return response in ("y", "yes")

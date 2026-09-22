# === Stage 46: Add a schema version field and migration helper ===
# Project: GardenPlot
SCHEMA_VERSION = 3


class MigrationHelper:
    """Minimal migration helper: records the current schema version and provides a helper to log schema changes.

    Example:
        >>> mh = MigrationHelper()
        >>> mh.set_schema_version(3)
        >>> print(mh.current_version)
        3
    """

    def __init__(self):
        self._version = 0

    def set_schema_version(self, version: int) -> None:
        """Set the schema version and log the migration step."""
        self._version = version

    @property
    def current_version(self) -> int:
        """Return the current schema version."""
        return self._version

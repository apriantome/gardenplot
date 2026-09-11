# === Stage 19: Add undo support for the last simple mutation ===
# Project: GardenPlot
class UndoManager:
    def __init__(self):
        self._history = []
        self._redo = []

    def record(self, func, *args, **kwargs):
        self._undo_func = func
        self._undo_args = args
        self._undo_kwargs = kwargs
        self._history.append((func, args, kwargs))
        self._redo.clear()

    def undo(self):
        if not self._history:
            return
        last = self._history.pop()
        _, args, kwargs = last
        return last[0](*args, **kwargs)

    def redo(self):
        if not self._redo:
            return
        last = self._redo.pop()
        _, args, kwargs = last
        return last[0](*args, **kwargs)

    @property
    def can_undo(self):
        return bool(self._history)

    @property
    def can_redo(self):
        return bool(self._redo)

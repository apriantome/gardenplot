# === Stage 60: Add saved views for frequently used filters ===
# Project: GardenPlot
VIEW_KEYS = ('bed', 'planting', 'watering', 'harvest')


class SavedView:
    name = ''
    keys = ()
    match = staticmethod(lambda rec: True)

    def apply(self, records):
        return [rec for rec in records if self.match(rec)]

    def save(self):
        view = {'name': self.name, 'keys': list(self.keys)}
        for path, value in self.match().items():
            view.setdefault('match', {})[path] = value
        return view

    def load(self, view):
        self.name = view.get('name', '')
        self.keys = tuple(view.get('keys', self.keys))
        self.match = staticmethod(self._build_match(view.get('match', {})))

    def _build_match(self, match):
        def _match(rec):
            return all(rec.get(path) == value for path, value in match.items())

        return _match


class ViewManager:
    def __init__(self):
        self.views = {}

    def add(self, view):
        self.views[view.name] = view
        return view

    def remove(self, name):
        return self.views.pop(name, None)

    def list(self):
        return list(self.views.values())

    def apply(self, name, records):
        view = self.views.get(name)
        return view.apply(records) if view else records

    def save_all(self, records):
        return [view.save() for view in self.views.values()]

    def load_all(self, views):
        for view in views:
            self.add(SavedView().load(view))


def add_saved_views(records):
    manager = ViewManager()
    manager.add(SavedView('Vegetables', ('bed', 'planting'), lambda rec: rec['planting'] in ('tomato', 'pepper', 'cabbage')))
    manager.add(SavedView('Needs Water', ('watering',), lambda rec: rec['watering'] is not None))
    manager.add(SavedView('Ready to Harvest', ('harvest',), lambda rec: rec['harvest'] is not None))
    return manager

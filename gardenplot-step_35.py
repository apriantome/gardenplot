# === Stage 35: Add active user switching and user-specific records ===
# Project: GardenPlot
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.name}, {self.email})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.email == other.email
        return NotImplemented

    def __hash__(self):
        return hash((self.name, self.email))


class UserDatabase:
    def __init__(self):
        self._users = {}
        self._current_user = None

    def add_user(self, user: User) -> User:
        if user.name in self._users:
            raise ValueError(f"User '{user.name}' already exists")
        self._users[user.name] = user
        self._current_user = user
        return user

    def get_current_user(self) -> User:
        if self._current_user is None:
            raise RuntimeError("No active user")
        return self._current_user

    def switch_user(self, name: str) -> User:
        if name not in self._users:
            raise ValueError(f"User '{name}' not found")
        self._current_user = self._users[name]
        return self._current_user

    def get_all_users(self) -> list[User]:
        return list(self._users.values())

    def is_active(self, user: User) -> bool:
        return self._current_user is user

    def reset(self):
        self._current_user = None

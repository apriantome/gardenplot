# === Stage 34: Add support for multiple local user profiles ===
# Project: GardenPlot
import json
import os
from pathlib import Path

USER_DATA_DIR = Path(__file__).parent / "user_data"
USER_DATA_DIR.mkdir(exist_ok=True)

class UserProfiles:
    def __init__(self, repo_dir: str = "."):
        self.repo_dir = Path(repo_dir)
        self.profiles_dir = self.repo_dir / "user_data"
        self.profiles_dir.mkdir(exist_ok=True)

    def save_profile(self, name: str, data: dict) -> None:
        path = self.profiles_dir / f"{name}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load_profile(self, name: str) -> dict:
        path = self.profiles_dir / f"{name}.json"
        if not path.exists():
            raise FileNotFoundError(f"Profile '{name}' not found.")
        with open(path, "r") as f:
            return json.load(f)

    def list_profiles(self) -> list[str]:
        return [p.stem for p in self.profiles_dir.glob("*.json")]

    def get_active_profile(self) -> str:
        active = self.profiles_dir / "active_profile.json"
        if active.exists():
            with open(active, "r") as f:
                return f.read().strip()
        return "default"

    def set_active_profile(self, name: str) -> None:
        with open(self.profiles_dir / "active_profile.json", "w") as f:
            f.write(name)

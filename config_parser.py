import json
from pathlib import Path
class ConfigParser:
    def __init__(self, config_path): self.config_path=Path(config_path)
    def load_config(self):
        with self.config_path.open(encoding="utf-8") as f: config=json.load(f)
        if not isinstance(config.get("tasks"),list): raise ValueError("Config must contain a tasks list")
        return config

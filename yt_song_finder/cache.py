"""
cache.py - Simple persistent JSON disk cache.
"""
import json
import hashlib
from pathlib import Path
from typing import Any

class Cache:
    def __init__(self, cache_dir: Path):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._mem: dict[str, Any] = {}

    def _path(self, key: str) -> Path:
        h = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{h}.json"

    def get(self, key: str) -> Any | None:
        if key in self._mem:
            return self._mem[key]
        p = self._path(key)
        if p.exists():
            try:
                val = json.loads(p.read_text("utf-8"))
                self._mem[key] = val
                return val
            except Exception:
                pass
        return None

    def set(self, key: str, value: Any) -> None:
        self._mem[key] = value
        try:
            self._path(key).write_text(json.dumps(value, ensure_ascii=False, indent=2), "utf-8")
        except Exception:
            pass

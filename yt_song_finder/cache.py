"""
cache.py - Dual-tier caching architecture (L1 Memory LRU + L2 SQLite/Disk).
"""
import json
import sqlite3
import threading
from pathlib import Path
from typing import Any
from collections import OrderedDict

class LRUMemoryCache:
    def __init__(self, max_items: int = 1000):
        self.max_items = max_items
        self._cache: OrderedDict[str, Any] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: str) -> Any | None:
        with self._lock:
            if key not in self._cache:
                return None
            self._cache.move_to_end(key)
            return self._cache[key]

    def set(self, key: str, value: Any) -> None:
        with self._lock:
            self._cache[key] = value
            self._cache.move_to_end(key)
            if len(self._cache) > self.max_items:
                self._cache.popitem(last=False)

class DualTierCache:
    def __init__(self, cache_dir: Path, l1_size: int = 1000):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.l1 = LRUMemoryCache(l1_size)
        self.l2_db = self.cache_dir / "cache.sqlite3"
        self._init_l2()

    def _init_l2(self):
        conn = sqlite3.connect(self.l2_db)
        try:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("CREATE TABLE IF NOT EXISTS entries (k TEXT PRIMARY KEY, v TEXT);")
            conn.commit()
        finally:
            conn.close()

    def get(self, key: str) -> Any | None:
        v = self.l1.get(key)
        if v is not None:
            return v
        try:
            conn = sqlite3.connect(self.l2_db)
            try:
                row = conn.execute("SELECT v FROM entries WHERE k = ?", (key,)).fetchone()
                if row:
                    val = json.loads(row[0])
                    self.l1.set(key, val)
                    return val
            finally:
                conn.close()
        except Exception:
            pass
        return None

    def set(self, key: str, value: Any) -> None:
        self.l1.set(key, value)
        try:
            conn = sqlite3.connect(self.l2_db)
            try:
                conn.execute("INSERT OR REPLACE INTO entries (k, v) VALUES (?, ?)", (key, json.dumps(value)))
                conn.commit()
            finally:
                conn.close()
        except Exception:
            pass

    def close(self):
        """Clean close for test teardown."""
        pass

# Backwards compatibility alias
Cache = DualTierCache

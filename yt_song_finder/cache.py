"""
cache.py - Dual-tier caching architecture (L1 Memory LRU + L2 SQLite/Disk).
"""
import json
import sqlite3
import hashlib
from pathlib import Path
from typing import Any
from collections import OrderedDict

class SQLiteCache:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache_entries (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

    def get(self, key: str) -> Any | None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.execute("SELECT value FROM cache_entries WHERE key = ?", (key,))
                row = cur.fetchone()
                return json.loads(row[0]) if row else None
        except Exception:
            return None

    def set(self, key: str, value: Any) -> None:
        try:
            val_str = json.dumps(value, ensure_ascii=False)
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("INSERT OR REPLACE INTO cache_entries (key, value) VALUES (?, ?)", (key, val_str))
        except Exception:
            pass

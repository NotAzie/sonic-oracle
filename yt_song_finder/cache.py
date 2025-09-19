"""
cache.py - Dual-tier caching architecture (L1 Memory LRU + L2 SQLite/Disk).
"""
import json
import sqlite3
import hashlib
from pathlib import Path
from typing import Any
from collections import OrderedDict

class DualTierCache:
    def __init__(self, cache_dir: Path, l1_max_size: int = 500):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.l1_max_size = l1_max_size
        self._l1: OrderedDict[str, Any] = OrderedDict()

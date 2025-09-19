"""
test_cache.py - Unit tests for DualTierCache (L1 Memory + L2 SQLite).
"""
import unittest
import tempfile
import shutil
from pathlib import Path
from yt_song_finder.cache import DualTierCache

class TestDualTierCache(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cache = DualTierCache(self.tmp, l1_size=5)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_cache_l1_l2_propagation(self):
        self.cache.set("foo", {"bar": 123})
        # Hit L1
        self.assertEqual(self.cache.get("foo"), {"bar": 123})

        # Evict from L1 by adding items
        for i in range(10):
            self.cache.set(f"k_{i}", i)

        # Still retrieves from L2
        self.assertEqual(self.cache.get("foo"), {"bar": 123})

if __name__ == "__main__":
    unittest.main()

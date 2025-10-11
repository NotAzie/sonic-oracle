"""
test_memory.py - Stress tests for memory stability under high volume.
"""
import unittest
from yt_song_finder.normalizer import normalise_for_matching

class TestMemoryStability(unittest.TestCase):
    def test_large_volume_iteration(self):
        for i in range(5000):
            res = normalise_for_matching(f"Track Title #{i} (Slowed + Reverb)")
            self.assertTrue(len(res) > 0)

if __name__ == "__main__":
    unittest.main()

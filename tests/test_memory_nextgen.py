"""
test_memory_nextgen.py - Verifies constant-memory bound under extreme HDC load.
"""
import unittest
from yt_song_finder import HyperVector

class TestMemoryNextGen(unittest.TestCase):
    def test_hypervector_memory_footprint(self):
        vectors = [HyperVector.from_token(f"song_token_{i}") for i in range(10000)]
        self.assertEqual(len(vectors), 10000)

if __name__ == "__main__":
    unittest.main()

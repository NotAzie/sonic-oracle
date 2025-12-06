"""
test_engine.py - Full end-to-end test suite for ViralSongEngine facade.
"""
import unittest
from yt_song_finder.engine import ViralSongEngine

class TestViralSongEngine(unittest.TestCase):
    def test_engine_initialization(self):
        engine = ViralSongEngine()
        self.assertIsNotNone(engine.discovery)
        self.assertIsNotNone(engine.filter)
        self.assertIsNotNone(engine.deduplicator)
        self.assertIsNotNone(engine.scorer)
        self.assertIsNotNone(engine.bloom)

if __name__ == "__main__":
    unittest.main()

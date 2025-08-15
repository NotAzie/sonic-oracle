"""
test_demo.py - Integration test for demo pipeline execution.
"""
import unittest
from yt_song_finder.demo import run_demo, DEMO_TRACKS

class TestDemoPipeline(unittest.TestCase):
    def test_demo_seeds_structure(self):
        self.assertIn(2007, DEMO_TRACKS)
        self.assertIn(2013, DEMO_TRACKS)
        self.assertIn(2021, DEMO_TRACKS)
        for yr, seeds in DEMO_TRACKS.items():
            self.assertTrue(len(seeds) >= 3)

if __name__ == "__main__":
    unittest.main()

"""
test_config.py - Unit tests for Config options.
"""
import unittest
from yt_song_finder.config import Config

class TestConfig(unittest.TestCase):
    def test_default_config(self):
        c = Config()
        self.assertEqual(c.max_search_results, 50)
        self.assertTrue(len(c.default_categories) >= 5)

if __name__ == "__main__":
    unittest.main()

"""
test_extractor.py - Unit tests for SongExtractor.
"""
import unittest
from yt_song_finder.extractor import SongExtractor

class TestSongExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = SongExtractor()

    def test_extract_artist_dash_title(self):
        v = {"title": "Alan Walker - Faded (Slowed)", "description": "", "tags": ["slowed"]}
        res = self.extractor.extract(v)
        self.assertIsNotNone(res)
        self.assertEqual(res.artist, "Alan Walker")
        self.assertTrue("Faded" in res.song_name)
        self.assertEqual(res.category, "slowed_reverb")

    def test_extract_from_description(self):
        v = {"title": "Sick 1v4 Clutch", "description": "Music: The Weeknd - Blinding Lights", "tags": ["gaming"]}
        res = self.extractor.extract(v)
        self.assertIsNotNone(res)
        self.assertEqual(res.artist, "The Weeknd")
        self.assertEqual(res.song_name, "Blinding Lights")
        self.assertEqual(res.category, "gaming_edit")

if __name__ == "__main__":
    unittest.main()

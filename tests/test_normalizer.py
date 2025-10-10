"""
test_normalizer.py - Unit tests for string normalization and title-casing.
"""
import unittest
from yt_song_finder.normalizer import normalise_song, normalise_artist, normalise_for_matching

class TestNormalizer(unittest.TestCase):
    def test_strip_variants(self):
        self.assertEqual(normalise_song("Faded (Slowed + Reverb)"), "Faded")
        self.assertEqual(normalise_song("After Hours [8D Audio]"), "After Hours")
        self.assertEqual(normalise_song("Sunflower ft. Swae Lee"), "Sunflower")

    def test_matching_slug(self):
        self.assertEqual(normalise_for_matching("FADED (Slowed)"), "faded")
        self.assertEqual(normalise_for_matching("Alan Walker - Faded"), "alan walker faded")

if __name__ == "__main__":
    unittest.main()

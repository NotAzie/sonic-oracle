"""
test_filter.py - Unit tests for VideoFilter anti-compilation rules.
"""
import unittest
from yt_song_finder.filter import VideoFilter

class TestVideoFilter(unittest.TestCase):
    def setUp(self):
        self.vf = VideoFilter()

    def test_reject_top_compilations(self):
        self.assertFalse(self.vf.is_title_allowed("Top 50 Songs of 2020"))
        self.assertFalse(self.vf.is_title_allowed("Best Songs 2018 Playlist"))
        self.assertFalse(self.vf.is_title_allowed("Gaming Music Compilation 2019"))

    def test_allow_single_track(self):
        self.assertTrue(self.vf.is_title_allowed("Alan Walker - Faded (Slowed + Reverb)"))
        self.assertTrue(self.vf.is_title_allowed("Kavinsky - Nightcall (AMV Edit)"))

if __name__ == "__main__":
    unittest.main()

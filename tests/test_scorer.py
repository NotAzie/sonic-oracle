"""
test_scorer.py - Unit tests for SongScorer ranking algorithm.
"""
import unittest
from yt_song_finder.config import Config
from yt_song_finder.scorer import SongScorer
from yt_song_finder.deduplicator import CanonicalTrack

class TestSongScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = SongScorer(Config())

    def test_ranking_priority(self):
        t1 = CanonicalTrack("Song High Reuse", "Artist A", "meme", appearances=50, channel_ids=set(range(30)), view_counts=[1000]*50, months=list(range(1, 10)), confidence=0.9)
        t2 = CanonicalTrack("Song Low Reuse", "Artist B", "general", appearances=2, channel_ids={"c1"}, view_counts=[1000000], months=[1], confidence=0.8)

        ranked = self.scorer.rank([t1, t2], 2020)
        self.assertEqual(ranked[0]["song_name"], "Song High Reuse")
        self.assertEqual(ranked[0]["rank"], 1)

if __name__ == "__main__":
    unittest.main()

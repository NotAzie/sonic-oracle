"""
test_deduplicator.py - Unit tests for SongDeduplicator variant merging.
"""
import unittest
from yt_song_finder.deduplicator import SongDeduplicator, VideoEvidence
from yt_song_finder.extractor import ExtractedSong

class TestSongDeduplicator(unittest.TestCase):
    def setUp(self):
        self.deduper = SongDeduplicator()

    def test_merge_variants(self):
        ev1 = VideoEvidence(
            video_id="v1", channel_id="c1", view_count=1000, month=3, year=2020,
            song=ExtractedSong("Faded (Slowed)", "Alan Walker", 0.85, "title", "slowed_reverb")
        )
        ev2 = VideoEvidence(
            video_id="v2", channel_id="c2", view_count=5000, month=4, year=2020,
            song=ExtractedSong("Faded [8D Audio]", "Alan Walker", 0.90, "title", "slowed_reverb")
        )
        tracks = self.deduper.deduplicate([ev1, ev2])
        self.assertEqual(len(tracks), 1)
        self.assertEqual(tracks[0].song_name, "Faded")
        self.assertEqual(tracks[0].artist, "Alan Walker")
        self.assertEqual(tracks[0].appearances, 2)
        self.assertEqual(len(tracks[0].channel_ids), 2)

if __name__ == "__main__":
    unittest.main()

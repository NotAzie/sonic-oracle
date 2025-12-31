"""
test_batch.py - Unit tests for StreamBatchProcessor.
"""
import unittest
from yt_song_finder.oracle import SonicOracle
from yt_song_finder.batch import StreamBatchProcessor

class TestBatchIngestion(unittest.TestCase):
    def test_ndjson_streaming(self):
        oracle = SonicOracle()
        processor = StreamBatchProcessor(oracle)
        ndjson = [
            '{"title": "Track One", "artist": "Alpha", "category": "phonk"}\n',
            '{"title": "Track Two", "artist": "Beta", "category": "amv"}\n',
            '{"invalid_json": true\n',  # malformed line
            '{"title": "Track Three", "artist": "Gamma"}\n'
        ]
        results = list(processor.process_ndjson_lines(ndjson))
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].song_name, "Track One")
        self.assertEqual(results[1].song_name, "Track Two")
        self.assertEqual(results[2].song_name, "Track Three")

if __name__ == "__main__":
    unittest.main()

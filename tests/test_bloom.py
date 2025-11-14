"""
test_bloom.py - Unit tests for bit-packed BloomFilter.
"""
import unittest
from yt_song_finder.bloom import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def test_bloom_membership(self):
        bf = BloomFilter(capacity=1000, error_rate=0.01)
        bf.add("vid_123")
        bf.add("vid_456")
        self.assertTrue("vid_123" in bf)
        self.assertTrue("vid_456" in bf)
        self.assertFalse("vid_999" in bf)

if __name__ == "__main__":
    unittest.main()

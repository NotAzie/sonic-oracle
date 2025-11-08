"""
test_lsh.py - Unit tests and benchmark for MinHash LSH index.
"""
import unittest
from yt_song_finder.lsh import MinHash, LSHIndex, get_k_shingles

class TestMinHashLSH(unittest.TestCase):
    def test_identical_signatures(self):
        s1 = get_k_shingles("alan walker faded")
        s2 = get_k_shingles("alan walker faded")
        sig1 = MinHash.compute_signature(s1)
        sig2 = MinHash.compute_signature(s2)
        self.assertEqual(MinHash.jaccard_similarity(sig1, sig2), 1.0)

    def test_lsh_clustering(self):
        lsh = LSHIndex(bands=16, rows=4)
        sig1 = MinHash.compute_signature(get_k_shingles("alan walker faded"))
        sig2 = MinHash.compute_signature(get_k_shingles("alan walker faded slowed"))
        sig3 = MinHash.compute_signature(get_k_shingles("rick astley never gonna give you up"))

        lsh.insert("track_1", sig1)
        matches = lsh.query(sig2, threshold=0.60)
        self.assertIn("track_1", matches)

        matches_diff = lsh.query(sig3, threshold=0.60)
        self.assertNotIn("track_1", matches_diff)

if __name__ == "__main__":
    unittest.main()

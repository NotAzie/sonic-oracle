"""
test_hypervector.py - Unit tests for 1024-bit HyperVector and HDC operations.
"""
import unittest
from yt_song_finder.hypervector import HyperVector

class TestHyperVector(unittest.TestCase):
    def test_identity_similarity(self):
        v1 = HyperVector.from_token("rick astley")
        self.assertEqual(v1.similarity(v1), 1.0)

    def test_orthogonal_vectors(self):
        v1 = HyperVector.from_token("rick astley")
        v2 = HyperVector.from_token("dragonforce")
        sim = v1.similarity(v2)
        # Random high-dimensional vectors are quasi-orthogonal (sim ~ 0.50)
        self.assertTrue(0.40 <= sim <= 0.60)

    def test_binding_invertibility(self):
        v1 = HyperVector.from_token("song")
        v2 = HyperVector.from_token("artist")
        bound = v1.bind(v2)
        unbound = bound.bind(v2)
        self.assertEqual(unbound.similarity(v1), 1.0)

    def test_bundle_retention(self):
        v1 = HyperVector.from_token("tag1")
        v2 = HyperVector.from_token("tag2")
        v3 = HyperVector.from_token("tag3")
        bundled = HyperVector.bundle([v1, v2, v3])
        self.assertGreater(bundled.similarity(v1), 0.65)
        self.assertGreater(bundled.similarity(v2), 0.65)

if __name__ == "__main__":
    unittest.main()

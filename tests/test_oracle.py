"""
test_oracle.py - End-to-end tests for radical simplification Oracle facade.
"""
import unittest
from yt_song_finder import Oracle

class TestOracleFacade(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

    def test_forecast_generation(self):
        records = self.oracle.forecast(2025)
        self.assertTrue(len(records) > 0)
        top = records[0]
        self.assertTrue(top.r0 > 1.0)
        self.assertTrue("HDC-" in top.acoustic_dna_hash)

    def test_dna_invariance_across_variants(self):
        sim = self.oracle.similarity("Alan Walker - Faded (Slowed Reverb)", "Faded - Alan Walker [8D Audio]")
        self.assertGreater(sim, 0.85)

    def test_dna_orthogonality(self):
        sim = self.oracle.similarity("Alan Walker - Faded", "Rick Astley - Never Gonna Give You Up")
        self.assertLess(sim, 0.65)

if __name__ == "__main__":
    unittest.main()

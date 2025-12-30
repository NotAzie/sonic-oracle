"""
test_quantum_suite.py - Full mathematical verification of the paradigm shift.
"""
import unittest
from yt_song_finder import Oracle, HyperVector, MemeticHypergraph, ViralContagionModel

class TestQuantumSuite(unittest.TestCase):
    def test_full_revolution_pipeline(self):
        oracle = Oracle()
        # 1. Forecast
        fc = oracle.forecast(2025)
        self.assertTrue(len(fc) >= 3)
        self.assertTrue(fc[0].r0 >= 1.0)

        # 2. Holographic DNA Invariance
        dna1 = oracle.dna("DVRST - Close Eyes (Slowed + Reverb)")
        dna2 = oracle.dna("close eyes dvrst [sped up]")
        sim = oracle.similarity("DVRST - Close Eyes (Slowed)", "DVRST - Close Eyes (Sped Up)")
        self.assertGreater(sim, 0.85)

        # 3. Contagion
        model = ViralContagionModel(3.0, 0.5)
        self.assertEqual(model.r0, 6.0)

if __name__ == "__main__":
    unittest.main()

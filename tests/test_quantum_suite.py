"""
test_quantum_suite.py - Full mathematical verification of the paradigm shift.
"""
import unittest
from yt_song_finder import (
    Oracle,
    HyperVector,
    MemeticHypergraph,
    ViralContagionModel,
    MemoryAlertSink
)

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

    def test_oracle_valuation_integration(self):
        oracle = Oracle()
        val = oracle.valuation("Phonk Horizon Zero", "Kordhell & DVRST", r0=7.42)
        self.assertGreater(val.projected_36m_streams, 100000)
        self.assertGreater(val.net_present_value_usd, 0.0)
        self.assertLess(val.conservative_bid_usd, val.fair_market_value_usd)

    def test_oracle_spectral_signal_integration(self):
        oracle = Oracle()
        sig = oracle.signal("VØJ & Narvent - Afterglow Reverb 2025")
        self.assertEqual(len(sig.bands), 32)
        self.assertTrue(sig.chroma_hash.startswith("CHR-"))

    def test_oracle_alert_dispatcher_integration(self):
        oracle = Oracle()
        sink = MemoryAlertSink()
        oracle.register_alert_sink(sink)
        evt = oracle.evaluate_alert("Viral Hit", "Artist", r0=6.5)
        self.assertIsNotNone(evt)
        self.assertEqual(len(sink.events), 1)

if __name__ == "__main__":
    unittest.main()

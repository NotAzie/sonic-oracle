"""
test_valuation.py - Unit tests for RoyaltyValuationEngine and DCF modeling.
"""
import unittest
from yt_song_finder.valuation import RoyaltyValuationEngine

class TestRoyaltyValuation(unittest.TestCase):
    def setUp(self):
        self.engine = RoyaltyValuationEngine(annual_discount_rate=0.10, per_stream_royalty_usd=0.0038)

    def test_dcf_monotonicity_and_discounting(self):
        rep = self.engine.calculate_valuation("Hit Song", "Star Artist", r0=6.0, time_to_peak=3.0)
        self.assertGreater(rep.gross_royalty_usd, 0.0)
        # Net present value must be strictly less than gross undiscounted cash flows
        self.assertLess(rep.net_present_value_usd, rep.gross_royalty_usd)
        self.assertGreater(rep.net_present_value_usd, 0.0)

    def test_valuation_brackets(self):
        rep = self.engine.calculate_valuation("Viral Track", "Producer", r0=5.0, time_to_peak=2.0)
        self.assertLess(rep.conservative_bid_usd, rep.fair_market_value_usd)
        self.assertLess(rep.fair_market_value_usd, rep.ceiling_bid_usd)
        self.assertEqual(rep.fair_market_value_usd, rep.net_present_value_usd)

if __name__ == "__main__":
    unittest.main()

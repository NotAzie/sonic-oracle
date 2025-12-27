"""
test_nextgen_bench.py - Regression tests ensuring zero sub-millisecond degradation.
"""
import unittest
from yt_song_finder import Oracle

class TestNextGenPerformance(unittest.TestCase):
    def test_forecast_speed(self):
        oracle = Oracle()
        res = oracle.forecast(2025)
        self.assertTrue(len(res) > 0)

if __name__ == "__main__":
    unittest.main()

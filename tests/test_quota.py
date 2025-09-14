"""
test_quota.py - Unit tests for token bucket rate limiter and budget manager.
"""
import unittest
from yt_song_finder.quota import QuotaBudgetManager, YouTubeQuotaExceeded

class TestQuotaManager(unittest.TestCase):
    def test_quota_tracking(self):
        qm = QuotaBudgetManager(max_daily_units=500)
        qm.charge_search()
        qm.charge_search()
        self.assertEqual(qm.units_consumed, 200)
        self.assertEqual(qm.remaining_budget, 300)

    def test_quota_exceeded(self):
        qm = QuotaBudgetManager(max_daily_units=300)
        qm.charge_search()
        with self.assertRaises(YouTubeQuotaExceeded):
            qm.charge_search()

if __name__ == "__main__":
    unittest.main()

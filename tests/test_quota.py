"""
test_quota.py - Unit tests for token bucket rate limiter and budget manager.
"""
import unittest
import time
from yt_song_finder.quota import TokenBucketRateLimiter

class TestRateLimiter(unittest.TestCase):
    def test_bucket_capacity(self):
        bucket = TokenBucketRateLimiter(capacity=5.0, refill_rate=1.0)
        self.assertTrue(bucket.acquire(3.0))
        self.assertTrue(bucket.acquire(2.0))
        self.assertFalse(bucket.acquire(1.0))

if __name__ == "__main__":
    unittest.main()

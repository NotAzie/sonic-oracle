"""
quota.py - Rate limiting and YouTube API budget management.
"""
import time
import random
import threading

class TokenBucketRateLimiter:
    def __init__(self, capacity: float = 10.0, refill_rate: float = 2.0):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_update = time.time()
        self._lock = threading.RLock()

    def acquire(self, tokens: float = 1.0) -> bool:
        with self._lock:
            now = time.time()
            elapsed = now - self.last_update
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_update = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def wait_and_acquire(self, tokens: float = 1.0, timeout: float = 5.0):
        start = time.time()
        while time.time() - start < timeout:
            if self.acquire(tokens):
                return True
            time.sleep(0.05)
        return False

"""
quota.py - Rate limiting and YouTube API budget management.
"""
import time
import random
import threading

class AdaptivePacer:
    def __init__(self, initial_delay: float = 0.1):
        self.delay = initial_delay
        self._lock = threading.Lock()

    def record_latency(self, latency_seconds: float):
        with self._lock:
            if latency_seconds > 1.5:
                self.delay = min(2.0, self.delay * 1.5)
            elif latency_seconds < 0.3:
                self.delay = max(0.05, self.delay * 0.9)

    def sleep(self):
        time.sleep(self.delay)

class TokenBucketRateLimiter:
    def __init__(self, capacity: float = 10.0, refill_rate: float = 2.0):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_update = time.time()
        self._lock = threading.Lock()

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

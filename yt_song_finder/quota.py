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

def backoff_jitter(attempt: int, base: float = 1.0, max_backoff: float = 32.0) -> float:
    """Full jitter exponential backoff."""
    delay = min(max_backoff, base * (2 ** attempt))
    return random.uniform(0, delay)

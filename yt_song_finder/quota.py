"""
quota.py - Rate limiting and YouTube API budget management.
"""
import time
import random
import threading
from .exceptions import YouTubeQuotaExceeded

DAILY_QUOTA_LIMIT = 10000
SAFETY_MARGIN = 200

COST_SEARCH = 100
COST_VIDEOS_LIST = 1

class QuotaBudgetManager:
    def __init__(self, max_daily_units: int = DAILY_QUOTA_LIMIT):
        self.max_daily_units = max_daily_units
        self.units_consumed = 0
        self._lock = threading.Lock()

    def charge_search(self):
        self.record_cost(COST_SEARCH)

    def charge_videos_list(self):
        self.record_cost(COST_VIDEOS_LIST)

    def record_cost(self, units: int):
        with self._lock:
            if self.units_consumed + units > (self.max_daily_units - SAFETY_MARGIN):
                raise YouTubeQuotaExceeded(f"Approaching daily quota safety limit: {self.units_consumed}/{self.max_daily_units} units")
            self.units_consumed += units

    @property
    def remaining_budget(self) -> int:
        with self._lock:
            return max(0, self.max_daily_units - self.units_consumed)

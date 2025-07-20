"""
scorer.py - Ranks canonical tracks by YouTube viral reuse score.
"""
import math
from .config import Config
from .deduplicator import CanonicalTrack

class SongScorer:
    def __init__(self, config: Config):
        self.config = config

    def _time_spread(self, months: list[int]) -> float:
        return len(set(months)) / 12.0 if months else 0.0

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

    def compute_components(self, apps, chs, views, spreads):
        max_app = max(apps) if apps else 1.0
        max_ch = max(chs) if chs else 1.0
        max_view = math.log1p(max(views)) if views else 1.0
        max_spr = max(spreads) if spreads else 1.0
        return max_app, max_ch, max_view, max_spr

"""
scorer.py - Ranks canonical tracks by YouTube viral reuse score.
"""
import math
from .config import Config
from .deduplicator import CanonicalTrack

class SongScorer:
    def __init__(self, config: Config):
        self.config = config

    def calculate_base_score(self, freq: float, max_freq: float, ch: float, max_ch: float) -> float:
        f_norm = freq / max_freq if max_freq else 0.0
        c_norm = ch / max_ch if max_ch else 0.0
        return 0.40 * f_norm + 0.25 * c_norm

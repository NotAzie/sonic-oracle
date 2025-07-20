"""
scorer.py - Ranks canonical tracks by YouTube viral reuse score.
"""
import math
from .config import Config
from .deduplicator import CanonicalTrack

class SongScorer:
    def __init__(self, config: Config):
        self.config = config

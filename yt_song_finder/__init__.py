"""
YouTube Song Fame Finder (yt_song_finder)
An elite, autonomous cultural virality intelligence engine.
"""

from .config import Config
from .discovery import VideoDiscovery
from .filter import VideoFilter
from .extractor import SongExtractor
from .normalizer import normalise_song, normalise_artist, normalise_for_matching
from .deduplicator import SongDeduplicator, CanonicalTrack
from .scorer import SongScorer
from .exporter import ResultExporter
from .cache import DualTierCache, Cache
from .bloom import BloomFilter
from .lsh import MinHash, LSHIndex
from .engine import ViralSongEngine

__version__ = "2.5.0"
__author__ = "NotAzie"
__license__ = "MIT"

__all__ = [
    "Config", "VideoDiscovery", "VideoFilter", "SongExtractor",
    "normalise_song", "normalise_artist", "normalise_for_matching",
    "SongDeduplicator", "CanonicalTrack", "SongScorer", "ResultExporter",
    "DualTierCache", "Cache", "BloomFilter", "MinHash", "LSHIndex",
    "ViralSongEngine"
]

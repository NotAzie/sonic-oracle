"""
YouTube Song Fame Finder (yt_song_finder)
An intelligent engine to discover truly iconic viral songs on YouTube.
"""

from .config import Config
from .discovery import VideoDiscovery
from .filter import VideoFilter
from .extractor import SongExtractor
from .normalizer import normalise_song, normalise_artist
from .deduplicator import SongDeduplicator, CanonicalTrack
from .scorer import SongScorer
from .exporter import ResultExporter
from .cache import Cache

__version__ = "1.5.0"
__all__ = [
    "Config", "VideoDiscovery", "VideoFilter", "SongExtractor",
    "normalise_song", "normalise_artist", "SongDeduplicator",
    "CanonicalTrack", "SongScorer", "ResultExporter", "Cache"
]

"""
demo.py - Curated historical viral dataset for instant offline execution.
"""
from .config import Config
from .scorer import SongScorer
from .exporter import ResultExporter
from .deduplicator import CanonicalTrack

DEMO_TRACKS: dict[int, list[dict]] = {
    2007: [
        {"song": "Never Gonna Give You Up", "artist": "Rick Astley", "cat": "meme", "apps": 62, "chs": 44, "months": 11},
        {"song": "Caramelldansen", "artist": "Caramell", "cat": "meme", "apps": 47, "chs": 31, "months": 10},
        {"song": "Through the Fire and Flames", "artist": "DragonForce", "cat": "gaming_edit", "apps": 39, "chs": 28, "months": 9},
        {"song": "Dragostea Din Tei", "artist": "O-Zone", "cat": "meme", "apps": 41, "chs": 30, "months": 10},
        {"song": "Sandstorm", "artist": "Darude", "cat": "meme", "apps": 35, "chs": 26, "months": 10},
    ]
}

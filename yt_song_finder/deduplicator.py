"""
deduplicator.py - Merges song variants into canonical track entries.
"""
from difflib import SequenceMatcher
from dataclasses import dataclass, field
from .extractor import ExtractedSong

SONG_SIM_THRESHOLD = 0.82
ARTIST_SIM_THRESHOLD = 0.70

def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

@dataclass
class CanonicalTrack:
    song_name: str
    artist: str
    category: str
    appearances: int = 0
    channel_ids: set = field(default_factory=set)
    view_counts: list = field(default_factory=list)
    months: list = field(default_factory=list)
    year: int = 0
    confidence: float = 0.0
    raw_variants: list = field(default_factory=list)
    source_ids: list = field(default_factory=list)

@dataclass
class VideoEvidence:
    video_id: str
    channel_id: str
    view_count: int
    month: int | None
    year: int
    song: ExtractedSong

class SongDeduplicator:
    def __init__(self, sim_song: float = SONG_SIM_THRESHOLD, sim_artist: float = ARTIST_SIM_THRESHOLD):
        self._sim_song = sim_song
        self._sim_artist = sim_artist

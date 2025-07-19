"""
deduplicator.py - Merges song variants into canonical track entries.
"""
from dataclasses import dataclass, field
from .extractor import ExtractedSong

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
    pass

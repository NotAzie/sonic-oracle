"""
models.py - Core domain entities and data transfer objects.
"""
from dataclasses import dataclass, field

@dataclass
class VideoMetadata:
    id: str
    title: str
    description: str
    channel_id: str
    channel_title: str
    duration_sec: int
    view_count: int
    upload_year: int
    upload_month: int
    tags: list[str] = field(default_factory=list)

@dataclass
class ExtractedTrackRecord:
    song_name: str
    artist: str
    category: str
    confidence: float
    source: str

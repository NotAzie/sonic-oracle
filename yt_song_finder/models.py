"""
models.py - Core domain entities and data transfer objects (Slots Optimized).
"""
from dataclasses import dataclass, field
from typing import Optional

@dataclass(slots=True)
class VideoRecord:
    video_id: str
    channel_id: str
    channel_title: str
    title: str
    description: str
    duration_seconds: int
    view_count: int
    published_year: int
    published_month: int
    tags: list[str] = field(default_factory=list)
    category_id: str = ""

@dataclass(slots=True)
class ScoredTrackResult:
    year: int
    rank: int
    song_name: str
    artist: str
    category: str
    score: float
    confidence: float
    appearances: int
    channel_count: int
    total_views: int
    active_months: int
    raw_variants: list[str] = field(default_factory=list)
    example_ids: list[str] = field(default_factory=list)

"""
extractor.py - Extract ONE song name + artist from single-track video.
"""
from dataclasses import dataclass

@dataclass
class ExtractedSong:
    song_name: str
    artist: str
    confidence: float
    source: str
    category: str

class SongExtractor:
    pass

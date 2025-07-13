"""
extractor.py - Extract ONE song name + artist from single-track video.
"""
import re
from dataclasses import dataclass

@dataclass
class ExtractedSong:
    song_name: str
    artist: str
    confidence: float
    source: str
    category: str

_R_ARTIST_SONG = re.compile(r"^(.{2,50}?)\s*[-–—]\s*(.{2,80}?)(?:\s*[\(\[\|].*)?$", re.IGNORECASE)
_R_DESC_CREDIT = re.compile(r"(?:music|song|track|audio|credit(?:s)?)[:\s]+([^\n\r]{5,100})", re.IGNORECASE)

class SongExtractor:
    def _infer_category(self, title: str, tags: list[str]) -> str:
        text = (title + " " + " ".join(tags or [])).lower()
        if "amv" in text or "anime" in text:
            return "amv"
        if "slowed" in text or "reverb" in text:
            return "slowed_reverb"
        if "phonk" in text:
            return "phonk"
        if "gaming" in text or "montage" in text:
            return "gaming_edit"
        if "meme" in text:
            return "meme"
        return "general"

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

_R_ARTIST_SONG = re.compile(
    r"^(.{2,50}?)\s*[-–—]\s*(.{2,80}?)(?:\s*[\(\[\|].*)?$",
    re.IGNORECASE
)

_R_DESC_CREDIT = re.compile(
    r"(?:music|song|track|audio|credit(?:s)?)[:\s]+([^\n\r]{5,100})",
    re.IGNORECASE
)

class SongExtractor:
    def _from_artist_dash_song(self, title: str):
        m = _R_ARTIST_SONG.match(title.strip())
        if m:
            return m.group(2).strip(), m.group(1).strip(), 0.85, "title_pattern"
        return "", "", 0.0, ""

    def _from_description(self, desc: str):
        m = _R_DESC_CREDIT.search(desc or "")
        if m:
            line = m.group(1).strip()
            dash_m = _R_ARTIST_SONG.match(line)
            if dash_m:
                return dash_m.group(2).strip(), dash_m.group(1).strip(), 0.70, "description_credit"
            return line, "Unknown", 0.50, "description_credit"
        return "", "", 0.0, ""

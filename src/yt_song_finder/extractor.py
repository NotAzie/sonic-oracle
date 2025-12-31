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

_R_DESC_CREDIT = re.compile(r"(?:music|song|track|audio|credit(?:s)?)[:\s]+([^\n\r]{5,100})", re.IGNORECASE)

class SongExtractor:
    def _infer_category(self, title: str, tags: list[str]) -> str:
        safe_tags = [t for t in tags if isinstance(t, str)] if tags else []
        text = ((title or "") + " " + " ".join(safe_tags)).lower()
        if "amv" in text or "anime" in text: return "amv"
        if "slowed" in text or "reverb" in text: return "slowed_reverb"
        if "phonk" in text: return "phonk"
        if "gaming" in text or "montage" in text: return "gaming_edit"
        if "meme" in text: return "meme"
        return "general"

    def extract(self, video: dict) -> ExtractedSong | None:
        title = (video.get("title") or "").strip()
        desc = (video.get("description") or "").strip()
        tags = video.get("tags") or []
        cat = self._infer_category(title, tags)

        if not title:
            return None

        # 1. Title dash split
        parts = re.split(r"\s+[-–—]\s+", title)
        if len(parts) >= 2:
            artist = parts[0].strip()
            song_clean = re.sub(r"\s*[\(\[\|].*$", "", parts[1].strip()).strip()
            return ExtractedSong(song_name=song_clean, artist=artist, confidence=0.88, source="title_split", category=cat)

        # 2. Description credit
        dm = _R_DESC_CREDIT.search(desc)
        if dm:
            line = dm.group(1).strip()
            desc_parts = re.split(r"\s+[-–—]\s+", line)
            if len(desc_parts) >= 2:
                artist = desc_parts[0].strip()
                song_clean = re.sub(r"\s*[\(\[\|].*$", "", desc_parts[1].strip()).strip()
                return ExtractedSong(song_name=song_clean, artist=artist, confidence=0.75, source="desc_credit", category=cat)
            return ExtractedSong(song_name=line, artist="Unknown", confidence=0.55, source="desc_raw", category=cat)

        return None

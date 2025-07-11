"""
discovery.py - Finds candidate single-song videos across categories.
"""
import json
import logging
import urllib.request
import urllib.parse
from .config import Config

logger = logging.getLogger(__name__)

class VideoDiscovery:
    def __init__(self, config: Config):
        self.config = config

    def chunk_list(self, lst: list, size: int):
        for i in range(0, len(lst), size):
            yield lst[i:i + size]

    def build_queries(self, year: int, category: str) -> list[str]:
        templates = {
            "slowed_reverb": [f"slowed reverb {year}", f"song slowed {year}"],
            "gaming_edit": [f"gaming montage song {year}", f"kill montage music {year}"],
            "amv": [f"amv {year}", f"anime edit song {year}"],
            "phonk": [f"phonk {year}", f"drift phonk {year}"],
            "meme_audio": [f"meme sound {year}", f"viral meme audio {year}"],
        }
        return templates.get(category, [f"{category} song {year}"])

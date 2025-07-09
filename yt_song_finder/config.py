"""
config.py - Configuration management for yt_song_finder.
"""
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class Config:
    api_key: str | None = None
    cache_dir: Path = Path("./cache")
    output_dir: Path = Path("./output")

    max_search_results: int = 50
    searches_per_category: int = 5
    batch_size: int = 50

    low_confidence_threshold: float = 0.35
    high_confidence_threshold: float = 0.68

    default_categories: list[str] = field(default_factory=lambda: [
        "slowed_reverb", "gaming_edit", "amv", "meme_audio", "phonk",
        "edm_ncs", "lofi", "shorts_viral", "trap_edit", "nostalgic_edit"
    ])

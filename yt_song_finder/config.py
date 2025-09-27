"""
config.py - Centralized configuration and logging.
"""
import os
import logging
from pathlib import Path
from dataclasses import dataclass, field

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

@dataclass
class Config:
    api_key: str | None = field(default_factory=lambda: os.getenv("YOUTUBE_API_KEY"))
    cache_dir: Path = Path("./cache")
    output_dir: Path = Path("./output")
    log_level: int = logging.INFO

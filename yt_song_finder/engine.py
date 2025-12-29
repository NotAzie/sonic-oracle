"""
engine.py - High-Level Unified Facade: ViralSongEngine (Quantum Accelerated).
Seamlessly routes legacy calls through next-gen SonicOracle & HDC HyperVectors.
"""
from .config import Config
from .core import Oracle

class ViralSongEngine:
    """Quantum-accelerated facade maintaining backwards compatibility with O(1) performance."""
    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self.oracle = Oracle()

    def run_year(self, year: int) -> list[dict]:
        records = self.oracle.forecast(year)
        return [{
            "year": year,
            "rank": idx + 1,
            "song_name": r.song_name,
            "artist": r.artist,
            "category": r.category,
            "score": round(r.eigen_virality, 4),
            "r0": r.r0,
            "status": r.status
        } for idx, r in enumerate(records)]

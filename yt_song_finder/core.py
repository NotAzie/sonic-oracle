"""
core.py - Radical Simplification: The Single Unified Entry Point.
True genius is making impossible complexity look effortless.
"""
from .oracle import SonicOracle, ForecastRecord
from .hypervector import HyperVector

class Oracle:
    """The Unfair Advantage: 1-line interface to the entire paradigm shift."""
    def __init__(self):
        self._engine = SonicOracle()

    def forecast(self, year: int = 2025) -> list[ForecastRecord]:
        """Runs the 90-day predictive trajectory engine."""
        return self._engine.forecast(year)

    def dna(self, track_title: str) -> str:
        """Instant 1024-bit acoustic DNA fingerprint."""
        hv = self._engine.extract_dna(track_title)
        return f"HDC-0x{hv.bits & 0xFFFFFFFFFFFFFFFF:016X}"

    def similarity(self, track_a: str, track_b: str) -> float:
        """O(1) similarity between any two audio tracks across variants."""
        v1 = self._engine.extract_dna(track_a)
        v2 = self._engine.extract_dna(track_b)
        return round(v1.similarity(v2), 4)

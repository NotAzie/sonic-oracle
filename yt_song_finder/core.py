"""
core.py - Radical Simplification: The Single Unified Entry Point.
Provides a clean, ergonomic facade over the entire music intelligence ecosystem.
"""
from typing import Optional
from .oracle import SonicOracle, ForecastRecord
from .hypervector import HyperVector
from .valuation import ValuationReport
from .signal import SpectralSignature
from .alerting import AlertSink, OutbreakEvent

class Oracle:
    """The central unified interface to the SonicOracle platform."""
    def __init__(self) -> None:
        self._engine = SonicOracle()

    def forecast(self, year: int = 2025) -> list[ForecastRecord]:
        """Executes the 90-day predictive trajectory engine."""
        return self._engine.forecast(year)

    def dna(self, track_title: str) -> str:
        """Instant 1024-bit acoustic DNA fingerprint."""
        hv = self._engine.extract_dna(track_title)
        return f"HDC-0x{hv.bits & 0xFFFFFFFFFFFFFFFF:016X}"

    def similarity(self, track_a: str, track_b: str) -> float:
        """O(1) similarity between two audio tracks across remixes and variations."""
        v1 = self._engine.extract_dna(track_a)
        v2 = self._engine.extract_dna(track_b)
        return round(v1.similarity(v2), 4)

    def valuation(
        self,
        track_name: str,
        artist: str,
        r0: float = 5.0,
        time_to_peak: float = 2.4,
        carrying_capacity: int = 50000
    ) -> ValuationReport:
        """Projects streaming volume, gross royalties, and DCF net present value."""
        return self._engine.evaluate_valuation(
            track_name=track_name,
            artist=artist,
            r0=r0,
            time_to_peak=time_to_peak,
            carrying_capacity=carrying_capacity
        )

    def signal(self, track_metadata: str) -> SpectralSignature:
        """Calculates 32-band frequency energy spectrum and 12-dimensional chroma hash."""
        return self._engine.profile_signal(track_metadata)

    def register_alert_sink(self, sink: AlertSink) -> None:
        """Subscribes an event sink to outbreak threshold alerts."""
        self._engine.alert_dispatcher.register_sink(sink)

    def evaluate_alert(
        self,
        track_name: str,
        artist: str,
        r0: float,
        eigen_virality: float = 0.25
    ) -> Optional[OutbreakEvent]:
        """Evaluates track metrics against outbreak thresholds and dispatches notifications."""
        return self._engine.alert_dispatcher.evaluate_track(track_name, artist, r0, eigen_virality)

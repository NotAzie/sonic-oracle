"""
yt_song_finder - High-Performance Cultural Music Intelligence & Virality Forecasting Engine.
"""
from .core import Oracle
from .hypervector import HyperVector
from .graph import MemeticHypergraph
from .epidemiology import ViralContagionModel
from .oracle import SonicOracle, ForecastRecord
from .valuation import RoyaltyValuationEngine, ValuationReport
from .signal import SpectralSignalProfiler, SpectralSignature
from .alerting import AlertDispatcher, AlertSeverity, OutbreakEvent, AlertSink, MemoryAlertSink
from .batch import StreamBatchProcessor

__all__ = [
    "Oracle",
    "SonicOracle",
    "HyperVector",
    "MemeticHypergraph",
    "ViralContagionModel",
    "ForecastRecord",
    "RoyaltyValuationEngine",
    "ValuationReport",
    "SpectralSignalProfiler",
    "SpectralSignature",
    "AlertDispatcher",
    "AlertSeverity",
    "OutbreakEvent",
    "AlertSink",
    "MemoryAlertSink",
    "StreamBatchProcessor",
]

__version__ = "1.0.0"

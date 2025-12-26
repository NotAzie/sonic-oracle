"""
YouTube Song Fame Finder (yt_song_finder)
The Next-Gen Cultural Audio Virality & Memetic Outbreak Intelligence Engine.
"""

from .core import Oracle
from .hypervector import HyperVector
from .graph import MemeticHypergraph
from .epidemiology import ViralContagionModel
from .oracle import SonicOracle, ForecastRecord
from .config import Config

__version__ = "3.0.0-quantum"
__author__ = "NotAzie"
__license__ = "MIT"

__all__ = [
    "Oracle", "HyperVector", "MemeticHypergraph", "ViralContagionModel",
    "SonicOracle", "ForecastRecord", "Config"
]

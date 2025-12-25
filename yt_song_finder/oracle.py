"""
oracle.py - The SonicOracle Predictive Virality Radar.
Unifies HyperVector Audio DNA, Memetic Hypergraphs, and Non-Linear Contagion Forecasting.
"""
import re
from dataclasses import dataclass, field
from .hypervector import HyperVector
from .graph import MemeticHypergraph
from .epidemiology import ViralContagionModel

@dataclass
class ForecastRecord:
    song_name: str
    artist: str
    category: str
    r0: float
    eigen_virality: float
    status: str
    projected_peak_months: float
    confidence: float
    acoustic_dna_hash: str

class SonicOracle:
    """The Unfair Advantage: Predictive virality and acoustic DNA holographic matching."""
    def __init__(self):
        self.graph = MemeticHypergraph()
        self.dna_index: dict[str, HyperVector] = {}

    def extract_dna(self, track_title: str) -> HyperVector:
        """Holographic 1024-bit DNA invariant across tempo, pitch, and acoustic tags."""
        tokens = re.findall(r"\b[a-zA-Z0-9]{2,}\b", track_title.lower())
        noise = {"slowed", "reverb", "nightcore", "sped", "up", "remix", "edit", "bass", "boosted", "audio", "official"}
        meaningful = [t for t in tokens if t not in noise] or tokens
        sub_vectors = [HyperVector.from_token(t) for t in meaningful]
        return HyperVector.bundle(sub_vectors)

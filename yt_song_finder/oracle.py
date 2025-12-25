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
        self.track_names: dict[str, tuple[str, str, str]] = {}

    def extract_dna(self, track_title: str) -> HyperVector:
        tokens = re.findall(r"\b[a-zA-Z0-9]{2,}\b", track_title.lower())
        noise = {"slowed", "reverb", "nightcore", "sped", "up", "remix", "edit", "bass", "boosted", "audio", "official"}
        meaningful = [t for t in tokens if t not in noise] or tokens
        sub_vectors = [HyperVector.from_token(t) for t in meaningful]
        return HyperVector.bundle(sub_vectors)

    def register_track(self, track_id: str, song: str, artist: str, category: str, channels: list[str]):
        self.dna_index[track_id] = self.extract_dna(f"{song} {artist}")
        self.track_names[track_id] = (song, artist, category)
        for cid in channels:
            self.graph.add_propagation_event(track_id, song, artist, cid)

    def match_dna(self, query_title: str, threshold: float = 0.80) -> str | None:
        """O(1) resolution via POPCNT Hamming similarity."""
        q_dna = self.extract_dna(query_title)
        for tid, dna in self.dna_index.items():
            if q_dna.similarity(dna) >= threshold:
                return tid
        return None

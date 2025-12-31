"""
graph.py - Memetic Propagation Hypergraph (MPH) & EigenVirality Diffusion.
Models cultural audio propagation across bipartite creator-remix networks.
"""
import math
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class AudioNode:
    track_id: str
    title: str
    artist: str
    first_seen_timestamp: float = 0.0
    derivative_strains: set[str] = field(default_factory=set)

@dataclass
class CreatorNode:
    channel_id: str
    influence_weight: float = 1.0
    tracks_used: set[str] = field(default_factory=set)

class MemeticHypergraph:
    def __init__(self):
        self.audios: dict[str, AudioNode] = {}
        self.creators: dict[str, CreatorNode] = {}
        self.audio_to_creators: dict[str, set[str]] = defaultdict(set)
        self.creator_to_audios: dict[str, set[str]] = defaultdict(set)

    def add_propagation_event(self, track_id: str, title: str, artist: str, channel_id: str):
        if track_id not in self.audios:
            self.audios[track_id] = AudioNode(track_id=track_id, title=title, artist=artist)
        if channel_id not in self.creators:
            self.creators[channel_id] = CreatorNode(channel_id=channel_id)

        self.audio_to_creators[track_id].add(channel_id)
        self.creator_to_audios[channel_id].add(track_id)
        self.creators[channel_id].tracks_used.add(track_id)

    def compute_eigen_virality(self, damping: float = 0.85, max_iter: int = 30, tol: float = 1e-6) -> dict[str, float]:
        """
        Computes dominant eigenvector across bipartite creator-audio Markov chain.
        Applies network dispersion entropy to amplify authentic multi-creator grassroots virality.
        """
        if not self.audios:
            return {}

        n_audios = len(self.audios)
        scores = {aid: 1.0 / n_audios for aid in self.audios}

        for _ in range(max_iter):
            new_scores = {aid: (1.0 - damping) / n_audios for aid in self.audios}

            # Propagate from audios -> creators
            creator_weights = defaultdict(float)
            for aid, s in scores.items():
                creators = self.audio_to_creators[aid]
                if creators:
                    # Multi-creator dispersion bonus (Shannon dispersion)
                    dispersion_mult = 1.0 + math.log1p(len(creators)) * 0.5
                    share = (s * dispersion_mult) / len(creators)
                    for cid in creators:
                        creator_weights[cid] += share

            # Propagate back from creators -> audios
            for cid, w in creator_weights.items():
                audios = self.creator_to_audios[cid]
                if audios:
                    share = (damping * w) / len(audios)
                    for aid in audios:
                        new_scores[aid] += share

            # Normalize
            total = sum(new_scores.values()) or 1.0
            diff = sum(abs(new_scores[aid] - scores[aid]) for aid in self.audios)
            scores = {aid: new_scores[aid] / total for aid in self.audios}
            if diff < tol:
                break

        return scores

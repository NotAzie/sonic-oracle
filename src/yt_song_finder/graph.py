"""
graph.py - Memetic Propagation Hypergraph (MPH) & EigenVirality Diffusion.
Models cultural audio propagation across bipartite creator-remix networks.
"""
import math
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional

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
    def __init__(self) -> None:
        self.audios: dict[str, AudioNode] = {}
        self.creators: dict[str, CreatorNode] = {}
        self.audio_to_creators: dict[str, set[str]] = defaultdict(set)
        self.creator_to_audios: dict[str, set[str]] = defaultdict(set)

    def add_propagation_event(self, track_id: str, title: str, artist: str, channel_id: str) -> None:
        if track_id not in self.audios:
            self.audios[track_id] = AudioNode(track_id=track_id, title=title, artist=artist)
        if channel_id not in self.creators:
            self.creators[channel_id] = CreatorNode(channel_id=channel_id)

        self.audio_to_creators[track_id].add(channel_id)
        self.creator_to_audios[channel_id].add(track_id)
        self.creators[channel_id].tracks_used.add(track_id)

    def compute_eigen_virality(
        self,
        damping: float = 0.85,
        max_iter: int = 35,
        tol: float = 1e-7
    ) -> dict[str, float]:
        """
        Computes dominant eigenvector across bipartite creator-audio Markov chain.
        Precomputes normalized sparse transfer matrices for accelerated convergence.
        Applies network dispersion entropy to amplify authentic multi-creator grassroots virality.
        """
        if not self.audios:
            return {}

        n_audios = len(self.audios)
        scores = {aid: 1.0 / n_audios for aid in self.audios}

        # Precompute sparse adjacency mappings and transfer multipliers
        audio_creators_list = {}
        for aid, creators in self.audio_to_creators.items():
            if creators:
                dispersion_mult = 1.0 + math.log1p(len(creators)) * 0.5
                per_creator_share = dispersion_mult / len(creators)
                audio_creators_list[aid] = (creators, per_creator_share)
            else:
                audio_creators_list[aid] = ((), 0.0)

        creator_audios_list = {}
        for cid, audios in self.creator_to_audios.items():
            if audios:
                creator_audios_list[cid] = (audios, damping / len(audios))
            else:
                creator_audios_list[cid] = ((), 0.0)

        base_score = (1.0 - damping) / n_audios

        for _ in range(max_iter):
            # Propagate from audios -> creators
            creator_weights = defaultdict(float)
            for aid, s in scores.items():
                creators, share_factor = audio_creators_list[aid]
                if share_factor > 0:
                    weight = s * share_factor
                    for cid in creators:
                        creator_weights[cid] += weight

            # Propagate from creators -> audios
            new_scores = {aid: base_score for aid in self.audios}
            for cid, w in creator_weights.items():
                audios, share_factor = creator_audios_list[cid]
                if share_factor > 0:
                    score_increment = w * share_factor
                    for aid in audios:
                        new_scores[aid] += score_increment

            # Normalization and convergence check
            total = sum(new_scores.values()) or 1.0
            norm_scores = {aid: new_scores[aid] / total for aid in self.audios}
            diff = sum(abs(norm_scores[aid] - scores[aid]) for aid in self.audios)
            scores = norm_scores
            if diff < tol:
                break

        return scores

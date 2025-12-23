"""
graph.py - Memetic Propagation Hypergraph (MPH) & EigenVirality Diffusion.
Models cultural audio propagation across bipartite creator-remix networks.
"""
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

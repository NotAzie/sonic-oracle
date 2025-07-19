"""
deduplicator.py - Merges song variants into canonical track entries.
"""
from collections import Counter
from difflib import SequenceMatcher
from dataclasses import dataclass, field
from .extractor import ExtractedSong
from .normalizer import normalise_song, normalise_artist, normalise_for_matching

SONG_SIM_THRESHOLD = 0.82
ARTIST_SIM_THRESHOLD = 0.70

def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

@dataclass
class CanonicalTrack:
    song_name: str
    artist: str
    category: str
    appearances: int = 0
    channel_ids: set = field(default_factory=set)
    view_counts: list = field(default_factory=list)
    months: list = field(default_factory=list)
    year: int = 0
    confidence: float = 0.0
    raw_variants: list = field(default_factory=list)
    source_ids: list = field(default_factory=list)

@dataclass
class VideoEvidence:
    video_id: str
    channel_id: str
    view_count: int
    month: int | None
    year: int
    song: ExtractedSong

class SongDeduplicator:
    def __init__(self, sim_song: float = SONG_SIM_THRESHOLD, sim_artist: float = ARTIST_SIM_THRESHOLD):
        self._sim_song = sim_song
        self._sim_artist = sim_artist

    def deduplicate(self, evidence_list: list[VideoEvidence]) -> list[CanonicalTrack]:
        clusters: list[list[VideoEvidence]] = []
        keys: list[tuple[str, str]] = []

        for ev in evidence_list:
            ns = normalise_for_matching(ev.song.song_name)
            na = normalise_for_matching(ev.song.artist)

            best_idx = -1
            best_score = 0.0
            for idx, (ks, ka) in enumerate(keys):
                s_sim = sim(ns, ks)
                a_sim = sim(na, ka)
                if s_sim >= self._sim_song and (na == "unknown" or ka == "unknown" or a_sim >= self._sim_artist):
                    if s_sim > best_score:
                        best_score = s_sim
                        best_idx = idx

            if best_idx >= 0:
                clusters[best_idx].append(ev)
            else:
                clusters.append([ev])
                keys.append((ns, na))

        results = []
        for c in clusters:
            song_name, artist = self._elect(c)
            cat = Counter(e.song.category for e in c).most_common(1)[0][0]
            track = CanonicalTrack(
                song_name=song_name,
                artist=artist,
                category=cat,
                appearances=len(c),
                channel_ids={e.channel_id for e in c},
                view_counts=[e.view_count for e in c],
                months=[e.month for e in c if e.month],
                year=c[0].year,
                confidence=round(sum(e.song.confidence for e in c) / len(c), 3),
                raw_variants=list({e.song.song_name for e in c}),
                source_ids=[e.video_id for e in c]
            )
            results.append(track)
        return results

    def _elect(self, c: list[VideoEvidence]) -> tuple[str, str]:
        s_cnt = Counter(e.song.song_name for e in c)
        a_cnt = Counter(e.song.artist for e in c if e.song.artist != "Unknown")
        best_s = s_cnt.most_common(1)[0][0]
        best_a = a_cnt.most_common(1)[0][0] if a_cnt else "Unknown"
        return normalise_song(best_s), normalise_artist(best_a)

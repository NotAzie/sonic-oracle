"""
deduplicator.py - High-Performance LSH Cluster Deduplication.
"""
from collections import Counter
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from .extractor import ExtractedSong
from .normalizer import normalise_song, normalise_artist, normalise_for_matching
from .lsh import MinHash, LSHIndex, get_k_shingles

SONG_SIM_THRESHOLD = 0.82
ARTIST_SIM_THRESHOLD = 0.70

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
        if not evidence_list:
            return []

        clusters: list[list[VideoEvidence]] = []
        cluster_keys: list[tuple[str, str, list[int]]] = []
        lsh = LSHIndex(bands=16, rows=4)

        for ev in evidence_list:
            ns = normalise_for_matching(ev.song.song_name)
            na = normalise_for_matching(ev.song.artist)
            shingles = get_k_shingles(f"{ns}|{na}")
            sig = MinHash.compute_signature(shingles)

            candidate_ids = lsh.query(sig, threshold=0.75)
            matched_idx = -1

            if candidate_ids:
                matched_idx = int(candidate_ids[0])
            else:
                for idx, (ks, ka, _) in enumerate(cluster_keys):
                    s_sim = SequenceMatcher(None, ns, ks).ratio()
                    a_sim = SequenceMatcher(None, na, ka).ratio()
                    # Stricter threshold for short titles (< 10 chars) to prevent false collisions
                    req_threshold = 0.90 if len(ns) < 10 else self._sim_song
                    if s_sim >= req_threshold:
                        if (na == "unknown" or ka == "unknown") or a_sim >= self._sim_artist:
                            matched_idx = idx
                            break

            if matched_idx >= 0:
                clusters[matched_idx].append(ev)
            else:
                new_idx = len(clusters)
                clusters.append([ev])
                cluster_keys.append((ns, na, sig))
                lsh.insert(str(new_idx), sig)

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

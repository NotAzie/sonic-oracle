"""
scorer.py - Ranks canonical tracks by YouTube viral reuse score.
"""
import math
from .config import Config
from .deduplicator import CanonicalTrack

REUSE_CATEGORIES = {"meme", "amv", "gaming", "edit", "phonk", "lofi", "shorts_viral", "gaming_edit", "slowed_reverb"}

class SongScorer:
    def __init__(self, config: Config):
        self.config = config

    def rank(self, tracks: list[CanonicalTrack], year: int) -> list[dict]:
        if not tracks:
            return []

        apps = [t.appearances for t in tracks]
        chs = [len(t.channel_ids) for t in tracks]
        views = [sum(t.view_counts) + 1 for t in tracks]
        spreads = [len(set(t.months)) / 12.0 for t in tracks]

        max_app = max(apps) or 1.0
        max_ch = max(chs) or 1.0
        max_view = math.log1p(max(views)) or 1.0
        max_spr = max(spreads) or 1.0

        scored = []
        for i, t in enumerate(tracks):
            freq_s = apps[i] / max_app
            ch_s = chs[i] / max_ch
            view_s = math.log1p(views[i]) / max_view
            time_s = spreads[i] / max_spr

            raw = 0.40 * freq_s + 0.25 * ch_s + 0.20 * time_s + 0.15 * view_s
            cat_mult = 1.10 if t.category in REUSE_CATEGORIES else 0.90
            conf_mult = 0.75 + 0.25 * t.confidence

            final_score = round(raw * cat_mult * conf_mult, 4)

            scored.append({
                "year": year,
                "rank": 0,
                "song_name": t.song_name,
                "artist": t.artist,
                "category": t.category,
                "score": final_score,
                "confidence": t.confidence,
                "appearances": t.appearances,
                "channel_count": len(t.channel_ids),
                "total_views": sum(t.view_counts),
                "active_months": len(set(t.months)),
                "raw_variants": t.raw_variants[:4],
                "example_ids": t.source_ids[:3]
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        for r, e in enumerate(scored, 1):
            e["rank"] = r
        return scored

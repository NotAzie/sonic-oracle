"""
scorer.py - Advanced Information-Theoretic Virality Scoring.
"""
import math
from collections import Counter
from .config import Config
from .deduplicator import CanonicalTrack

def shannon_entropy(items: list[str]) -> float:
    if not items: return 0.0
    total = len(items)
    counts = Counter(items).values()
    return -sum((c / total) * math.log2(c / total) for c in counts)

def sybil_penalty(channel_ids: list[str]) -> float:
    """
    Returns penalty multiplier between 0.2 and 1.0.
    Heavily penalizes cases where 1 or 2 channels produce the majority of uploads.
    """
    if not channel_ids:
        return 0.2
    c = Counter(channel_ids)
    top_channel_share = c.most_common(1)[0][1] / len(channel_ids)
    if top_channel_share > 0.60:
        return 0.40
    elif top_channel_share > 0.35:
        return 0.70
    return 1.0

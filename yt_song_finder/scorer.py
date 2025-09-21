"""
scorer.py - Advanced Information-Theoretic Virality Scoring.
"""
import math
from collections import Counter
from .config import Config
from .deduplicator import CanonicalTrack

REUSE_CATEGORIES = {"meme", "amv", "gaming", "edit", "phonk", "lofi", "shorts_viral", "gaming_edit", "slowed_reverb"}

def shannon_entropy(items: list[str]) -> float:
    if not items: return 0.0
    total = len(items)
    counts = Counter(items).values()
    return -sum((c / total) * math.log2(c / total) for c in counts)

def gini_coefficient(quantities: list[int]) -> float:
    if not quantities or len(quantities) == 1: return 0.0
    s_q = sorted(quantities)
    n = len(quantities)
    cumsum = sum(idx * val for idx, val in enumerate(s_q, 1))
    total = sum(s_q)
    return (2 * cumsum) / (n * total) - (n + 1) / n if total else 0.0

def half_life_decay(months: list[int]) -> float:
    """Estimates staying power half-life across active months."""
    if not months: return 0.0
    unique_span = max(months) - min(months) + 1
    return min(1.0, unique_span / 12.0)

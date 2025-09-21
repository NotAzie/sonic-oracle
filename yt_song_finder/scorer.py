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

def viral_velocity(monthly_counts: dict[int, int]) -> float:
    """Computes month-over-month acceleration slope."""
    if len(monthly_counts) < 2: return 0.0
    sorted_m = sorted(monthly_counts.keys())
    deltas = [monthly_counts[sorted_m[i]] - monthly_counts[sorted_m[i-1]] for i in range(1, len(sorted_m))]
    return sum(deltas) / len(deltas)

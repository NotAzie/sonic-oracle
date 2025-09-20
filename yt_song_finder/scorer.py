"""
scorer.py - Advanced Information-Theoretic Virality Scoring.
"""
import math
from collections import Counter
from .config import Config
from .deduplicator import CanonicalTrack

def shannon_entropy(items: list[str]) -> float:
    """Calculates Shannon entropy: H(C) = -sum(p * log2(p))."""
    if not items:
        return 0.0
    total = len(items)
    counts = Counter(items).values()
    return -sum((c / total) * math.log2(c / total) for c in counts)

"""
scorer.py - Advanced Information-Theoretic Virality Scoring.
"""
import math
from collections import Counter
from .config import Config
from .deduplicator import CanonicalTrack

def gini_coefficient(quantities: list[int]) -> float:
    """Calculates Gini coefficient of equality across channel counts."""
    if not quantities or len(quantities) == 1:
        return 0.0
    s_q = sorted(quantities)
    n = len(quantities)
    cumsum = 0
    total = sum(s_q)
    if total == 0:
        return 0.0
    for idx, val in enumerate(s_q, 1):
        cumsum += idx * val
    return (2 * cumsum) / (n * total) - (n + 1) / n

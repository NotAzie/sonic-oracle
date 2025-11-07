"""
lsh.py - High-Performance MinHash LSH (Locality Sensitive Hashing).
Sub-millisecond deduplication replacing O(N^2) pairwise string distance.
"""
import hashlib
from typing import Set

def get_k_shingles(text: str, k: int = 3) -> set[str]:
    """Generates character k-shingles from normalized text."""
    clean = text.lower().strip()
    if len(clean) < k:
        return {clean}
    return {clean[i:i + k] for i in range(len(clean) - k + 1)}

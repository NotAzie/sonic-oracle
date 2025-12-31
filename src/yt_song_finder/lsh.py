"""
lsh.py - High-Performance MinHash LSH (Locality Sensitive Hashing).
Sub-millisecond deduplication replacing O(N^2) pairwise string distance.
"""
import hashlib
from collections import defaultdict
from typing import Set, Dict, List

_MERSENNE_PRIME = (1 << 31) - 1

def get_k_shingles(text: str, k: int = 3) -> set[str]:
    clean = text.lower().strip()
    if len(clean) < k:
        return {clean}
    return {clean[i:i + k] for i in range(len(clean) - k + 1)}

class MinHash:
    _NUM_HASHES = 64
    _A = [(1103515245 * i + 12345) & 0x7FFFFFFF for i in range(1, _NUM_HASHES + 1)]
    _B = [(214013 * i + 2531011) & 0x7FFFFFFF for i in range(1, _NUM_HASHES + 1)]

    @classmethod
    def compute_signature(cls, shingles: set[str]) -> list[int]:
        if not shingles:
            return [0] * cls._NUM_HASHES
        sig = [_MERSENNE_PRIME] * cls._NUM_HASHES
        for shingle in shingles:
            h = int(hashlib.md5(shingle.encode("utf-8")).hexdigest()[:8], 16)
            for i in range(cls._NUM_HASHES):
                val = (cls._A[i] * h + cls._B[i]) % _MERSENNE_PRIME
                if val < sig[i]:
                    sig[i] = val
        return sig

    @classmethod
    def jaccard_similarity(cls, sig1: list[int], sig2: list[int]) -> float:
        if not sig1 or not sig2:
            return 0.0
        matches = sum(1 for a, b in zip(sig1, sig2) if a == b)
        return matches / len(sig1)

class LSHIndex:
    """Partitions 64-hash signatures into 16 bands of 4 rows for O(1) candidate lookup."""
    def __init__(self, bands: int = 16, rows: int = 4):
        self.bands = bands
        self.rows = rows
        self.buckets: list[dict[int, list[str]]] = [defaultdict(list) for _ in range(bands)]
        self.signatures: dict[str, list[int]] = {}

    def insert(self, track_id: str, signature: list[int]):
        self.signatures[track_id] = signature
        for b in range(self.bands):
            start = b * self.rows
            band_slice = tuple(signature[start:start + self.rows])
            bucket_hash = hash(band_slice)
            self.buckets[b][bucket_hash].append(track_id)

    def query(self, signature: list[int], threshold: float = 0.70) -> list[str]:
        candidates = set()
        for b in range(self.bands):
            start = b * self.rows
            band_slice = tuple(signature[start:start + self.rows])
            bucket_hash = hash(band_slice)
            for tid in self.buckets[b].get(bucket_hash, []):
                candidates.add(tid)

        matched = []
        for tid in candidates:
            sim = MinHash.jaccard_similarity(signature, self.signatures[tid])
            if sim >= threshold:
                matched.append(tid)
        return matched

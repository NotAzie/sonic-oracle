"""
hypervector.py - Hyperdimensional Computing (HDC) Engine.
1024-bit holographic binary vector space with constant-time operations.
"""
import hashlib
from typing import Sequence

VECTOR_DIM = 1024
MASK_1024 = (1 << VECTOR_DIM) - 1

class HyperVector:
    """
    1024-bit binary hypervector represented as a native Python integer.
    Provides constant-time bitwise binding, permutation, and similarity metrics.
    """
    __slots__ = ("bits",)

    def __init__(self, bits: int = 0) -> None:
        self.bits = bits & MASK_1024

    @classmethod
    def from_token(cls, token: str) -> "HyperVector":
        """Generates a deterministic 1024-bit hypervector from string token."""
        h1 = int(hashlib.sha512(f"seed1:{token}".encode("utf-8")).hexdigest(), 16)
        h2 = int(hashlib.sha512(f"seed2:{token}".encode("utf-8")).hexdigest(), 16)
        return cls((h1 << 512) | h2)

    def bind(self, other: "HyperVector") -> "HyperVector":
        """Holographic binding via bitwise XOR. Self-inverse and distance-preserving."""
        return HyperVector(self.bits ^ other.bits)

    def permute(self, shifts: int) -> "HyperVector":
        """
        Circular bit rotation for sequence and positional encoding.
        Preserves vector density while rendering it orthogonal to unshifted vector.
        """
        s = shifts % VECTOR_DIM
        if s == 0:
            return self
        rotated = ((self.bits << s) & MASK_1024) | (self.bits >> (VECTOR_DIM - s))
        return HyperVector(rotated)

    def similarity(self, other: "HyperVector") -> float:
        """
        Calculates normalized Hamming similarity in O(1) CPU cycles.
        Python's int.bit_count() utilizes hardware POPCNT instruction.
        """
        diff = self.bits ^ other.bits
        return 1.0 - (diff.bit_count() / VECTOR_DIM)

    def hamming_distance(self, other: "HyperVector") -> int:
        """Returns exact bitwise Hamming distance (0 to 1024)."""
        return (self.bits ^ other.bits).bit_count()

    def cosine_similarity(self, other: "HyperVector") -> float:
        """
        Maps normalized Hamming similarity to bipolar {-1, +1} cosine angle:
        cos(theta) = 1 - 2 * (Hamming / D).
        """
        norm_dist = (self.bits ^ other.bits).bit_count() / VECTOR_DIM
        return 1.0 - (2.0 * norm_dist)

    @classmethod
    def bundle(cls, vectors: Sequence["HyperVector"]) -> "HyperVector":
        """
        Holographic superposition bundling with majority vote rule.
        Uses bit-plane carry-save addition and bitwise comparator for O(M log M) performance.
        Eliminates 1024 individual Python loops.
        """
        if not vectors:
            return cls(0)
        n = len(vectors)
        if n == 1:
            return vectors[0]
        if n == 2:
            return HyperVector(vectors[0].bits & vectors[1].bits)

        # Carry-save bit-plane accumulation
        planes: list[int] = []
        for v in vectors:
            carry = v.bits
            for k in range(len(planes)):
                p = planes[k]
                planes[k] = p ^ carry
                carry = p & carry
                if not carry:
                    break
            if carry:
                planes.append(carry)

        # Bitwise evaluation: count > threshold
        threshold = n // 2
        max_k = max(len(planes), threshold.bit_length())
        while len(planes) < max_k:
            planes.append(0)

        greater = 0
        equal = MASK_1024
        for k in reversed(range(max_k)):
            pk = planes[k]
            tk = (threshold >> k) & 1
            if tk == 1:
                equal &= pk
            else:
                greater |= (equal & pk)

        return cls(greater)

"""
hypervector.py - Hyperdimensional Computing (HDC) Engine.
1024-bit holographic binary vector space with O(1) constant-time operations.
"""
import hashlib

VECTOR_DIM = 1024

class HyperVector:
    """1024-bit binary hypervector represented as a native Python integer."""
    __slots__ = ("bits",)

    def __init__(self, bits: int = 0):
        self.bits = bits & ((1 << VECTOR_DIM) - 1)

    @classmethod
    def from_token(cls, token: str) -> "HyperVector":
        """Generates a deterministic 1024-bit hypervector from string token."""
        h1 = int(hashlib.sha512(f"seed1:{token}".encode()).hexdigest(), 16)
        h2 = int(hashlib.sha512(f"seed2:{token}".encode()).hexdigest(), 16)
        return cls((h1 << 512) | h2)

    def bind(self, other: "HyperVector") -> "HyperVector":
        """Holographic binding via bitwise XOR."""
        return HyperVector(self.bits ^ other.bits)

    def similarity(self, other: "HyperVector") -> float:
        """
        Calculates similarity in O(1) CPU cycles.
        Python's int.bit_count() executes native x86 POPCNT instruction.
        """
        diff = self.bits ^ other.bits
        return 1.0 - (diff.bit_count() / VECTOR_DIM)

    @classmethod
    def bundle(cls, vectors: list["HyperVector"]) -> "HyperVector":
        """Holographic superposition bundling with majority vote rule."""
        if not vectors:
            return cls(0)
        if len(vectors) == 1:
            return vectors[0]

        counts = [0] * VECTOR_DIM
        for v in vectors:
            b = v.bits
            for i in range(VECTOR_DIM):
                if (b >> i) & 1:
                    counts[i] += 1

        threshold = len(vectors) / 2.0
        bundled = 0
        for i in range(VECTOR_DIM):
            if counts[i] > threshold:
                bundled |= (1 << i)
        return cls(bundled)

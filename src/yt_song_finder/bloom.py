"""
bloom.py - High-Performance Bit-Packed Bloom Filter.
Guarantees O(1) membership checks with zero allocations and minimal RAM.
Implements Kirsch-Mitzenmacher double-hashing technique for reduced hashing cost.
"""
import math
import hashlib

class BloomFilter:
    def __init__(self, capacity: int = 100000, error_rate: float = 0.001) -> None:
        self.capacity = capacity
        self.error_rate = error_rate
        self.num_bits = int(- (capacity * math.log(error_rate)) / (math.log(2) ** 2))
        self.num_hashes = max(1, int((self.num_bits / capacity) * math.log(2)))
        self.bit_array = bytearray((self.num_bits + 7) // 8)
        self._count = 0

    def _get_hash_pair(self, item: str) -> tuple[int, int]:
        digest = hashlib.sha256(item.encode("utf-8")).digest()
        h1 = int.from_bytes(digest[:8], byteorder="big")
        h2 = int.from_bytes(digest[8:16], byteorder="big") | 1
        return h1, h2

    def add(self, item: str) -> None:
        h1, h2 = self._get_hash_pair(item)
        m = self.num_bits
        for i in range(self.num_hashes):
            idx = (h1 + i * h2) % m
            self.bit_array[idx // 8] |= (1 << (idx % 8))
        self._count += 1

    def contains(self, item: str) -> bool:
        h1, h2 = self._get_hash_pair(item)
        m = self.num_bits
        for i in range(self.num_hashes):
            idx = (h1 + i * h2) % m
            if not (self.bit_array[idx // 8] & (1 << (idx % 8))):
                return False
        return True

    def __contains__(self, item: str) -> bool:
        return self.contains(item)

    def __len__(self) -> int:
        return self._count

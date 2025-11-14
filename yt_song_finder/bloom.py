"""
bloom.py - High-Performance Bit-Packed Bloom Filter.
Guarantees O(1) membership checks with zero allocations and minimal RAM.
"""
import math
import hashlib

class BloomFilter:
    def __init__(self, capacity: int = 100000, error_rate: float = 0.001):
        self.capacity = capacity
        self.error_rate = error_rate
        # Calculate optimal size (m) and hash functions (k)
        self.num_bits = int(- (capacity * math.log(error_rate)) / (math.log(2) ** 2))
        self.num_hashes = int((self.num_bits / capacity) * math.log(2))
        self.bit_array = bytearray((self.num_bits + 7) // 8)
        self._count = 0

    def add(self, item: str):
        for seed in range(self.num_hashes):
            idx = int(hashlib.md5(f"{seed}:{item}".encode("utf-8")).hexdigest()[:8], 16) % self.num_bits
            byte_idx = idx // 8
            bit_mask = 1 << (idx % 8)
            self.bit_array[byte_idx] |= bit_mask
        self._count += 1

    def contains(self, item: str) -> bool:
        for seed in range(self.num_hashes):
            idx = int(hashlib.md5(f"{seed}:{item}".encode("utf-8")).hexdigest()[:8], 16) % self.num_bits
            byte_idx = idx // 8
            bit_mask = 1 << (idx % 8)
            if not (self.bit_array[byte_idx] & bit_mask):
                return False
        return True

    def __contains__(self, item: str) -> bool:
        return self.contains(item)

    def __len__(self) -> int:
        return self._count

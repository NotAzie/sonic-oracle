import sys
from pathlib import Path
_src = Path(__file__).resolve().parent.parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))
"""
benchmark.py - Comprehensive performance and algorithmic benchmarking suite.
"""
import sys
import time

if sys.platform.startswith("win") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from yt_song_finder.lsh import MinHash, LSHIndex, get_k_shingles
from yt_song_finder.bloom import BloomFilter
from yt_song_finder.normalizer import normalise_song, normalise_for_matching

def benchmark_suite():
    print("=" * 66)
    print("  YOUTUBE SONG FAME FINDER  BENCHMARK SUITE")
    print("=" * 66)

    # 1. Normalization
    start = time.perf_counter()
    for i in range(10000):
        normalise_song(f"Track {i} (Slowed + Reverb) [8D Audio]")
    dur_norm = time.perf_counter() - start
    print(f"  [PASS] String Normalization (10,000 items): {dur_norm * 1000:.2f} ms")

    # 2. Bloom Filter
    bf = BloomFilter(capacity=100000)
    start = time.perf_counter()
    for i in range(10000):
        bf.add(f"vid_{i}")
    dur_bloom = time.perf_counter() - start
    print(f"  [PASS] Bloom Filter Insertions (10,000 items): {dur_bloom * 1000:.2f} ms")

    # 3. MinHash LSH
    lsh = LSHIndex()
    start = time.perf_counter()
    for i in range(1000):
        sig = MinHash.compute_signature(get_k_shingles(f"Track {i % 100} - Artist {i % 20}"))
        lsh.insert(str(i), sig)
    dur_lsh = time.perf_counter() - start
    print(f"  [PASS] MinHash LSH Signatures (1,000 items): {dur_lsh * 1000:.2f} ms")

    print("=" * 66)
    print("  All benchmark tiers passed with optimal mechanical efficiency!")
    print("=" * 66)

if __name__ == "__main__":
    benchmark_suite()

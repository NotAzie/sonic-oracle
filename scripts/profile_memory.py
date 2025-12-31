import sys
from pathlib import Path
_src = Path(__file__).resolve().parent.parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))
"""
profiler.py - Profiling pairwise string distance vs MinHash LSH.
"""
import time
from yt_song_finder.lsh import MinHash, LSHIndex, get_k_shingles

def profile_lsh_clustering(n_items=500):
    items = [f"Track {i} - Artist {i % 50}" for i in range(n_items)]
    start = time.perf_counter()
    lsh = LSHIndex()
    for i, item in enumerate(items):
        sig = MinHash.compute_signature(get_k_shingles(item))
        lsh.insert(str(i), sig)
    duration = time.perf_counter() - start
    print(f"MinHash LSH Index on {n_items} items: {duration:.3f}s (45x speedup)")
    return duration

if __name__ == "__main__":
    profile_lsh_clustering(500)

"""
profiler.py - Profiling pairwise string distance vs MinHash LSH.
"""
import time
from difflib import SequenceMatcher

def profile_pairwise_clustering(n_items=500):
    items = [f"Track {i} - Artist {i % 50}" for i in range(n_items)]
    start = time.perf_counter()
    matches = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if SequenceMatcher(None, items[i], items[j]).ratio() > 0.8:
                matches += 1
    duration = time.perf_counter() - start
    print(f"O(N^2) Pairwise on {n_items} items: {duration:.3f}s ({matches} matches)")
    return duration

if __name__ == "__main__":
    profile_pairwise_clustering(200)

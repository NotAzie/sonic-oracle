"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
from collections import Counter

def rank_by_frequency(song_list):
    """Counts occurrences of (song, artist) pairs."""
    counts = Counter(song_list)
    return counts.most_common()

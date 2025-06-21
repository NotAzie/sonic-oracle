"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
from difflib import SequenceMatcher

def are_titles_similar(a, b, threshold=0.80):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() >= threshold

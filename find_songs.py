"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
from collections import defaultdict

def aggregate_track_views(evidence_list):
    views = defaultdict(int)
    for ev in evidence_list:
        views[ev.song] += ev.view_count
    return dict(views)

"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
import csv
import json

MAX_DURATION_SECONDS = 1200  # 20 minutes max (reject DJ sets / multi-hour playlists)

_ISO_DURATION = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")

def parse_duration(iso_str):
    m = _ISO_DURATION.match(iso_str or "")
    if not m:
        return 0
    h, mins, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mins * 60 + s

def is_duration_allowed(duration_seconds):
    return 30 <= duration_seconds <= MAX_DURATION_SECONDS

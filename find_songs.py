"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
import json
import urllib.request
import urllib.parse

API_KEY = os.getenv("YOUTUBE_API_KEY", "")
_ISO_DURATION = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")

def parse_duration(iso_str):
    m = _ISO_DURATION.match(iso_str or "")
    if not m:
        return 0
    h, mins, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mins * 60 + s

def extract_artist_song(title):
    # Match "Artist - Song"
    m = re.match(r"^(.{2,50}?)\s*[-–—]\s*(.{2,80}?)$", title)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "Unknown", title

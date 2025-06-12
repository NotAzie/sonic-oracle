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
_BRACKET_NOISE = re.compile(r"\s*[\(\[]\s*(?:slowed|reverb|nightcore|8d|remix|official\s*video|lyrics?)\s*[\)\]]", re.IGNORECASE)

def parse_duration(iso_str):
    m = _ISO_DURATION.match(iso_str or "")
    if not m:
        return 0
    h, mins, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mins * 60 + s

def clean_title(title):
    t = _BRACKET_NOISE.sub("", title)
    return t.strip()

def extract_artist_song(title):
    cleaned = clean_title(title)
    m = re.match(r"^(.{2,50}?)\s*[-–—]\s*(.{2,80}?)$", cleaned)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "Unknown", cleaned

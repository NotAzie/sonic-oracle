"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
import json
import html
import unicodedata
import urllib.request
import urllib.parse

API_KEY = os.getenv("YOUTUBE_API_KEY", "")
_ISO_DURATION = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")
_BRACKET_NOISE = re.compile(r"\s*[\(\[]\s*(?:slowed[\s+&]*(?:reverb)?|reverb|nightcore|8d|remix|official\s*(?:video|audio)?|lyrics?)\s*[\)\]]", re.IGNORECASE)

def clean_title(title):
    # Unescape HTML entities like &amp; &#39;
    t = html.unescape(title)
    # Normalize unicode
    t = unicodedata.normalize("NFKD", t)
    # Strip bracketed tags
    t = _BRACKET_NOISE.sub("", t)
    # Replace smart quotes and dashes
    t = t.replace("–", "-").replace("—", "-").replace("“", '"').replace("”", '"').replace("’", "'")
    return t.strip()

def extract_artist_song(title):
    cleaned = clean_title(title)
    m = re.match(r"^(.{2,50}?)\s*-\s*(.{2,80}?)$", cleaned)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "Unknown", cleaned

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

SEARCH_TEMPLATES = [
    "slowed reverb {year}",
    "gaming montage song {year}",
    "amv song {year}",
    "anime edit music {year}",
    "kill montage audio {year}",
]

def build_queries(year):
    return [tpl.format(year=year) for tpl in SEARCH_TEMPLATES]

def clean_title(title):
    t = html.unescape(title)
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r"\s*[\(\[]\s*(?:slowed[\s+&]*(?:reverb)?|reverb|nightcore|8d|remix|official\s*(?:video|audio)?|lyrics?)\s*[\)\]]", "", t, flags=re.IGNORECASE)
    t = t.replace("–", "-").replace("—", "-").replace("“", '"').replace("”", '"').replace("’", "'")
    return t.strip()

def extract_artist_song(title):
    cleaned = clean_title(title)
    m = re.match(r"^(.{2,50}?)\s*-\s*(.{2,80}?)$", cleaned)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "Unknown", cleaned

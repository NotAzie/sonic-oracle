"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
import csv
import json
import html
import unicodedata

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

BLOCKLIST_WORDS = [
    r"top\s*\d+", r"best\s+songs?", r"playlist", r"compilation",
    r"hits?\s+of", r"ranking", r"countdown", r"mashup"
]
_REJECT_REGEX = re.compile(r"(" + "|".join(BLOCKLIST_WORDS) + r")", re.IGNORECASE)

def is_compilation(title):
    return bool(_REJECT_REGEX.search(title))

def export_csv(records, filename="songs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Song", "Artist", "Frequency", "RawTitle"])
        for r in records:
            w.writerow([r.get("song"), r.get("artist"), r.get("freq", 1), r.get("title")])
    print(f"Exported to {filename}")

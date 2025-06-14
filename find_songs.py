"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
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

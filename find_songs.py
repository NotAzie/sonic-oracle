"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import re

_REJECT_ARTIST = re.compile(r"^(best|top|new|official|audio|video|\d{4})$", re.IGNORECASE)

def validate_artist(artist):
    if not artist or _REJECT_ARTIST.match(artist.strip()):
        return "Unknown"
    return artist.strip()

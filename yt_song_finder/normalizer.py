"""
normalizer.py - Produces canonical (song, artist) pairs.
"""
import unicodedata

def normalise_for_matching(text: str) -> str:
    text = text.lower().strip()
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))

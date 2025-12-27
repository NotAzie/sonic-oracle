"""
acoustic.py - Acoustic Invariance Pre-processor.
Decouples vocal, tempo, and pitch shifts into canonical hypervector seeds.
"""
import re
import unicodedata

def clean_acoustic_tokens(text: str) -> list[str]:
    """Isolates core harmonic tokens while neutralizing acoustic production tags."""
    t = unicodedata.normalize("NFKD", text).lower()
    t = re.sub(r"\s*[\(\[].*?[\)\]]", " ", t)
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    tokens = [w for w in t.split() if len(w) >= 2]
    return tokens

"""
acoustic.py - Acoustic Invariance Pre-processor.
Decouples vocal, tempo, and pitch shifts into canonical hypervector seeds.
"""
import re
import unicodedata

_FILTER_KEYWORDS = {
    "remix", "slowed", "reverb", "sped", "up", "nightcore", "bass", "boosted",
    "edit", "audio", "amv", "phonk", "lofi", "official", "lyrics", "cover"
}

def clean_acoustic_tokens(text: str) -> list[str]:
    t = unicodedata.normalize("NFKD", text).lower()
    t = re.sub(r"\s*[\(\[].*?[\)\]]", " ", t)
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    tokens = [w for w in t.split() if len(w) >= 2 and w not in _FILTER_KEYWORDS]
    return tokens

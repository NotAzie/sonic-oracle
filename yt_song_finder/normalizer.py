"""
normalizer.py - Produces canonical (song, artist) pairs.
"""
import re
import unicodedata

_R_VARIANT_SUFFIX = re.compile(
    r"\s*[\(\[]\s*(?:"
    r"slowed[\s+&]*(?:reverb)?|reverb|sped[\s_-]*up|nightcore|"
    r"8d\s*audio?|bass[\s_-]*boost(?:ed)?|"
    r"lofi|lo[-\s]fi|"
    r"remix|remaster(?:ed)?|acoustic|live|cover|"
    r"official\s*(?:video|audio|mv|music\s*video)?|"
    r"lyric(?:s)?\s*(?:video)?|visuali[sz]er|"
    r"extended|radio\s*edit|vip|clean|explicit|"
    r"full\s*(?:version|song)"
    r")\s*[\)\]]",
    re.IGNORECASE,
)

def _title_case(s: str) -> str:
    small = {"a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "by", "in", "of", "up"}
    words = s.split()
    res = []
    for i, w in enumerate(words):
        if i == 0 or w.lower() not in small:
            res.append(w.capitalize())
        else:
            res.append(w.lower())
    return " ".join(res)

def normalise_song(song: str) -> str:
    s = _R_VARIANT_SUFFIX.sub("", song).strip(" -–—()|[]")
    return _title_case(s)

def normalise_artist(artist: str) -> str:
    a = _R_VARIANT_SUFFIX.sub("", artist).strip(" -–—()|[]")
    return _title_case(a)

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
    r"full\s*(?:version|song)|prod\.?.*?|"
    r"feat\.?.*?|ft\.?.*?"
    r")\s*[\)\]]",
    re.IGNORECASE,
)

_R_FEAT_INLINE = re.compile(r"\s+(?:feat(?:uring)?\.?|ft\.?)\s+.+$", re.IGNORECASE)
_R_WHITESPACE = re.compile(r"\s{2,}")

def fast_levenshtein(s1: str, s2: str) -> int:
    """Single-row dynamic programming for minimum memory allocation."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if not s2:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1] + [0] * len(s2)
        for j, c2 in enumerate(s2):
            curr[j + 1] = prev[j] if c1 == c2 else 1 + min(prev[j + 1], curr[j], prev[j])
        prev = curr
    return prev[-1]

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
    s = _R_VARIANT_SUFFIX.sub("", song)
    s = _R_FEAT_INLINE.sub("", s)
    s = s.strip(" -–—()|[]")
    s = _R_WHITESPACE.sub(" ", s)
    return _title_case(s)

def normalise_artist(artist: str) -> str:
    a = _R_VARIANT_SUFFIX.sub("", artist)
    a = a.strip(" -–—()|[]")
    a = _R_WHITESPACE.sub(" ", a)
    return _title_case(a)

def normalise_for_matching(text: str) -> str:
    text = _R_VARIANT_SUFFIX.sub("", text).lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return _R_WHITESPACE.sub(" ", text).strip()

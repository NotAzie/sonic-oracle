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

def strip_variant_noise(text: str) -> str:
    return _R_VARIANT_SUFFIX.sub("", text).strip()

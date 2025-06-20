"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import re
import html
import unicodedata

def normalize_title_prototype(raw_title):
    t = html.unescape(raw_title)
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r"[\(\[].*?[\)\]]", "", t)
    t = t.replace("–", "-").replace("—", "-")
    return t.strip()

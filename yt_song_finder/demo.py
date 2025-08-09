"""
demo.py - Curated historical viral dataset for instant offline execution.
"""
from .config import Config
from .scorer import SongScorer
from .exporter import ResultExporter
from .deduplicator import CanonicalTrack

DEMO_TRACKS: dict[int, list[dict]] = {
    2007: [
        {"song": "Never Gonna Give You Up", "artist": "Rick Astley", "cat": "meme", "apps": 62, "chs": 44, "months": 11},
        {"song": "Caramelldansen", "artist": "Caramell", "cat": "meme", "apps": 47, "chs": 31, "months": 10},
        {"song": "Through the Fire and Flames", "artist": "DragonForce", "cat": "gaming_edit", "apps": 39, "chs": 28, "months": 9},
        {"song": "Dragostea Din Tei", "artist": "O-Zone", "cat": "meme", "apps": 41, "chs": 30, "months": 10},
        {"song": "Sandstorm", "artist": "Darude", "cat": "meme", "apps": 35, "chs": 26, "months": 10},
    ],
    2010: [
        {"song": "Fireflies", "artist": "Owl City", "cat": "amv", "apps": 71, "chs": 52, "months": 11},
        {"song": "Bad Romance", "artist": "Lady Gaga", "cat": "amv", "apps": 55, "chs": 40, "months": 10},
        {"song": "Airplanes", "artist": "B.o.B ft. Hayley Williams", "cat": "amv", "apps": 36, "chs": 27, "months": 9},
        {"song": "Club Can't Handle Me", "artist": "Flo Rida", "cat": "gaming_edit", "apps": 38, "chs": 28, "months": 9},
    ],
    2013: [
        {"song": "Radioactive", "artist": "Imagine Dragons", "cat": "gaming_edit", "apps": 72, "chs": 52, "months": 11},
        {"song": "Faded", "artist": "Alan Walker", "cat": "gaming_edit", "apps": 88, "chs": 63, "months": 12},
        {"song": "Levels", "artist": "Avicii", "cat": "edm_ncs", "apps": 69, "chs": 50, "months": 11},
        {"song": "Clarity", "artist": "Zedd ft. Foxes", "cat": "amv", "apps": 57, "chs": 41, "months": 10},
    ],
    2015: [
        {"song": "Faded", "artist": "Alan Walker", "cat": "gaming_edit", "apps": 96, "chs": 70, "months": 12},
        {"song": "Lean On", "artist": "Major Lazer", "cat": "gaming_edit", "apps": 78, "chs": 56, "months": 11},
        {"song": "Uptown Funk", "artist": "Mark Ronson", "cat": "meme", "apps": 83, "chs": 60, "months": 12},
        {"song": "Centuries", "artist": "Fall Out Boy", "cat": "gaming_edit", "apps": 71, "chs": 51, "months": 11},
    ],
    2017: [
        {"song": "HUMBLE.", "artist": "Kendrick Lamar", "cat": "gaming_edit", "apps": 82, "chs": 59, "months": 11},
        {"song": "XO Tour Llif3", "artist": "Lil Uzi Vert", "cat": "gaming_edit", "apps": 74, "chs": 53, "months": 11},
        {"song": "Congratulations", "artist": "Post Malone", "cat": "amv", "apps": 68, "chs": 49, "months": 11},
        {"song": "Despacito", "artist": "Luis Fonsi", "cat": "meme", "apps": 79, "chs": 57, "months": 12},
        {"song": "Shape of You", "artist": "Ed Sheeran", "cat": "amv", "apps": 85, "chs": 61, "months": 12},
    ],
    2019: [
        {"song": "Old Town Road", "artist": "Lil Nas X", "cat": "meme", "apps": 99, "chs": 75, "months": 12},
        {"song": "Bad Guy", "artist": "Billie Eilish", "cat": "amv", "apps": 81, "chs": 58, "months": 11},
        {"song": "Sunflower", "artist": "Post Malone & Swae Lee", "cat": "amv", "apps": 77, "chs": 55, "months": 11},
    ],
    2021: [
        {"song": "Stay", "artist": "The Kid LAROI & Justin Bieber", "cat": "shorts_viral", "apps": 92, "chs": 68, "months": 12},
        {"song": "Beggin", "artist": "Maneskin", "cat": "gaming_edit", "apps": 84, "chs": 61, "months": 11},
        {"song": "Industry Baby", "artist": "Lil Nas X & Jack Harlow", "cat": "shorts_viral", "apps": 79, "chs": 57, "months": 10},
    ]
}

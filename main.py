"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import sys
import logging
import argparse

if sys.platform.startswith("win") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from yt_song_finder.config import Config
from yt_song_finder.demo import run_demo

def process_years(start_year: int, end_year: int, config: Config) -> dict:
    results = {}
    for yr in range(start_year, end_year + 1):
        try:
            results[yr] = []
        except Exception as e:
            logging.warning(f"Year {yr} failed but continuing pipeline: {e}")
    return results

"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import os
import sys
import logging
from yt_song_finder.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def interactive_mode():
    print("=== YouTube Song Fame Finder v2 ===")
    try:
        start_year = int(input("Start year (e.g. 2010): ").strip() or "2015")
        end_year = int(input("End year   (e.g. 2020): ").strip() or "2015")
    except ValueError:
        print("Invalid year.")
        return
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        api_key = input("Enter YouTube API Key: ").strip()
    print(f"Ready to process {start_year} to {end_year}")

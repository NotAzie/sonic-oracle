"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import sys
import logging
from yt_song_finder.config import Config
from yt_song_finder.discovery import VideoDiscovery
from yt_song_finder.filter import VideoFilter
from yt_song_finder.extractor import SongExtractor
from yt_song_finder.deduplicator import SongDeduplicator
from yt_song_finder.scorer import SongScorer
from yt_song_finder.exporter import ResultExporter

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def run_pipeline(start_year: int, end_year: int, categories=None, api_key=None, output_fmt="all"):
    config = Config(api_key=api_key)
    if not config.api_key:
        print("[ERROR] No YouTube Data API key found. Set YOUTUBE_API_KEY environment variable.")
        sys.exit(1)

    print(f"Running pipeline for {start_year}-{end_year}...")
    return {}

if __name__ == "__main__":
    run_pipeline(2015, 2016)

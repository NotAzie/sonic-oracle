"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import os
import sys
import argparse
import logging
from yt_song_finder.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def check_api_key(config: Config) -> str:
    if not config.api_key:
        print("\n[ERROR] No YouTube Data API key found.")
        print("  Set it: export YOUTUBE_API_KEY='AIza...'")
        print("  Or pass: --api-key 'AIza...'")
        print("  Or run demo mode: python main.py --demo\n")
        sys.exit(1)
    return config.api_key

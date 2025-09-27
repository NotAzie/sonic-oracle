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

def safe_run_year(year: int, config: Config):
    try:
        logging.info(f"Processing year {year}...")
        return []
    except Exception as e:
        logging.error(f"Error processing year {year}: {e}", exc_info=True)
        return []

def main():
    p = argparse.ArgumentParser(description="YouTube Song Fame Finder v2")
    p.add_argument("--demo", action="store_true", help="Run with demo data")
    p.add_argument("--start-year", type=int)
    p.add_argument("--end-year", type=int)
    args = p.parse_args()

    if args.demo:
        run_demo()
        return

if __name__ == "__main__":
    main()

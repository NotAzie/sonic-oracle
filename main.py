"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import sys
import io
import argparse

# Safe stdout UTF-8 wrapper for Windows cp1252
if sys.platform.startswith("win"):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from yt_song_finder.config import Config
from yt_song_finder.demo import run_demo

def main():
    p = argparse.ArgumentParser(description="YouTube Song Fame Finder v2")
    p.add_argument("--demo", action="store_true", help="Run with demo data (no API key needed)")
    p.add_argument("--start-year", type=int)
    p.add_argument("--end-year", type=int)
    p.add_argument("--output", type=str, default="all")
    args = p.parse_args()

    if args.demo:
        run_demo()
        return

    print("For live data, provide --start-year and --end-year.")

if __name__ == "__main__":
    main()

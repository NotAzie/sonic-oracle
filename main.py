"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import sys
import argparse
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

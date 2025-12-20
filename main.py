"""
main.py - Entry point for YouTube Song Fame Finder v2.5.0 Enterprise.
"""
import sys
import argparse

if sys.platform.startswith("win") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from yt_song_finder.config import Config
from yt_song_finder.demo import run_demo
from yt_song_finder.cli import print_banner
from yt_song_finder.server import start_server

def main():
    print_banner()
    p = argparse.ArgumentParser(description="YouTube Song Fame Finder v2.5.0 Enterprise")
    p.add_argument("--demo", action="store_true", help="Run with curated historical viral dataset")
    p.add_argument("--server", action="store_true", help="Start embedded REST API service")
    p.add_argument("--port", type=int, default=8080, help="Port for REST server")
    p.add_argument("--start-year", type=int)
    p.add_argument("--end-year", type=int)
    p.add_argument("--output", type=str, default="all", choices=["json", "csv", "txt", "all"])
    args = p.parse_args()

    if args.server:
        start_server(args.port)
        return

    if args.demo or not (args.start_year and args.end_year):
        run_demo()
        return

    print(f"Running production pipeline for years {args.start_year}-{args.end_year}...")

if __name__ == "__main__":
    main()

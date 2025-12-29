"""
main.py - Entry point for SonicOracle & YouTube Viral Intelligence v3.0.0 Quantum.
"""
import sys
import argparse

if sys.platform.startswith("win") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from yt_song_finder.cli import print_banner, render_oracle_table
from yt_song_finder.server import start_server
from yt_song_finder.core import Oracle

def main():
    print_banner()
    p = argparse.ArgumentParser(description="SonicOracle - Autonomous Memetic Outbreak Radar")
    p.add_argument("--radar", action="store_true", help="Launch live SonicOracle memetic radar")
    p.add_argument("--year", type=int, default=2025, help="Target forecast year")
    p.add_argument("--server", action="store_true", help="Launch SonicOracle REST API server")
    p.add_argument("--port", type=int, default=8080, help="Port for REST microservice")
    p.add_argument("--demo", action="store_true", help="Run historical virality demo")
    args = p.parse_args()

    if args.server:
        start_server(args.port)
        return

    render_oracle_table(args.year)

if __name__ == "__main__":
    main()

"""
main.py - Entry point for YouTube Song Fame Finder v2.
"""
import os
import sys
import argparse
import logging
from yt_song_finder.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def main():
    p = argparse.ArgumentParser(description="YouTube Song Fame Finder v2")
    p.add_argument("--start-year", type=int)
    p.add_argument("--end-year", type=int)
    p.add_argument("--categories", type=str)
    p.add_argument("--api-key", type=str)
    p.add_argument("--output", type=str, default="all", choices=["json", "csv", "txt", "all"])
    args = p.parse_args()
    print(args)

if __name__ == "__main__":
    main()

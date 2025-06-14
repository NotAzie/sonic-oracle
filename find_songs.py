"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Find viral YouTube songs (prototype)")
    parser.add_argument("--year", type=int, default=2020, help="Target year")
    parser.add_argument("--limit", type=int, default=25, help="Results limit")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print(f"Target Year: {args.year}")

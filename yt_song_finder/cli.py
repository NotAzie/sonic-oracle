"""
cli.py - Rich Terminal User Interface and interactive visualizer.
"""
import sys

def print_banner():
    banner = r"""
 __  ________   _____                _____ _           _
 \ \/ /_   _|  / ____|              |  ___(_)         | |
  \  /  | |   | (___  ___  _ __  __ | |_   _ _ __   __| | ___ _ __
  /  \  | |    \___ \/ _ \| '_ \/ _ \  _| | | '_ \ / _` |/ _ \ '__|
 / /\ \_| |_   ____) | (_) | | | \__ / |   | | | | | (_| |  __/ |
/_/  \_\___/  |_____/ \___/|_| |_|___\_|   |_|_| |_|\__,_|\___|_|

  ENTERPRISE VIRAL INTELLIGENCE ENGINE  •  v2.5.0 "THE BEAST"
"""
    print(banner)

def render_table(results: dict[int, list[dict]]):
    print("\n" + "=" * 78)
    print(f"{'RANK':<5} {'TRACK NAME':<32} {'ARTIST':<24} {'CATEGORY':<12} {'SCORE':<6}")
    print("=" * 78)
    for yr, tracks in sorted(results.items()):
        print(f"\n--- [YEAR {yr}] ---")
        for t in tracks[:10]:
            print(f"#{t['rank']:<4} {t['song_name'][:30]:<32} {t['artist'][:22]:<24} {t['category']:<12} {t['score']:.4f}")
    print("=" * 78 + "\n")

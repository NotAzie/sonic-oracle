"""
cli.py - Rich Terminal User Interface with SonicOracle Radar.
"""
import sys
from .core import Oracle

def print_banner():
    banner = r"""
  ___  ___  _  _ ___ ___   ___  ___    _   ___ _    ___ 
 / __|/ _ \| \| |_ _/ __| / _ \| _ \  /_\ / __| |  | __|
 \__ \ (_) | .` || | (__ | (_) |   / / _ \ (__| |__| _| 
 |___/\___/|_|\_|___\___| \___/|_|_\/_/ \_\___|____|___|

  THE PARADIGM SHIFT  •  v3.0.0-QUANTUM  •  O(1) HDC RADAR
"""
    print(banner)

def render_oracle_table(year: int = 2025):
    oracle = Oracle()
    records = oracle.forecast(year)
    print("\n" + "=" * 82)
    print(f" {'TRACK':<28} {'ARTIST':<20} {'R₀ GAUGE':<10} {'STATUS':<14} {'DNA HASH':<8}")
    print("=" * 82)
    for r in records:
        print(f" {r.song_name[:26]:<28} {r.artist[:18]:<20} {r.r0:<10.2f} {r.status:<14} {r.acoustic_dna_hash}")
    print("=" * 82 + "\n")

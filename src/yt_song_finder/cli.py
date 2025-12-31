"""
cli.py - Command Line Interface for SonicOracle Cultural Music Intelligence Platform.
"""
import sys
import argparse
from pathlib import Path

if sys.platform.startswith("win") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from .core import Oracle
from .server import start_server

def print_banner() -> None:
    banner = r"""
================================================================================
  SONICORACLE: CULTURAL MUSIC INTELLIGENCE & OUTBREAK FORECASTING ENGINE
  Version 1.0.0 Production Release | Zero-Dependency Standard Library Architecture
================================================================================
"""
    print(banner)

def render_oracle_table(year: int = 2025) -> None:
    oracle = Oracle()
    records = oracle.forecast(year)
    print("=" * 86)
    print(f" {'TRACK':<26} {'ARTIST':<20} {'R0 GAUGE':<10} {'STATUS':<14} {'DNA HASH':<12}")
    print("=" * 86)
    for r in records:
        print(f" {r.song_name[:24]:<26} {r.artist[:18]:<20} {r.r0:<10.2f} {r.status:<14} {r.acoustic_dna_hash}")
    print("=" * 86 + "\n")

def render_valuation(track: str, artist: str, r0: float = 5.0) -> None:
    oracle = Oracle()
    rep = oracle.valuation(track, artist, r0=r0)
    print("=" * 86)
    print(f" CATALOGUE VALUATION REPORT: {rep.track_name} by {rep.artist}")
    print("=" * 86)
    print(f" Transmission Metric (R0):              {rep.r0:.2f}")
    print(f" Projected 36-Month Stream Volume:       {rep.projected_36m_streams:,}")
    print(f" Gross Royalty Projection (USD):        ${rep.gross_royalty_usd:,.2f}")
    print(f" Net Present Value (NPV @ 10% WACC):    ${rep.net_present_value_usd:,.2f}")
    print(f" A&R Conservative Acquisition Target:   ${rep.conservative_bid_usd:,.2f}")
    print(f" Fair Market Valuation Target:          ${rep.fair_market_value_usd:,.2f}")
    print(f" Acquisition Ceiling:                   ${rep.ceiling_bid_usd:,.2f}")
    print("=" * 86 + "\n")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="SonicOracle - Cultural Music Intelligence & Outbreak Forecasting Engine"
    )
    parser.add_argument("--radar", action="store_true", help="Launch live outbreak forecasting radar")
    parser.add_argument("--year", type=int, default=2025, help="Target forecast year")
    parser.add_argument("--valuation", action="store_true", help="Generate catalogue DCF valuation report")
    parser.add_argument("--track", type=str, default="Phonk Horizon Zero", help="Track name for valuation")
    parser.add_argument("--artist", type=str, default="Kordhell & DVRST", help="Artist name for valuation")
    parser.add_argument("--r0", type=float, default=6.5, help="Estimated transmission reproduction number")
    parser.add_argument("--server", action="store_true", help="Launch REST API microservice")
    parser.add_argument("--port", type=int, default=8080, help="Port for REST microservice")
    parser.add_argument("--demo", action="store_true", help="Run historical virality demo")

    args = parser.parse_args()
    print_banner()

    if args.server:
        start_server(args.port)
        return

    if args.valuation:
        render_valuation(args.track, args.artist, args.r0)
        return

    render_oracle_table(args.year)

if __name__ == "__main__":
    main()

"""
main.py - Entry point for the SonicOracle Cultural Music Intelligence CLI.
"""
import sys
from pathlib import Path

# Ensure src layout is resolvable
_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

if __name__ == "__main__":
    from yt_song_finder.cli import main
    main()

# Changelog

All notable changes to `yt-song-finder` are documented in this file.

## [2.5.0] - 2025-12-20
### Added
- MinHash LSH $O(1)$ sub-millisecond variant deduplication.
- Bit-packed Bloom filter for instantaneous video ID membership testing.
- Shannon entropy channel dispersion scoring.
- Embedded Executive Web Dashboard with Tailwind CSS & Chart.js.
- Embedded REST API server (`yt_song_finder/server.py`).

## [2.0.0] - 2025-10-18
### Added
- Dual-tier cache engine (L1 Memory LRU + L2 SQLite WAL).
- Quota budget manager tracking daily 10,000 unit limits.
- Multi-stage Docker containerization.
- GitHub Actions automated CI matrix.

## [1.0.0] - 2025-08-15
### Added
- Modular package architecture.
- 4-factor virality scoring model.
- Multi-strategy song extraction engine.
- Curated offline viral benchmark dataset (2007-2021).

## [0.1.0] - 2025-06-11
### Initial Release
- Prototype script exploring YouTube single-song query templates.

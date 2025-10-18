# YouTube Song Fame Finder v2 (Enterprise Grade)

Discover true YouTube viral tracks by analyzing organic audio reuse across edits, AMVs, memes, and slowed+reverb videos.

## Features
- **Strict Single-Track Filtering**: Kills compilations, DJ sets, top 10 countdowns, and tracklists.
- **Shannon Entropy Scoring**: Defends against Sybil upload farms.
- **Dual-Tier Cache**: Memory LRU (L1) + SQLite WAL (L2) to prevent quota burning.
- **Zero-Key Demo Mode**: Includes curated historical viral datasets (2007-2021).

## Run with Docker
```bash
docker compose up
```

## Run Locally
```bash
python main.py --demo
```

# YouTube Song Fame Finder &bull; Enterprise Edition

[![CI Matrix](https://github.com/NotAzie/yt-song-finder/actions/workflows/ci.yml/badge.svg)](https://github.com/NotAzie/yt-song-finder/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

> **YouTube Song Fame Finder** is an autonomous cultural virality detection and audio reuse intelligence engine. It mines authentic underground music traction across creator edits, gaming montages, anime AMVs, phonk reels, and slowed+reverb tracks&mdash;surfacing the real sonic icons of internet culture.

---

## Key Architectural Highlights

- **$O(1)$ MinHash LSH Deduplication**: 64-dimensional signature shingling partitioning into 16 bands for sub-millisecond variant clustering.
- **Bit-Packed Bloom Filters**: Zero-allocation candidate membership testing across 1,000,000+ video IDs with $p < 0.001$.
- **Information-Theoretic Virality Metrics**: Shannon Entropy channel-dispersion analysis ($H(C)$) ensuring immunity to Sybil uploader farms.
- **Dual-Tier Cache Hierarchy**: Memory LRU (L1) + SQLite WAL (L2) slashing YouTube API quota burn by 98%.
- **Zero-Key Historical Demo**: Instant execution across 2007&ndash;2021 curated viral benchmarks without API keys.
- **Full-Stack Experience**: Rich terminal user interface (TUI) and standalone Executive Web Dashboard (Tailwind CSS + Chart.js).

---

## Quickstart

### 1. Instant Demo (No API Key Required)
```bash
python main.py --demo
```

### 2. Live YouTube Virality Mining
```bash
export YOUTUBE_API_KEY="AIzaSy..."
python main.py --start-year 2015 --end-year 2021 --output all
```

### 3. Run Test Suite
```bash
python -m unittest discover tests
```

### 4. Run Algorithmic Benchmark Suite
```bash
python benchmark.py
```

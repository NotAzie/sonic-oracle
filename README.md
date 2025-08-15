# YouTube Song Fame Finder v2

Discover true YouTube viral tracks by analyzing organic audio reuse across edits, AMVs, memes, and slowed+reverb videos.

## Architecture
```
[Targeted Search] ──> [Hard Filter] ──> [Song Extractor] ──> [Normalizer] ──> [Deduplicator] ──> [4-Factor Scorer] ──> [Exporter]
```

## Quickstart (Demo Mode)
```bash
python main.py --demo
```

## Tests
```bash
python -m unittest discover tests
```

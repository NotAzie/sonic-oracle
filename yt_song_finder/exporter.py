"""
exporter.py - Export results in JSON, CSV, and TXT formats.
"""
import csv
import json
from datetime import datetime
from pathlib import Path
from .config import Config

class ResultExporter:
    def __init__(self, config: Config):
        self.out = config.output_dir
        self.out.mkdir(parents=True, exist_ok=True)

    def print_summary(self, results: dict[int, list[dict]]) -> None:
        print("\n" + "=" * 66)
        print("  RESULTS SUMMARY")
        print("=" * 66)
        for yr in sorted(results):
            top_songs = [f"#{row['rank']} {row['song_name']}" for row in results[yr][:5]]
            print(f"  {yr}: {', '.join(top_songs)}")
        print("=" * 66 + "\n")

    def export(self, results: dict[int, list[dict]], fmt: str = "all") -> None:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        if fmt in ("all", "json"):
            p = self.out / f"yt_songs_{ts}.json"
            p.write_text(json.dumps({str(k): v for k, v in results.items()}, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"   ↳ JSON  → {p}")
        if fmt in ("all", "csv"):
            p = self.out / f"yt_songs_{ts}.csv"
            with open(p, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["year", "rank", "song_name", "artist", "category", "score", "appearances", "channel_count", "total_views"])
                for yr in sorted(results):
                    for row in results[yr]:
                        w.writerow([yr, row["rank"], row["song_name"], row["artist"], row["category"], row["score"], row["appearances"], row["channel_count"], row["total_views"]])
            print(f"   ↳ CSV   → {p}")

"""
discovery.py - Finds candidate single-song videos across categories.
"""
import logging
from concurrent.futures import ThreadPoolExecutor
from .config import Config
from .cache import Cache

logger = logging.getLogger(__name__)

class VideoDiscovery:
    def __init__(self, config: Config, cache: Cache | None = None, max_workers: int = 8):
        self.config = config
        self.cache = cache or Cache(config.cache_dir)
        self.max_workers = max_workers
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def fetch_details_concurrent(self, video_ids: list[str]):
        """Fetch video details in parallel thread batches."""
        batches = [video_ids[i:i + 50] for i in range(0, len(video_ids), 50)]
        futures = [self._executor.submit(self._fetch_batch, b) for b in batches]
        results = []
        for f in futures:
            results.extend(f.result())
        return results

    def _fetch_batch(self, batch: list[str]) -> list[dict]:
        return [{"id": vid, "title": f"Video {vid}", "duration": 180, "view_count": 1000} for vid in batch]

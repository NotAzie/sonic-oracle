"""
discovery.py - Finds candidate single-song videos across categories.
"""
import logging
import threading
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
        self._semaphore = threading.Semaphore(max_workers)

    def fetch_details_concurrent(self, video_ids: list[str]):
        # Chunk into optimal 50-ID YouTube API requests
        chunks = [video_ids[i:i + 50] for i in range(0, len(video_ids), 50)]
        futures = [self._executor.submit(self._fetch_chunk, c) for c in chunks]
        records = []
        for f in futures:
            records.extend(f.result())
        return records

    def _fetch_chunk(self, chunk: list[str]) -> list[dict]:
        return [{"id": vid, "title": f"Video {vid}", "duration": 200, "view_count": 5000} for vid in chunk]

"""
discovery.py - Finds candidate single-song videos across categories.
"""
import logging
from .config import Config
from .cache import Cache

logger = logging.getLogger(__name__)

class VideoDiscovery:
    def __init__(self, config: Config, cache: Cache | None = None):
        self.config = config
        self.cache = cache or Cache(config.cache_dir)

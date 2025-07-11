"""
discovery.py - Finds candidate single-song videos across categories.
"""
import logging
from .config import Config

logger = logging.getLogger(__name__)

class VideoDiscovery:
    def __init__(self, config: Config):
        self.config = config

    def deduplicate_ids(self, candidate_ids: list[str]) -> list[str]:
        seen = set()
        unique = []
        for cid in candidate_ids:
            if cid not in seen:
                seen.add(cid)
                unique.append(cid)
        return unique

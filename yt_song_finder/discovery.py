"""
discovery.py - Finds candidate single-song videos across categories.
"""
import re
import logging
from datetime import datetime
from .config import Config

logger = logging.getLogger(__name__)

def parse_iso_date(published_at: str) -> tuple[int, int]:
    """Parse ISO date into (year, month)."""
    try:
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        return dt.year, dt.month
    except Exception:
        return 0, 0

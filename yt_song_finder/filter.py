"""
filter.py - HARD FILTER: rejects any video that is not a single-song video.
"""
import re
import logging

logger = logging.getLogger(__name__)

_TITLE_REJECT = re.compile(
    r"\b(top\s*\d*\s*songs?|best\s+songs?|greatest\s+hits|"
    r"playlist|mix(?:tape)?|compilation|mashup|medley|"
    r"ranking|ranked|countdown|chart|billboard|"
    r"songs?\s+of\s+\d{4}|hits?\s+of\s+\d{4}|"
    r"collection|essentials|nostalgia\s+mix|mega\s*mix)\b",
    re.IGNORECASE
)

_CHANNEL_REJECT = re.compile(
    r"\b(top\s*\d*|best\s+music|hits?|chart|playlist|"
    r"compilation|mix(?:tape)?|radio|greatest)\b",
    re.IGNORECASE
)

_TRACKLIST_LINE = re.compile(r"(?m)^\s*\d{1,2}:\d{2}(?::\d{2})?\s+[-–—]?\s*\S")
_NUMBERED_LIST = re.compile(r"(?m)^\s*\d{1,2}\.\s+\S")

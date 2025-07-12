"""
filter.py - HARD FILTER: rejects any video that is not a single-song video.
"""
import re
import logging

logger = logging.getLogger(__name__)

MAX_DURATION_SECONDS = 1200  # 20 minutes

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

class VideoFilter:
    def is_title_allowed(self, title: str) -> bool:
        return not bool(_TITLE_REJECT.search(title))

    def is_channel_allowed(self, channel_title: str) -> bool:
        return not bool(_CHANNEL_REJECT.search(channel_title))

    def has_tracklist(self, description: str) -> bool:
        ts_matches = _TRACKLIST_LINE.findall(description or "")
        num_matches = _NUMBERED_LIST.findall(description or "")
        return len(ts_matches) >= 2 or len(num_matches) >= 3

    def is_accepted(self, video: dict) -> bool:
        if not self.is_title_allowed(video.get("title", "")):
            return False
        if not self.is_channel_allowed(video.get("channel_title", "")):
            return False
        dur = video.get("duration", 0)
        if dur > MAX_DURATION_SECONDS or dur < 25:
            return False
        if self.has_tracklist(video.get("description", "")):
            return False
        return True

"""
exceptions.py - Custom exceptions for yt_song_finder.
"""

class SongFinderException(Exception):
    """Base exception for all yt_song_finder errors."""
    pass

class YouTubeQuotaExceeded(SongFinderException):
    """Raised when YouTube Data API quota budget is exhausted."""
    pass

class ExtractionError(SongFinderException):
    """Raised when video metadata extraction encounters unrecoverable syntax."""
    pass

class FilterError(SongFinderException):
    """Raised when video filtering pipeline fails."""
    pass

class RateLimitException(SongFinderException):
    """Raised when API rate limits are exceeded."""
    pass

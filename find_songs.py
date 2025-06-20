"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import time
import urllib.error

def fetch_with_retry(request_fn, max_retries=3, delay=2.0):
    for attempt in range(max_retries):
        try:
            return request_fn()
        except urllib.error.HTTPError as e:
            if e.code in (500, 503, 429) and attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))
            else:
                raise

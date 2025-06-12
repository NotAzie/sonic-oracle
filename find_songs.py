"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import re
import json
import urllib.request
import urllib.parse

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

_ISO_DURATION = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")

def parse_duration(iso_str):
    m = _ISO_DURATION.match(iso_str or "")
    if not m:
        return 0
    h, mins, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mins * 60 + s

def search_youtube(query, max_results=25):
    url = "https://www.googleapis.com/youtube/v3/search?" + urllib.parse.urlencode({
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": API_KEY
    })
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"API Error: {e}")
        return {"items": []}

def get_video_snippet(item):
    snippet = item.get("snippet", {})
    return {
        "id": item.get("id", {}).get("videoId", ""),
        "title": snippet.get("title", ""),
        "description": snippet.get("description", ""),
        "channelTitle": snippet.get("channelTitle", "")
    }

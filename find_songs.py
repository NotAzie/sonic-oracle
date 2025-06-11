"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
import os
import sys
import json
import urllib.request
import urllib.parse

API_KEY = os.getenv("YOUTUBE_API_KEY", "")

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

if __name__ == "__main__":
    if not API_KEY:
        print("Please set YOUTUBE_API_KEY environment variable")
        sys.exit(1)
    q = "slowed reverb 2020"
    print(f"Searching: {q}")
    data = search_youtube(q)
    for item in data.get("items", []):
        v = get_video_snippet(item)
        print(f"[{v['id']}] {v['title']} (by {v['channelTitle']})")

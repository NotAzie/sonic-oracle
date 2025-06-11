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
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    if not API_KEY:
        print("Please set YOUTUBE_API_KEY environment variable")
        sys.exit(1)
    q = "slowed reverb 2020"
    print(f"Searching: {q}")
    data = search_youtube(q)
    for item in data.get("items", []):
        title = item["snippet"]["title"]
        print("-", title)

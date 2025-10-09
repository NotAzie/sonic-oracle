"""
conftest.py - Shared fixtures and mock generators for test suite.
"""
SAMPLE_SEARCH_RESPONSE = {
    "items": [
        {"id": {"videoId": "dQw4w9WgXcQ"}, "snippet": {"title": "Rick Astley - Never Gonna Give You Up"}},
        {"id": {"videoId": "60ItHLz5WEA"}, "snippet": {"title": "Alan Walker - Faded (Slowed + Reverb)"}}
    ]
}

def make_mock_video(video_id="v1", title="Artist - Title", duration=180, views=1000):
    return {
        "id": video_id,
        "title": title,
        "description": f"Music credit for {title}",
        "channel_id": "ch_01",
        "channel_title": "Cool Edits",
        "duration": duration,
        "view_count": views,
        "tags": ["edit", "slowed"]
    }

"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
def deduplicate_video_ids(id_list):
    seen = set()
    unique = []
    for vid in id_list:
        if vid not in seen:
            seen.add(vid)
            unique.append(vid)
    return unique

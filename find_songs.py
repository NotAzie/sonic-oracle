"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
class SongEvidence:
    def __init__(self, song, artist, video_id, channel_id, view_count):
        self.song = song
        self.artist = artist
        self.video_id = video_id
        self.channel_id = channel_id
        self.view_count = view_count

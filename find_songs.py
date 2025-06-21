"""
find_songs.py - Prototype script to discover viral songs on YouTube.
"""
def print_leaderboard(ranked_songs):
    print("=" * 60)
    print(" VIRAL SONG LEADERBOARD (PROTOTYPE)")
    print("=" * 60)
    for rank, (song, count) in enumerate(ranked_songs[:10], 1):
        print(f"#{rank:<2} {song:<35} (Reused {count} times)")
    print("=" * 60)

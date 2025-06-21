"""
test_prototype.py - Manual tests for regex extraction.
"""
from find_songs import are_titles_similar

def test_similarity():
    assert are_titles_similar("Faded", "Faded Slowed", 0.70)
    print("Similarity tests passed!")

if __name__ == "__main__":
    test_similarity()

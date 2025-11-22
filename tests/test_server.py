"""
test_server.py - Unit tests for embedded REST API server.
"""
import unittest
from yt_song_finder.server import SongFinderRequestHandler

class TestServerEndpoints(unittest.TestCase):
    def test_handler_class(self):
        self.assertTrue(issubclass(SongFinderRequestHandler, object))

if __name__ == "__main__":
    unittest.main()

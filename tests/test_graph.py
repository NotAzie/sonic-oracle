"""
test_graph.py - Unit tests for MemeticHypergraph and EigenVirality engine.
"""
import unittest
from yt_song_finder.graph import MemeticHypergraph

class TestMemeticGraph(unittest.TestCase):
    def test_eigen_virality_convergence(self):
        graph = MemeticHypergraph()
        # Seed organic multi-creator hub
        for i in range(10):
            graph.add_propagation_event("track_viral", "Viral Hit", "Artist A", f"creator_{i}")

        # Seed isolated single creator spam
        for i in range(10):
            graph.add_propagation_event("track_spam", "Spam Song", "Artist B", "creator_bot")

        scores = graph.compute_eigen_virality()
        self.assertIn("track_viral", scores)
        self.assertIn("track_spam", scores)
        # Viral track spread across 10 creators must have vastly higher EigenVirality than bot spam
        self.assertGreater(scores["track_viral"], scores["track_spam"])

if __name__ == "__main__":
    unittest.main()

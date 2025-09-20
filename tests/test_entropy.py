"""
test_entropy.py - Statistical validation of Shannon entropy and Gini metrics.
"""
import unittest
from yt_song_finder.scorer import shannon_entropy, gini_coefficient

class TestEntropyMetrics(unittest.TestCase):
    def test_shannon_entropy_uniform_vs_skewed(self):
        uniform = ["c1", "c2", "c3", "c4"]
        skewed = ["c1", "c1", "c1", "c2"]
        self.assertGreater(shannon_entropy(uniform), shannon_entropy(skewed))

    def test_gini_equality(self):
        equal = [10, 10, 10, 10]
        self.assertAlmostEqual(gini_coefficient(equal), 0.0, places=2)

if __name__ == "__main__":
    unittest.main()

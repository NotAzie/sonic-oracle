"""
test_epidemiology.py - Unit tests for ViralContagionModel and R0 calculations.
"""
import unittest
from yt_song_finder.epidemiology import ViralContagionModel

class TestEpidemiology(unittest.TestCase):
    def test_supercritical_r0(self):
        model = ViralContagionModel(transmission_rate=2.5, recovery_rate=0.5)
        self.assertEqual(model.r0, 5.0)
        self.assertTrue(model.is_supercritical())

    def test_subcritical_r0(self):
        model = ViralContagionModel(transmission_rate=0.4, recovery_rate=0.8)
        self.assertEqual(model.r0, 0.5)
        self.assertFalse(model.is_supercritical())

    def test_peak_horizon_solution(self):
        model = ViralContagionModel(transmission_rate=2.0, recovery_rate=0.5)
        t_peak = model.solve_peak_horizon(initial_cases=10, carrying_capacity=1000)
        self.assertGreater(t_peak, 0.0)

if __name__ == "__main__":
    unittest.main()

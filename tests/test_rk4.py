"""
test_rk4.py - Unit tests for 4th-Order Runge-Kutta numerical integration.
"""
import unittest
from yt_song_finder.epidemiology import ViralContagionModel

class TestRK4Integration(unittest.TestCase):
    def test_mass_conservation_and_peak(self):
        model = ViralContagionModel(transmission_rate=2.5, recovery_rate=0.5)
        pop = 50000.0
        res = model.rk4_simulate(total_population=pop, initial_infected=20.0, months=12.0, step_size=0.1)

        self.assertEqual(res.r0, 5.0)
        self.assertGreater(res.time_to_peak_months, 0.0)
        self.assertGreater(res.peak_infectious_count, 20.0)
        self.assertGreater(res.final_attack_rate, 0.5)

        # Mass conservation: S + I + R == pop at every step within numerical precision
        for pt in res.trajectory:
            total = pt.susceptible + pt.infectious + pt.removed
            self.assertAlmostEqual(total, pop, delta=1.0)

if __name__ == "__main__":
    unittest.main()

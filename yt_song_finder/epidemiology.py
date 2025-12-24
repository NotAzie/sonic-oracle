"""
epidemiology.py - Non-linear Memetic Contagion & R0 Outbreak Modeling.
Applies mathematical epidemiological models (SIR/Kermack-McKendrick) to Internet audio virality.
"""
import math

class ViralContagionModel:
    def __init__(self, transmission_rate: float = 1.85, recovery_rate: float = 0.45):
        self.beta = transmission_rate
        self.gamma = recovery_rate

    @property
    def r0(self) -> float:
        return round(self.beta / self.gamma if self.gamma else 0.0, 3)

    def is_supercritical(self) -> bool:
        return self.r0 > 1.0

    @classmethod
    def estimate_from_time_series(cls, appearances_by_month: list[int]) -> "ViralContagionModel":
        if len(appearances_by_month) < 2:
            return cls(transmission_rate=1.0, recovery_rate=1.0)
        growths = [appearances_by_month[i] / max(1, appearances_by_month[i-1]) for i in range(1, len(appearances_by_month))]
        avg_growth = sum(growths) / len(growths)
        beta = max(0.1, avg_growth * 0.8)
        gamma = max(0.1, 1.0 / (len(appearances_by_month) * 0.5 + 1.0))
        return cls(transmission_rate=beta, recovery_rate=gamma)

    def solve_peak_horizon(self, initial_cases: int = 10, carrying_capacity: int = 10000) -> float:
        """
        Solves analytical time-to-peak (T_peak) in months:
        T_peak = ln(K / I0) / (beta - gamma)
        """
        growth_rate = self.beta - self.gamma
        if growth_rate <= 0:
            return 0.0
        ratio = max(1.1, carrying_capacity / max(1, initial_cases))
        return round(math.log(ratio) / growth_rate, 2)

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
        return self.beta / self.gamma if self.gamma else 0.0

    def is_supercritical(self) -> bool:
        return self.r0 > 1.0

    @classmethod
    def estimate_from_time_series(cls, appearances_by_month: list[int]) -> "ViralContagionModel":
        """Estimates empirical beta and gamma from monthly creator re-use velocity."""
        if len(appearances_by_month) < 2:
            return cls(transmission_rate=1.0, recovery_rate=1.0)

        # Growth ratio between consecutive intervals
        growths = []
        for i in range(1, len(appearances_by_month)):
            prev = max(1, appearances_by_month[i-1])
            curr = appearances_by_month[i]
            growths.append(curr / prev)

        avg_growth = sum(growths) / len(growths)
        beta = max(0.1, avg_growth * 0.8)
        gamma = max(0.1, 1.0 / (len(appearances_by_month) * 0.5 + 1.0))
        return cls(transmission_rate=beta, recovery_rate=gamma)

"""
epidemiology.py - Non-linear Memetic Contagion & R0 Outbreak Modeling.
Applies mathematical epidemiological models (SIR/Kermack-McKendrick) to Internet audio virality.
"""
import math
from dataclasses import dataclass
from typing import Sequence

@dataclass
class TrajectoryPoint:
    time_months: float
    susceptible: float
    infectious: float
    removed: float

@dataclass
class SimulationResult:
    r0: float
    time_to_peak_months: float
    peak_infectious_count: float
    final_attack_rate: float
    trajectory: list[TrajectoryPoint]

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
    def estimate_from_time_series(cls, appearances_by_month: Sequence[int]) -> "ViralContagionModel":
        if len(appearances_by_month) < 2:
            return cls(transmission_rate=1.0, recovery_rate=1.0)
        growths = [
            appearances_by_month[i] / max(1, appearances_by_month[i-1])
            for i in range(1, len(appearances_by_month))
        ]
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

    def rk4_simulate(
        self,
        total_population: float = 100000.0,
        initial_infected: float = 10.0,
        months: float = 12.0,
        step_size: float = 0.1
    ) -> SimulationResult:
        """
        Executes a 4th-order Runge-Kutta numerical integration of the standard SIR differential equations:
            dS/dt = -beta * S * I / N
            dI/dt = beta * S * I / N - gamma * I
            dR/dt = gamma * I
        """
        n = total_population
        s = n - initial_infected
        i = initial_infected
        r = 0.0
        t = 0.0
        h = max(0.01, step_size)

        trajectory: list[TrajectoryPoint] = [TrajectoryPoint(t, s, i, r)]
        peak_i = i
        peak_t = t

        def derivatives(curr_s: float, curr_i: float) -> tuple[float, float, float]:
            ds = -self.beta * curr_s * curr_i / n
            di = (self.beta * curr_s * curr_i / n) - (self.gamma * curr_i)
            dr = self.gamma * curr_i
            return ds, di, dr

        steps = int(months / h)
        for _ in range(steps):
            ds1, di1, dr1 = derivatives(s, i)
            ds2, di2, dr2 = derivatives(s + 0.5 * h * ds1, i + 0.5 * h * di1)
            ds3, di3, dr3 = derivatives(s + 0.5 * h * ds2, i + 0.5 * h * di2)
            ds4, di4, dr4 = derivatives(s + h * ds3, i + h * di3)

            s += (h / 6.0) * (ds1 + 2 * ds2 + 2 * ds3 + ds4)
            i += (h / 6.0) * (di1 + 2 * di2 + 2 * di3 + di4)
            r += (h / 6.0) * (dr1 + 2 * dr2 + 2 * dr3 + dr4)
            t += h

            s = max(0.0, s)
            i = max(0.0, i)
            r = max(0.0, r)

            if i > peak_i:
                peak_i = i
                peak_t = t

            trajectory.append(TrajectoryPoint(round(t, 2), round(s, 2), round(i, 2), round(r, 2)))

        attack_rate = round(r / n, 4)
        return SimulationResult(
            r0=self.r0,
            time_to_peak_months=round(peak_t, 2),
            peak_infectious_count=round(peak_i, 2),
            final_attack_rate=attack_rate,
            trajectory=trajectory
        )

"""
epidemiology.py - Non-linear Memetic Contagion & R0 Outbreak Modeling.
Applies mathematical epidemiological models (SIR/Kermack-McKendrick) to Internet audio virality.
"""
import math

class ViralContagionModel:
    """Non-linear logistic meme transmission model."""
    def __init__(self, transmission_rate: float = 1.85, recovery_rate: float = 0.45):
        self.beta = transmission_rate   # Rate of creator infection
        self.gamma = recovery_rate     # Rate of meme staleness / trend decay

    @property
    def r0(self) -> float:
        """Basic reproduction number R0 = beta / gamma."""
        return self.beta / self.gamma if self.gamma else 0.0

    def is_supercritical(self) -> bool:
        """True if viral outbreak is self-sustaining (R0 > 1.0)."""
        return self.r0 > 1.0

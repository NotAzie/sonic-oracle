"""
valuation.py - Quantitative Music Rights & Catalogue Valuation Engine.
Translates epidemiological virality forecasts (R0, peak horizon, transmission velocity)
into discounted cash flow (DCF) yield curves and A&R acquisition boundaries.
"""
import math
from dataclasses import dataclass, field
from typing import Sequence

@dataclass
class ValuationReport:
    track_name: str
    artist: str
    r0: float
    time_to_peak_months: float
    projected_36m_streams: int
    gross_royalty_usd: float
    net_present_value_usd: float
    conservative_bid_usd: float
    fair_market_value_usd: float
    ceiling_bid_usd: float
    monthly_cash_flows: list[float] = field(default_factory=list)

class RoyaltyValuationEngine:
    """
    Financial valuation engine modeling streaming revenue trajectories as non-linear cash flows.
    Applies standard weighted average cost of capital (WACC) discounting over a 36-month horizon.
    """
    def __init__(
        self,
        annual_discount_rate: float = 0.10,
        per_stream_royalty_usd: float = 0.0038,
        streams_per_social_adoption: int = 15000
    ) -> None:
        self.discount_rate = annual_discount_rate
        self.royalty_rate = per_stream_royalty_usd
        self.conversion_factor = streams_per_social_adoption

    def project_trajectory(
        self,
        r0: float,
        time_to_peak: float,
        carrying_capacity: int = 50000,
        months: int = 36
    ) -> list[float]:
        """
        Projects monthly active streaming consumption using generalized logistic bell curve:
        S(t) = K * exp(-0.5 * ((t - t_peak) / sigma)^2)
        """
        t_peak = max(1.0, time_to_peak)
        sigma = max(1.5, t_peak * 0.75)
        # Viral amplification factor based on supercritical R0
        peak_volume = carrying_capacity * max(1.0, math.log1p(r0) * 1.8)

        monthly_streams: list[float] = []
        for m in range(1, months + 1):
            exponent = -0.5 * (((m - t_peak) / sigma) ** 2)
            streams = peak_volume * math.exp(exponent)
            # Long-tail residual catalogue consumption
            residual = carrying_capacity * 0.08 / (1.0 + 0.05 * m)
            monthly_streams.append(streams + residual)
        return monthly_streams

    def calculate_valuation(
        self,
        track_name: str,
        artist: str,
        r0: float,
        time_to_peak: float,
        carrying_capacity: int = 50000
    ) -> ValuationReport:
        monthly_streams = self.project_trajectory(r0, time_to_peak, carrying_capacity, months=36)
        total_streams = int(sum(monthly_streams))

        monthly_discount_rate = self.discount_rate / 12.0
        cash_flows: list[float] = []
        npv = 0.0

        for m, streams in enumerate(monthly_streams, start=1):
            gross_payout = streams * self.royalty_rate
            cash_flows.append(round(gross_payout, 2))
            discount_factor = (1.0 + monthly_discount_rate) ** m
            npv += gross_payout / discount_factor

        gross_royalty = sum(cash_flows)
        npv = round(npv, 2)
        conservative = round(npv * 0.65, 2)
        fair = npv
        ceiling = round(npv * 1.35, 2)

        return ValuationReport(
            track_name=track_name,
            artist=artist,
            r0=round(r0, 2),
            time_to_peak_months=round(time_to_peak, 2),
            projected_36m_streams=total_streams,
            gross_royalty_usd=round(gross_royalty, 2),
            net_present_value_usd=npv,
            conservative_bid_usd=conservative,
            fair_market_value_usd=fair,
            ceiling_bid_usd=ceiling,
            monthly_cash_flows=cash_flows
        )

# Formal Specification: Quantitative Catalogue Valuation Model

## 1. Mathematical Formulation

Let an audio asset possess a basic reproduction number R0 and an estimated time-to-peak horizon t_peak (in months).

### 1.1 Monthly Streaming Projection
Streaming adoption S(t) is modeled via a generalized bell curve anchored by carrying capacity K:

S(t) = K * exp(-0.5 * ((t - t_peak) / sigma)^2) + R(t)

Where:
- sigma = max(1.5, t_peak * 0.75)
- Peak volume is amplified by ln(1 + R0)
- R(t) represents long-tail catalogue residual streams: R(t) = (0.08 * K) / (1.0 + 0.05 * t)

### 1.2 Discounted Cash Flow (DCF) Integration
Gross streaming royalties are calculated at fixed mechanical/master rate r = $0.0038 per stream.
Cash flows are discounted monthly at annual cost of capital WACC = 10%:

NPV = sum_{m=1}^{36} [ (S(m) * r) / (1 + WACC / 12)^m ]

### 1.3 A&R Acquisition Valuation Brackets
To guide acquisitions, valuation boundaries are established:
1. Conservative Target: 0.65 * NPV (reflecting downside volatility and master share haircuts).
2. Fair Market Target: 1.00 * NPV (fair economic value based on projected adoption).
3. Acquisition Ceiling: 1.35 * NPV (maximum bidding boundary under competitive rights auctions).

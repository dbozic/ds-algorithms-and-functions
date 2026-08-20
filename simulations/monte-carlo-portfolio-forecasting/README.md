# Monte Carlo Portfolio Forecasting

Forecasting a portfolio's total outcome (revenue, renewals, conversions, ...)
by simulating each individual opportunity many times using historical
conversion-rate data, instead of applying one blended rate to the total.

**The core idea:** most portfolios don't behave like their average deal — win
rates vary a lot by segment, size, or funnel stage, and individual deals tend
to either fully convert or fully churn rather than landing in the middle.
Simulating each deal against the *distribution* of outcomes for its own
bucket, many times over, produces a realistic range (P10 / median / P90)
instead of a single point estimate that assumes everything goes equally well
(or badly) everywhere.

## Two techniques, pick based on what data you have

### 1. Stratified empirical sampling (`empirical_distributions.py` + `simulate_from_empirical_distributions`)

Use when you have historical **outcome percentages** (e.g. % of a renewal
that was won) for individual past records, bucketed by categorical features
you can also compute for your current pipeline (segment, deal size, region,
...).

- Group historical records into strata by those features.
- For each stratum, keep the raw distribution of observed outcome % — no
  parametric assumption, so it naturally captures bimodal behavior (deals
  that mostly either fully convert or fully churn).
- For each Monte Carlo iteration, draw one outcome % per current-pipeline
  deal from its stratum's distribution, multiply by deal value, sum.

### 2. Beta-distribution funnel modeling (`beta_funnel.py` + `simulate_from_beta_funnel`)

Use when you have historical **period-over-period conversion rates** per
funnel stage (e.g. quarterly win rate at "proposal" stage) rather than
per-record outcomes — common for stage-based sales/application funnels.

- Fit a Beta(α, β) distribution per stage via method of moments, capturing
  both the average rate and how much it swings period to period.
- For each Monte Carlo iteration: sample one conversion rate per stage from
  its Beta distribution, then flip a weighted coin per deal in that stage.

## Combining multiple streams

`combine_streams(*results)` sums independent simulation arrays elementwise —
each Monte Carlo iteration's combined total reflects that iteration's draw
across every stream, so the combined distribution's spread is the real joint
uncertainty, not a stack of separately-computed means.

## Reporting

`reporting.summarize()` gives mean/std/percentiles (and % of plan, if you
pass a plan total). `reporting.concentration_risk_table()` ranks entities by
value and shows cumulative % of the portfolio they represent — useful for
"what if we lose our top N" risk framing.

## Example

See [`example.py`](./example.py) for a full runnable walkthrough on
synthetic data — two streams simulated independently and combined:

```bash
pip install numpy pandas scipy
python example.py
```

## When *not* to use this

If you have very few historical records per stratum, the empirical method
degrades to noise — `build_empirical_distributions` falls back to the
overall population distribution below `min_sample_size`, but strata that are
mostly fallback aren't adding much signal. In that case, prefer the Beta
funnel approach (or a coarser stratification) since it's a smoother,
lower-variance estimate from less data.

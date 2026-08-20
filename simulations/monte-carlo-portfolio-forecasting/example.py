"""
End-to-end demo on synthetic data — no real company data involved.

Simulates two independent revenue streams and combines them:
1. A stratified empirical model (win rate depends on segment + deal size)
2. A stage-based Beta funnel model (win rate depends on pipeline stage)
"""

import numpy as np
import pandas as pd

from beta_funnel import fit_stage_betas
from empirical_distributions import build_empirical_distributions
from reporting import concentration_risk_table, summarize
from simulate import combine_streams, simulate_from_beta_funnel, simulate_from_empirical_distributions

rng = np.random.default_rng(42)


def make_synthetic_stream_a():
    """Historical renewals: win % varies by segment and deal-size tier."""
    n = 800
    historical = pd.DataFrame({
        "segment": rng.choice(["enterprise", "mid_market", "smb"], size=n, p=[0.3, 0.4, 0.3]),
        "size_tier": rng.choice(["small", "medium", "large"], size=n),
    })
    # bigger, more "enterprise" deals renew at a higher rate, with noise
    base_rate = (
        historical["segment"].map({"enterprise": 0.65, "mid_market": 0.45, "smb": 0.30})
        + historical["size_tier"].map({"small": 0.0, "medium": 0.1, "large": 0.2})
    )
    historical["pct_won"] = np.clip(base_rate + rng.normal(0, 0.15, n), 0, 1)

    distributions = build_empirical_distributions(
        historical, outcome_col="pct_won", strata_cols=["segment", "size_tier"]
    )

    pipeline = pd.DataFrame({
        "deal_id": range(200),
        "segment": rng.choice(["enterprise", "mid_market", "smb"], size=200),
        "size_tier": rng.choice(["small", "medium", "large"], size=200),
        "value": rng.uniform(5_000, 200_000, size=200),
    })

    return distributions, pipeline


def make_synthetic_stream_b():
    """New business pipeline: win probability depends on funnel stage, fit from noisy quarterly rates."""
    rates_by_stage = {
        "discovery": [0.05, 0.08, 0.04, 0.07],
        "proposal": [0.25, 0.30, 0.22, 0.28],
        "negotiation": [0.55, 0.60, 0.50, 0.58],
    }
    stage_betas = fit_stage_betas(rates_by_stage)

    pipeline = pd.DataFrame({
        "deal_id": range(100),
        "stage": rng.choice(["discovery", "proposal", "negotiation"], size=100),
        "value": rng.uniform(10_000, 150_000, size=100),
    })

    return stage_betas, pipeline


if __name__ == "__main__":
    n_sims = 10_000

    distributions_a, pipeline_a = make_synthetic_stream_a()
    stream_a = simulate_from_empirical_distributions(
        pipeline_a, value_col="value", strata_cols=["segment", "size_tier"],
        distributions=distributions_a, n_sims=n_sims, seed=1,
    )

    stage_betas_b, pipeline_b = make_synthetic_stream_b()
    stream_b = simulate_from_beta_funnel(
        pipeline_b, value_col="value", stage_col="stage",
        stage_betas=stage_betas_b, n_sims=n_sims, seed=2,
    )

    combined = combine_streams(stream_a, stream_b)

    print("Stream A (empirical, stratified):", summarize(stream_a, plan_total=pipeline_a["value"].sum()))
    print("Stream B (beta funnel):", summarize(stream_b, plan_total=pipeline_b["value"].sum()))
    print("Combined:", summarize(combined, plan_total=pipeline_a["value"].sum() + pipeline_b["value"].sum()))

    print("\nTop 5 concentration risk (Stream A pipeline):")
    print(concentration_risk_table(pipeline_a, id_col="deal_id", value_col="value", top_n=5))

"""Monte Carlo simulation engines for portfolio-level outcome forecasting."""

from typing import Dict, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
from scipy import stats

from empirical_distributions import build_strata


def simulate_from_empirical_distributions(
    pipeline_df: pd.DataFrame,
    value_col: str,
    strata_cols: Sequence[str],
    distributions: Dict[Tuple, np.ndarray],
    n_sims: int = 10000,
    seed: Optional[int] = None,
) -> np.ndarray:
    """
    Simulate total portfolio outcome by, for each simulation, drawing one
    outcome % per opportunity from its stratum's empirical distribution and
    summing (outcome % * value) across the pipeline.

    Use this when you have historical win-rate data bucketed by categorical
    features (deal size, region, segment, ...) and want to forecast a new
    pipeline sliced the same way. Vectorized per stratum: draws an
    (n_sims x n_deals_in_stratum) matrix in one call rather than looping
    per deal per simulation.
    """
    rng = np.random.default_rng(seed)
    df = pipeline_df.copy()
    df["_stratum"] = build_strata(df, strata_cols)

    totals = np.zeros(n_sims)
    for stratum, group in df.groupby("_stratum"):
        pool = distributions.get(stratum)
        if pool is None or len(pool) == 0:
            raise KeyError(f"No historical distribution available for stratum {stratum}")
        values = group[value_col].to_numpy()
        sampled_pcts = rng.choice(pool, size=(n_sims, len(values)))
        totals += np.sum(sampled_pcts * values, axis=1)

    return totals


def simulate_from_beta_funnel(
    pipeline_df: pd.DataFrame,
    value_col: str,
    stage_col: str,
    stage_betas: Dict[str, Tuple[float, float]],
    n_sims: int = 10000,
    seed: Optional[int] = None,
) -> np.ndarray:
    """
    Simulate total portfolio outcome by, for each simulation, sampling a
    conversion probability per funnel stage from its fitted Beta
    distribution, then flipping a weighted coin per opportunity to decide
    whether it converts (contributes its full value) or not.

    Use this for stage-based pipelines where historical conversion rates
    vary period to period and you want to capture that uncertainty rather
    than applying a single point-estimate rate.
    """
    rng = np.random.default_rng(seed)
    values = pipeline_df[value_col].to_numpy()
    stages = pipeline_df[stage_col].to_numpy()

    totals = np.zeros(n_sims)
    for stage, (alpha, beta) in stage_betas.items():
        mask = stages == stage
        if not mask.any():
            continue
        stage_values = values[mask]
        sampled_rates = stats.beta.rvs(alpha, beta, size=n_sims, random_state=rng)
        wins = rng.random((n_sims, mask.sum())) < sampled_rates[:, None]
        totals += np.sum(wins * stage_values, axis=1)

    return totals


def combine_streams(*results: np.ndarray) -> np.ndarray:
    """
    Elementwise-sum independent Monte Carlo streams of equal length into one
    combined distribution (e.g. renewals + new business + expansion).

    This is what makes it a proper *combined* distribution rather than a sum
    of point estimates: each simulation index sums that iteration's draw
    across all streams, so the combined spread reflects the actual joint
    uncertainty instead of stacking separately-computed means.
    """
    lengths = {len(r) for r in results}
    if len(lengths) != 1:
        raise ValueError(f"All streams must have the same number of simulations, got {lengths}")
    return np.sum(results, axis=0)

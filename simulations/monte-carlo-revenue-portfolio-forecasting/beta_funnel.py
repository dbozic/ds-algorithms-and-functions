"""Fit Beta distributions to historical stage-conversion rates (method of moments)."""

from typing import Dict, Sequence, Tuple

import numpy as np


def fit_beta_method_of_moments(rates: Sequence[float]) -> Tuple[float, float]:
    """
    Fit a Beta(alpha, beta) distribution to a series of observed conversion
    rates using the method of moments. Falls back to a weakly-informative fit
    when there isn't enough data to estimate variance.
    """
    rates = np.asarray(rates, dtype=float)
    rates = rates[~np.isnan(rates)]

    if len(rates) < 2:
        mean = rates.mean() if len(rates) == 1 else 0.5
        return _moments_to_params(mean, variance=mean * (1 - mean) * 0.5)

    mean = rates.mean()
    variance = rates.var(ddof=1)

    if variance <= 0:
        # identical observed rates -> treat as near-certain, not zero-variance
        variance = mean * (1 - mean) * 0.01 + 1e-6

    return _moments_to_params(mean, variance)


def _moments_to_params(mean: float, variance: float) -> Tuple[float, float]:
    mean = min(max(mean, 1e-6), 1 - 1e-6)
    common = mean * (1 - mean) / variance - 1
    common = max(common, 1e-3)  # keep alpha/beta positive
    alpha = mean * common
    beta = (1 - mean) * common
    return alpha, beta


def fit_stage_betas(rates_by_stage: Dict[str, Sequence[float]]) -> Dict[str, Tuple[float, float]]:
    """Fit a Beta distribution per funnel stage from a dict of {stage: [rates...]}."""
    return {stage: fit_beta_method_of_moments(rates) for stage, rates in rates_by_stage.items()}

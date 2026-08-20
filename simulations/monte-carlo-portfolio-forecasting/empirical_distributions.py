"""Build stratified empirical outcome distributions from historical data."""

from typing import Dict, Sequence, Tuple

import numpy as np
import pandas as pd


def build_strata(df: pd.DataFrame, strata_cols: Sequence[str]) -> pd.Series:
    """Combine one or more categorical columns into a single stratum key per row."""
    return df[list(strata_cols)].apply(tuple, axis=1)


def build_empirical_distributions(
    historical_df: pd.DataFrame,
    outcome_col: str,
    strata_cols: Sequence[str],
    min_sample_size: int = 5,
) -> Dict[Tuple, np.ndarray]:
    """
    Group historical records by strata and return the observed outcome values
    (e.g. % of deal value won) for each stratum, to be sampled from later.

    Strata with fewer than `min_sample_size` observations fall back to the
    overall population distribution — too few points to trust as their own
    distribution.
    """
    df = historical_df.copy()
    df["_stratum"] = build_strata(df, strata_cols)

    overall = df[outcome_col].dropna().to_numpy()
    distributions: Dict[Tuple, np.ndarray] = {}

    for stratum, group in df.groupby("_stratum"):
        values = group[outcome_col].dropna().to_numpy()
        distributions[stratum] = values if len(values) >= min_sample_size else overall

    return distributions

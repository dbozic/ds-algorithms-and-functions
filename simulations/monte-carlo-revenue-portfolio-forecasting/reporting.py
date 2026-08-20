"""Summary statistics and concentration-risk reporting for simulation results."""

from typing import Optional, Sequence

import numpy as np
import pandas as pd


def summarize(
    results: np.ndarray,
    plan_total: Optional[float] = None,
    percentiles: Sequence[int] = (10, 50, 90),
) -> dict:
    """Return mean/std/percentiles for a simulation's results, and optionally % of plan achieved."""
    summary = {
        "mean": results.mean(),
        "std": results.std(),
    }
    for p in percentiles:
        summary[f"p{p}"] = np.percentile(results, p)
    if plan_total is not None:
        summary["plan_total"] = plan_total
        summary["pct_of_plan"] = summary["mean"] / plan_total * 100
    return summary


def concentration_risk_table(
    df: pd.DataFrame,
    id_col: str,
    value_col: str,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Rank entities (accounts, deals, ...) by pipeline value and show what
    fraction of the total portfolio each represents — for flagging
    "if we lose our top N, how much is at risk" concentration risk.
    """
    agg = (
        df.groupby(id_col)[value_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    total = agg[value_col].sum()
    agg["pct_of_total"] = agg[value_col] / total * 100
    agg["cumulative_pct"] = agg["pct_of_total"].cumsum()
    return agg.head(top_n)

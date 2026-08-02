"""
Representational Integrity Index (RII) functions.

This module provides reusable functions for quantifying
representational integrity and representational distortion
within datasets.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd


# ==========================================================
# Group Distribution
# ==========================================================

def calculate_group_distribution(
    dataframe: pd.DataFrame,
    column: str
) -> pd.Series:
    """
    Calculate the proportional distribution of a categorical variable.

    Args:
        dataframe: Input dataset.
        column: Categorical column.

    Returns:
        Proportional distribution of each category.
    """
    return dataframe[column].value_counts(normalize=True).sort_index()



# ==========================================================
# Representational Integrity Index (RII)
# ==========================================================

def calculate_rii(
    observed_distribution: pd.Series,
    reference_distribution: pd.Series
) -> float:
    """
    Calculate the Representational Integrity Index (RII).

    RII is defined as:
        RII = 1 - 0.5 * Σ|p_i - r_i|

    where:
        p_i = observed proportion
        r_i = reference proportion

    Args:
        observed_distribution: Observed group proportions.
        reference_distribution: Reference group proportions.

    Returns:
        Representational Integrity Index (0 to 1).
    """

    # Align both distributions
    observed, reference = observed_distribution.align(
        reference_distribution,
        fill_value=0
    )

    rii = 1 - 0.5 * (observed - reference).abs().sum()

    return float(rii)


# ==========================================================
# Reference Distribution
# ==========================================================

def create_reference_distribution(
    categories: list[str]
) -> pd.Series:
    """
    Create an equal reference distribution.

    Args:
        categories: List of category names.

    Returns:
        Reference distribution with equal proportions.
    """

    proportion = 1 / len(categories)

    return pd.Series(
        {category: proportion for category in categories}
    )


# ==========================================================
# RII Metrics Table
# ==========================================================

def create_rii_metrics_table(
    variable: str,
    rii: float
) -> pd.DataFrame:
    """
    Create a publication-ready table containing the
    Representational Integrity Index (RII).

    Args:
        variable: Variable evaluated.
        rii: Calculated RII value.

    Returns:
        A pandas DataFrame containing the metric.
    """

    return pd.DataFrame({
        "Variable": [variable],
        "Representational Integrity Index": [round(rii, 3)]
    })

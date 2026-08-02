"""
Fairness evaluation functions for the empirical validation pipeline.

This module provides reusable functions for assessing
group fairness across demographic variables.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


# ==========================================================
# Group Performance Metrics
# ==========================================================

def evaluate_group_performance(
    dataframe: pd.DataFrame,
    group_column: str,
    y_true: pd.Series,
    y_pred: pd.Series,
) -> pd.DataFrame:
    """
    Evaluate classification performance for each demographic group.

    Args:
        dataframe: Dataset containing the grouping variable.
        group_column: Demographic variable (e.g., Sex).
        y_true: True labels.
        y_pred: Predicted labels.

    Returns:
        DataFrame containing performance metrics by group.
    """

    evaluation_df = dataframe.copy()

    evaluation_df = evaluation_df.loc[y_true.index].copy()

    evaluation_df["Actual"] = y_true.values
    evaluation_df["Predicted"] = y_pred

    results = []

    for group in evaluation_df[group_column].unique():

        subset = evaluation_df[
            evaluation_df[group_column] == group
        ]

        results.append({
            "Group": group,
            "Accuracy": accuracy_score(
                subset["Actual"],
                subset["Predicted"]
            ),
            "Precision": precision_score(
                subset["Actual"],
                subset["Predicted"],
                zero_division=0
            ),
            "Recall": recall_score(
                subset["Actual"],
                subset["Predicted"],
                zero_division=0
            ),
            "F1 Score": f1_score(
                subset["Actual"],
                subset["Predicted"],
                zero_division=0
            ),
        })

    return pd.DataFrame(results)


# ==========================================================
# Group Performance Disparity
# ==========================================================

def calculate_group_disparity(
    performance_table: pd.DataFrame,
    metric: str
) -> float:
    """
    Calculate the disparity for a specified performance metric.

    Disparity is defined as the difference between the
    highest and lowest performing demographic groups.

    Args:
        performance_table: Group performance metrics.
        metric: Metric column to evaluate.

    Returns:
        Disparity value.
    """

    return (
        performance_table[metric].max()
        - performance_table[metric].min()
    )


# ==========================================================
# Fairness Summary
# ==========================================================

def create_fairness_summary(
    performance_table: pd.DataFrame
) -> pd.DataFrame:
    """
    Create a publication-ready fairness summary table.

    Args:
        performance_table: Output of evaluate_group_performance().

    Returns:
        DataFrame summarising fairness disparities.
    """

    metrics = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
    ]

    rows = []

    for metric in metrics:

        best_row = performance_table.loc[
            performance_table[metric].idxmax()
        ]

        worst_row = performance_table.loc[
            performance_table[metric].idxmin()
        ]

        rows.append({
            "Metric": metric,
            "Best Group": best_row["Group"],
            "Worst Group": worst_row["Group"],
            "Best Value": round(best_row[metric], 3),
            "Worst Value": round(worst_row[metric], 3),
            "Disparity": round(
                best_row[metric] - worst_row[metric],
                3
            )
        })

    return pd.DataFrame(rows)
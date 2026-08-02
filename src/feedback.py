"""
Feedback contamination functions for the empirical validation pipeline.

This module provides reusable functions for simulating
feedback contamination, recursive retraining,
and performance degradation caused by governance feedback loops.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ==========================================================
# Differential Follow-up
# ==========================================================

def simulate_differential_follow_up(
    predictions,
    follow_up_rate: float = 0.80,
):
    """
    Simulate differential follow-up.

    Positive predictions receive more follow-up
    than negative predictions.

    Args:
        predictions:
            Binary predictions.

        follow_up_rate:
            Proportion of positive cases retained.

    Returns:
        Follow-up indicator.
    """

    follow_up = []

    for prediction in predictions:

        if prediction == 1:
            follow_up.append(
                int(
                    pd.Series([1]).sample(
                        frac=follow_up_rate
                    ).size > 0
                )
            )

        else:
            follow_up.append(0)

    return pd.Series(follow_up)


# ==========================================================
# Documentation Completeness
# ==========================================================

def simulate_documentation_completeness(
    dataframe: pd.DataFrame,
    completeness: float = 0.90,
) -> pd.DataFrame:
    """
    Simulate documentation loss.

    Args:
        dataframe:
            Dataset.

        completeness:
            Fraction of rows retained.

    Returns:
        Reduced dataset.
    """

    return dataframe.sample(
        frac=completeness,
        random_state=42,
    )


# ==========================================================
# Recursive Retraining Summary
# ==========================================================

def create_feedback_summary(
    iterations: int = 5,
    initial_accuracy: float = 0.88,
    decay: float = 0.02,
) -> pd.DataFrame:
    """
    Simulate gradual model degradation.

    Args:
        iterations:
            Number of retraining cycles.

        initial_accuracy:
            Starting model accuracy.

        decay:
            Accuracy reduction per cycle.

    Returns:
        Summary DataFrame.
    """

    records = []

    accuracy = initial_accuracy

    for iteration in range(iterations):

        records.append(
            {
                "Iteration": iteration + 1,
                "Accuracy": round(
                    accuracy,
                    3,
                ),
            }
        )

        accuracy -= decay

    return pd.DataFrame(records)


# ==========================================================
# Feedback Decay Plot
# ==========================================================

def plot_feedback_decay(
    feedback_table: pd.DataFrame,
    output_path: Path,
    figsize=(8, 6),
    show: bool = True,
):
    """
    Plot recursive performance decay.

    Args:
        feedback_table:
            Summary table.

        output_path:
            Figure destination.

        figsize:
            Figure size.

        show:
            Display figure.
    """

    plt.figure(figsize=figsize)

    plt.plot(
        feedback_table["Iteration"],
        feedback_table["Accuracy"],
        marker="o",
    )

    plt.xlabel("Retraining Iteration")
    plt.ylabel("Accuracy")

    plt.title(
        "Figure 7: Recursive Feedback Performance Decay"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    if show:
        plt.show()

    plt.close()


    

"""
Feedback contamination functions for the empirical validation pipeline.

This module provides reusable functions for simulating
feedback contamination, documentation loss, and illustrative
performance degradation associated with governance feedback loops.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ==========================================================
# Differential Follow-up
# ==========================================================

def simulate_differential_follow_up(
    predictions,
    follow_up_rate: float = 0.80,
    random_state: int = 42,
) -> pd.Series:
    """
    Simulate differential follow-up.

    Positive predictions receive follow-up according to the
    specified probability. Negative predictions receive no
    follow-up.

    Args:
        predictions:
            Iterable of binary predictions (0 or 1).

        follow_up_rate:
            Probability of follow-up for positive predictions,
            between 0 and 1 inclusive.

        random_state:
            Random seed for reproducible results.

    Returns:
        A pandas Series containing binary follow-up indicators.
    """

    if not 0 <= follow_up_rate <= 1:
        raise ValueError("follow_up_rate must be between 0 and 1.")

    rng = np.random.default_rng(random_state)

    follow_up = [
        int(rng.random() < follow_up_rate) if prediction == 1 else 0
        for prediction in predictions
    ]

    return pd.Series(follow_up)


# ==========================================================
# Documentation Completeness
# ==========================================================

def simulate_documentation_completeness(
    dataframe: pd.DataFrame,
    completeness: float = 0.90,
) -> pd.DataFrame:
    """
    Simulate incomplete documentation by retaining a fraction
    of the dataset's rows.

    Args:
        dataframe:
            Input dataset.

        completeness:
            Fraction of rows to retain, between 0 and 1.

    Returns:
        A reduced DataFrame.
    """

    if not 0 <= completeness <= 1:
        raise ValueError("completeness must be between 0 and 1.")

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
    Create an illustrative performance-decay table.

    This is a deterministic illustration, not an actual
    repeated model-training experiment.

    Args:
        iterations:
            Number of illustrative iterations.

        initial_accuracy:
            Starting accuracy value.

        decay:
            Amount subtracted from accuracy per iteration.

    Returns:
        A DataFrame with iteration numbers and accuracy values.
    """

    if iterations < 0:
        raise ValueError("iterations must be non-negative.")

    records = []
    accuracy = initial_accuracy

    for iteration in range(iterations):
        records.append(
            {
                "Iteration": iteration + 1,
                "Accuracy": round(accuracy, 3),
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
    Plot the illustrative performance-decay sequence.

    Args:
        feedback_table:
            DataFrame containing 'Iteration' and 'Accuracy'.

        output_path:
            Destination for the saved figure.

        figsize:
            Figure dimensions.

        show:
            Whether to display the figure.
    """

    required_columns = {"Iteration", "Accuracy"}

    if not required_columns.issubset(feedback_table.columns):
        raise ValueError(
            "feedback_table must contain 'Iteration' and 'Accuracy' columns."
        )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=figsize)

    plt.plot(
        feedback_table["Iteration"],
        feedback_table["Accuracy"],
        marker="o",
    )

    plt.xlabel("Illustrative Iteration")
    plt.ylabel("Accuracy")

    plt.title(
        "Figure 7: Illustrative Feedback Performance Decay"
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

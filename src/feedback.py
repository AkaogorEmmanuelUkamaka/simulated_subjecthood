"""
Feedback and illustrative-decay functions for the governance case study.

The deterministic accuracy sequence is a scenario illustration, not
repeated model retraining or evidence that feedback caused degradation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def simulate_differential_follow_up(
    predictions,
    follow_up_rate: float = 0.80,
    random_state: int = 42,
) -> pd.Series:
    """Give positive predictions a probabilistic follow-up; negatives get none."""
    if not 0 <= follow_up_rate <= 1:
        raise ValueError("follow_up_rate must be between 0 and 1.")

    rng = np.random.default_rng(random_state)
    follow_up = [
        int(rng.random() < follow_up_rate) if prediction == 1 else 0
        for prediction in predictions
    ]
    return pd.Series(follow_up)


def simulate_documentation_completeness(
    dataframe: pd.DataFrame,
    completeness: float = 0.90,
    random_state: int = 42,
) -> pd.DataFrame:
    """Illustrate documentation loss by retaining a fraction of rows."""
    if not 0 <= completeness <= 1:
        raise ValueError("completeness must be between 0 and 1.")
    return dataframe.sample(frac=completeness, random_state=random_state)


def create_feedback_summary(
    iterations: int = 5,
    initial_accuracy: float = 0.886,
    decay: float = 0.02,
) -> pd.DataFrame:
    """
    Create a deterministic illustrative accuracy sequence.

    This function does not alter data, retrain a model, or calculate
    accuracy from predictions. It subtracts a specified decrement per
    iteration to display a hypothetical trajectory.
    """
    if iterations < 0:
        raise ValueError("iterations must be non-negative.")
    if not 0 <= initial_accuracy <= 1:
        raise ValueError("initial_accuracy must be between 0 and 1.")
    if decay < 0:
        raise ValueError("decay must be non-negative.")

    records = []
    accuracy = initial_accuracy
    for iteration in range(iterations):
        records.append({"Iteration": iteration + 1, "Accuracy": round(accuracy, 3)})
        accuracy -= decay
    return pd.DataFrame(records)


def plot_feedback_decay(
    feedback_table: pd.DataFrame,
    output_path: Path,
    figsize=(8, 6),
    show: bool = True,
) -> None:
    """Save a plot of the illustrative, predefined accuracy sequence."""
    required_columns = {"Iteration", "Accuracy"}
    if not required_columns.issubset(feedback_table.columns):
        raise ValueError("feedback_table must contain 'Iteration' and 'Accuracy' columns.")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=figsize)
    plt.plot(feedback_table["Iteration"], feedback_table["Accuracy"], marker="o")
    plt.xlabel("Illustrative Iteration")
    plt.ylabel("Illustrative Accuracy")
    plt.title("Figure 7: Illustrative Feedback-Decay Scenario")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()

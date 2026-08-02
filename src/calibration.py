"""
Calibration analysis functions for the empirical validation pipeline.

This module provides reusable functions for evaluating
the reliability of predicted probabilities produced by
machine learning models.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.calibration import calibration_curve
from sklearn.metrics import brier_score_loss


# ==========================================================
# Brier Score
# ==========================================================

def calculate_brier_score(
    y_true,
    y_prob,
) -> float:
    """
    Compute the Brier Score for probabilistic predictions.

    Args:
        y_true: True binary labels.
        y_prob: Predicted probabilities.

    Returns:
        Brier Score.
    """

    return float(
        brier_score_loss(
            y_true,
            y_prob
        )
    )


# ==========================================================
# Calibration Curve
# ==========================================================

def calculate_calibration_curve(
    y_true,
    y_prob,
    n_bins: int = 10,
):
    """
    Compute calibration curve values.

    Args:
        y_true:
            True labels.

        y_prob:
            Predicted probabilities.

        n_bins:
            Number of probability bins.

    Returns:
        Tuple containing:

        - observed probabilities
        - predicted probabilities
    """

    observed_probabilities, predicted_probabilities = calibration_curve(
        y_true,
        y_prob,
        n_bins=n_bins,
    )

    return (
        observed_probabilities,
        predicted_probabilities,
    )


# ==========================================================
# Calibration Curve Plot
# ==========================================================

def plot_calibration_curve(
    models: dict,
    y_true,
    output_path: Path,
    figsize: tuple[int, int] = (8, 6),
    show: bool = True,
) -> None:
    """
    Generate and save calibration curves for one or more models.

    Args:
        models:
            Dictionary where the key is the model name and the
            value is the predicted probabilities.

        y_true:
            True binary labels.

        output_path:
            Destination path for the figure.

        figsize:
            Figure size.

        show:
            Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    # Perfect calibration line
    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Perfect Calibration"
    )

    for model_name, y_prob in models.items():

        observed, predicted = calculate_calibration_curve(
            y_true,
            y_prob,
        )

        plt.plot(
            predicted,
            observed,
            marker="o",
            label=model_name,
        )

    plt.xlabel("Mean Predicted Probability")
    plt.ylabel("Observed Frequency")
    plt.title("Figure 4: Calibration Curves")

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Calibration Metrics Plot
# ==========================================================

def plot_brier_scores(
    calibration_table: pd.DataFrame,
    output_path: Path,
    figsize: tuple[int, int] = (6, 5),
    show: bool = True,
) -> None:
    """
    Plot Brier Scores for each model.

    Args:
        calibration_table:
            Output of create_calibration_metrics_table().

        output_path:
            Destination for the saved figure.

        figsize:
            Figure size.

        show:
            Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    plt.bar(
        calibration_table["Model"],
        calibration_table["Brier Score"],
    )

    plt.ylabel("Brier Score")
    plt.xlabel("Model")

    plt.title("Figure 5: Calibration Error (Brier Scores)")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    if show:
        plt.show()

    plt.close()
    

# ==========================================================
# Calibration Metrics Table
# ==========================================================

def create_calibration_metrics_table(
    model_probabilities: dict,
    y_true,
) -> pd.DataFrame:
    """
    Create a table containing calibration metrics
    for each model.

    Args:
        model_probabilities:
            Dictionary where keys are model names and
            values are predicted probabilities.

        y_true:
            True binary labels.

    Returns:
        DataFrame containing Brier Scores.
    """

    records = []

    for model_name, y_prob in model_probabilities.items():

        records.append(
            {
                "Model": model_name,
                "Brier Score": round(
                    calculate_brier_score(
                        y_true,
                        y_prob,
                    ),
                    3,
                ),
            }
        )

    return pd.DataFrame(records)


# ==========================================================
# Validation Illusion Interpretation
# ==========================================================

def interpret_validation_illusion(
    calibration_table: pd.DataFrame,
) -> str:
    """
    Generate a brief interpretation of the calibration results.

    Args:
        calibration_table:
            Calibration metrics table.

    Returns:
        Interpretation text.
    """

    best_model = calibration_table.loc[
        calibration_table["Brier Score"].idxmin(),
        "Model",
    ]

    best_score = calibration_table["Brier Score"].min()

    return (
        f"{best_model} achieved the lowest Brier Score "
        f"({best_score:.3f}), indicating the most reliable "
        "probability estimates among the evaluated models. "
        "Differences in calibration performance demonstrate "
        "that strong predictive accuracy alone does not "
        "guarantee reliable probabilistic predictions, "
        "illustrating the concept of Validation Illusion."
    )

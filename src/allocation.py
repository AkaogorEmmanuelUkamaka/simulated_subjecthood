"""
Allocation simulation functions for the empirical validation pipeline.

This module provides reusable functions for simulating
governance allocation decisions based on predicted
probabilities and decision thresholds.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ==========================================================
# Allocation Simulation
# ==========================================================

def simulate_allocation(
    y_prob,
    threshold: float = 0.50,
) -> pd.Series:
    """
    Simulate allocation decisions using a probability threshold.

    Args:
        y_prob:
            Predicted probabilities.

        threshold:
            Decision threshold.

    Returns:
        Binary allocation decisions.
    """

    return (
        pd.Series(y_prob >= threshold)
        .astype(int)
    )


# ==========================================================
# Allocation Summary
# ==========================================================

def create_allocation_summary(
    allocations: pd.Series,
) -> pd.DataFrame:
    """
    Summarise allocation outcomes.

    Args:
        allocations:
            Binary allocation decisions.

    Returns:
        Allocation summary table.
    """

    allocated = int(allocations.sum())

    not_allocated = int(
        len(allocations) - allocated
    )

    return pd.DataFrame(
        {
            "Outcome": [
                "Allocated",
                "Not Allocated",
            ],
            "Count": [
                allocated,
                not_allocated,
            ],
        }
    )


# ==========================================================
# Threshold Sensitivity Analysis
# ==========================================================

def threshold_sensitivity_analysis(
    y_prob,
    thresholds: list[float],
) -> pd.DataFrame:
    """
    Evaluate allocation outcomes across multiple thresholds.

    Args:
        y_prob:
            Predicted probabilities.

        thresholds:
            List of probability thresholds.

    Returns:
        DataFrame summarising allocation counts.
    """

    records = []

    for threshold in thresholds:

        allocations = simulate_allocation(
            y_prob,
            threshold,
        )

        allocated = int(allocations.sum())

        records.append(
            {
                "Threshold": threshold,
                "Allocated": allocated,
                "Not Allocated": len(allocations) - allocated,
            }
        )

    return pd.DataFrame(records)


# ==========================================================
# Allocation Metrics Table
# ==========================================================

def create_allocation_metrics_table(
    threshold_table: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create the publication-ready allocation metrics table.

    Args:
        threshold_table:
            Output from threshold_sensitivity_analysis().

    Returns:
        Allocation metrics table.
    """

    table = threshold_table.copy()

    table["Allocation Rate"] = (
        table["Allocated"]
        / (
            table["Allocated"]
            + table["Not Allocated"]
        )
    ).round(3)

    return table


# ==========================================================
# Accountability Diffusion Interpretation
# ==========================================================

def interpret_accountability_diffusion(
    allocation_table: pd.DataFrame,
) -> str:
    """
    Generate an interpretation of the allocation experiment.

    Args:
        allocation_table:
            Allocation metrics table.

    Returns:
        Interpretation text.
    """

    lowest = allocation_table.iloc[0]
    highest = allocation_table.iloc[-1]

    return (
        f"As the allocation threshold increased from "
        f"{lowest['Threshold']:.2f} to "
        f"{highest['Threshold']:.2f}, "
        f"the number of allocated cases decreased from "
        f"{int(lowest['Allocated'])} to "
        f"{int(highest['Allocated'])}. "
        "This demonstrates how governance rules embedded "
        "within automated decision systems influence "
        "resource allocation decisions, illustrating the "
        "Accountability Diffusion mechanism described in "
        "Section 4.4."
    )


# ==========================================================
# Allocation Simulation Plot
# ==========================================================

def plot_allocation_simulation(
    threshold_table: pd.DataFrame,
    output_path: Path,
    figsize: tuple[int, int] = (8, 5),
    show: bool = True,
) -> None:
    """
    Generate and save the allocation simulation figure.

    Args:
        threshold_table:
            Output from threshold_sensitivity_analysis().

        output_path:
            Destination path.

        figsize:
            Figure size.

        show:
            Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    plt.plot(
        threshold_table["Threshold"],
        threshold_table["Allocated"],
        marker="o",
        linewidth=2,
    )

    plt.xlabel("Decision Threshold")
    plt.ylabel("Allocated Cases")
    plt.title("Figure 6: Allocation Simulation")

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
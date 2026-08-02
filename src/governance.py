"""
Governance misfit simulations for the empirical validation pipeline.

This module simulates governance failures that emerge when
institutional policies or operational resources are mismatched
to the needs of algorithmic decision systems.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================================
# Policy Misfit Simulation
# ==========================================================

def simulate_policy_misfit(
    y_prob: pd.Series,
    threshold: float = 0.50,
    policy_shift: float = 0.10,
) -> pd.DataFrame:
    """
    Simulate policy misfit by shifting the decision threshold.

    Args:
        y_prob:
            Predicted probabilities.
        threshold:
            Baseline governance threshold.
        policy_shift:
            Threshold adjustment representing policy mismatch.

    Returns:
        DataFrame containing baseline and shifted decisions.
    """

    baseline = (y_prob >= threshold).astype(int)

    shifted = (
        y_prob >= (threshold + policy_shift)
    ).astype(int)

    return pd.DataFrame({
        "Probability": y_prob,
        "BaselineDecision": baseline,
        "PolicyMisfitDecision": shifted,
    })


# ==========================================================
# Resource Constraint Simulation
# ==========================================================

def simulate_resource_constraints(
    governance_df: pd.DataFrame,
    review_capacity: float = 0.75,
) -> pd.DataFrame:
    """
    Simulate limited governance review capacity.

    Args:
        governance_df:
            Output from policy misfit simulation.
        review_capacity:
            Proportion of cases that can actually be reviewed.

    Returns:
        Governance DataFrame with review status.
    """

    reviewed = (
        governance_df.sample(
            frac=review_capacity,
            random_state=42,
        ).index
    )

    governance_df = governance_df.copy()

    governance_df["Reviewed"] = False
    governance_df.loc[reviewed, "Reviewed"] = True

    return governance_df


# ==========================================================
# Governance Summary
# ==========================================================

def create_governance_summary(
    governance_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Summarise governance simulation outcomes.

    Args:
        governance_df:
            Governance simulation DataFrame.

    Returns:
        Summary table.
    """

    summary = pd.DataFrame({
        "Metric": [
            "Total Cases",
            "Baseline Positive Decisions",
            "Policy Misfit Decisions",
            "Reviewed Cases",
            "Unreviewed Cases",
        ],
        "Value": [
            len(governance_df),
            governance_df["BaselineDecision"].sum(),
            governance_df["PolicyMisfitDecision"].sum(),
            governance_df["Reviewed"].sum(),
            (~governance_df["Reviewed"]).sum(),
        ]
    })

    return summary


# ==========================================================
# Governance Trade-off Plot (Figure 8)
# Figure 8
# ==========================================================

def plot_governance_tradeoff(
    summary: pd.DataFrame,
    output_path,
):
    """
    Plot governance trade-off summary.

    Args:
        summary:
            Governance summary DataFrame.
        output_path:
            Location to save the figure.
    """

    plt.figure(figsize=(8, 5))

    plt.bar(
        summary["Metric"],
        summary["Value"],
    )

    plt.xticks(rotation=25, ha="right")

    plt.ylabel("Count")

    plt.title("Figure 8: Governance Trade-offs")

    plt.tight_layout()

    plt.savefig(output_path, dpi=300)

    plt.close()
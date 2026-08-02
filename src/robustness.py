"""
Robustness analysis functions for the empirical validation pipeline.

This module provides reusable functions for assessing
the stability and reliability of model performance.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


# ==========================================================
# Bootstrap Confidence Intervals
# ==========================================================

def bootstrap_confidence_interval(
    y_true,
    y_pred,
    y_prob,
    metric_function,
    n_bootstrap: int = 1000,
    confidence_level: float = 0.95,
    random_state: int = 42,
):
    """
    Estimate a confidence interval for a metric using bootstrap
    resampling.

    Args:
        y_true: True labels.
        y_pred: Predicted labels.
        y_prob: Predicted probabilities.
        metric_function: Metric function to evaluate.
        n_bootstrap: Number of bootstrap samples.
        confidence_level: Confidence level.
        random_state: Random seed.

    Returns:
        Mean estimate, lower CI, upper CI.
    """

    rng = np.random.default_rng(random_state)

    scores = []

    n = len(y_true)

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    y_prob = np.asarray(y_prob)

    for _ in range(n_bootstrap):

        indices = rng.choice(
            n,
            size=n,
            replace=True
        )

        yt = y_true[indices]
        yp = y_pred[indices]
        ypr = y_prob[indices]

        if metric_function == roc_auc_score:
            score = metric_function(yt, ypr)
        else:
            score = metric_function(yt, yp)

        scores.append(score)

    lower = np.percentile(
        scores,
        (1 - confidence_level) / 2 * 100
    )

    upper = np.percentile(
        scores,
        (1 + confidence_level) / 2 * 100
    )

    return (
        float(np.mean(scores)),
        float(lower),
        float(upper),
    )


# ==========================================================
# Bootstrap Summary Table
# ==========================================================

def create_bootstrap_summary(
    y_true,
    y_pred,
    y_prob,
    n_bootstrap: int = 1000,
) -> pd.DataFrame:
    """
    Create a publication-ready summary table containing
    bootstrap confidence intervals for all evaluation metrics.

    Args:
        y_true: True labels.
        y_pred: Predicted labels.
        y_prob: Predicted probabilities.
        n_bootstrap: Number of bootstrap samples.

    Returns:
        Bootstrap summary table.
    """

    metrics = [
        ("Accuracy", accuracy_score),
        ("Precision", precision_score),
        ("Recall", recall_score),
        ("F1 Score", f1_score),
        ("ROC AUC", roc_auc_score),
    ]

    rows = []

    for metric_name, metric_function in metrics:

        mean, lower, upper = bootstrap_confidence_interval(
            y_true=y_true,
            y_pred=y_pred,
            y_prob=y_prob,
            metric_function=metric_function,
            n_bootstrap=n_bootstrap,
        )

        rows.append({
            "Metric": metric_name,
            "Mean": round(mean, 3),
            "Lower 95% CI": round(lower, 3),
            "Upper 95% CI": round(upper, 3),
        })

    return pd.DataFrame(rows)

"""
Model training functions for the empirical validation pipeline.

This module provides reusable functions for training,
evaluating, and comparing machine learning models.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    auc,
)

import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================================
# Train-Test Split
# ==========================================================

def split_train_test(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.Series,
    pd.Series,
]:
    """
    Split the dataset into training and testing sets.

    Args:
        X: Feature matrix.
        y: Target vector.
        test_size: Proportion of test observations.
        random_state: Random seed.

    Returns:
        X_train, X_test, y_train, y_test
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


# ==========================================================
# Logistic Regression
# ==========================================================

def train_logistic_regression(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42
) -> LogisticRegression:
    """
    Train a Logistic Regression classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training target vector.
        random_state: Random seed.

    Returns:
        Trained LogisticRegression model.
    """

    model = LogisticRegression(
        random_state=random_state,
        max_iter=1000
    )

    model.fit(X_train, y_train)

    return model


# ==========================================================
# Random Forest
# ==========================================================

def train_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42
) -> RandomForestClassifier:
    """
    Train a Random Forest classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training target vector.
        random_state: Random seed.

    Returns:
        Trained RandomForestClassifier model.
    """

    model = RandomForestClassifier(
        random_state=random_state,
        n_estimators=100
    )

    model.fit(X_train, y_train)

    return model


# ==========================================================
# XGBoost
# ==========================================================

def train_xgboost(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42
) -> XGBClassifier:
    """
    Train an XGBoost classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training target vector.
        random_state: Random seed.

    Returns:
        Trained XGBClassifier model.
    """

    model = XGBClassifier(
        random_state=random_state,
        n_estimators=100,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    return model


# ==========================================================
# Predictions
# ==========================================================

def predict_model(
    model,
    X_test: pd.DataFrame
) -> tuple[pd.Series, pd.Series]:
    """
    Generate class predictions and prediction probabilities.

    Args:
        model: Trained machine learning model.
        X_test: Test feature matrix.

    Returns:
        Tuple containing:
            - Predicted class labels
            - Predicted probabilities for the positive class
    """

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    return y_pred, y_prob


# ==========================================================
# Model Evaluation
# ==========================================================

def evaluate_model(
    y_true: pd.Series,
    y_pred: pd.Series,
    y_prob: pd.Series
) -> pd.DataFrame:
    """
    Evaluate classification performance.

    Args:
        y_true: True labels.
        y_pred: Predicted labels.
        y_prob: Predicted probabilities.

    Returns:
        DataFrame containing evaluation metrics.
    """

    metrics = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
            "ROC AUC"
        ],
        "Value": [
            accuracy_score(y_true, y_pred),
            precision_score(y_true, y_pred),
            recall_score(y_true, y_pred),
            f1_score(y_true, y_pred),
            roc_auc_score(y_true, y_prob),
        ]
    })

    return metrics


# ==========================================================
# Model Comparison
# ==========================================================

def compare_models(
    results: dict[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    Combine evaluation metrics from multiple models.

    Args:
        results: Dictionary mapping model names to
                 evaluation DataFrames.

    Returns:
        Combined comparison table.
    """

    comparison = []

    for model_name, metrics in results.items():

        row = {"Model": model_name}

        for _, metric in metrics.iterrows():
            row[metric["Metric"]] = metric["Value"]

        comparison.append(row)

    return pd.DataFrame(comparison)


# ==========================================================
# ROC Curve Plot
# ==========================================================

def plot_roc_curves(
    models: dict,
    y_true,
    output_path: Path,
    figsize: tuple[int, int] = (8, 6),
    show: bool = True,
) -> None:
    """
    Generate and save ROC curves for one or more models.

    Args:
        models:
            Dictionary where keys are model names and
            values are predicted probabilities.

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

    # Random classifier
    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Random Classifier",
    )

    for model_name, y_prob in models.items():

        fpr, tpr, _ = roc_curve(
            y_true,
            y_prob,
        )

        roc_auc = auc(
            fpr,
            tpr,
        )

        plt.plot(
            fpr,
            tpr,
            linewidth=2,
            label=f"{model_name} (AUC = {roc_auc:.3f})",
        )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Figure 3: ROC Curves")

    plt.legend(loc="lower right")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    if show:
        plt.show()

    plt.close()



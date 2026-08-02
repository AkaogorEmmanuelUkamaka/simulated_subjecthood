"""
Visualisation functions for the empirical validation pipeline.

This module provides reusable functions for generating
publication-quality figures used throughout the project.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ==========================================================
# Missingness Heatmap
# ==========================================================

def plot_missingness_heatmap(
    dataframe: pd.DataFrame,
    output_path: Path,
    figsize: tuple[int, int] = (12, 6),
    show: bool = True
) -> None:
    """
    Generate and save a missingness heatmap.

    Args:
        dataframe: Input dataset.
        output_path: File path for saving the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.heatmap(
        dataframe.isnull(),
        cmap="viridis",
        cbar=False,
        yticklabels=False
    )

    plt.title("Figure 1: Missingness Heatmap")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Numerical Feature Distributions
# ==========================================================

def plot_histogram(
    dataframe: pd.DataFrame,
    column: str,
    output_path: Path,
    figsize: tuple[int, int] = (8, 5),
    show: bool = True
) -> None:
    """
    Generate and save a histogram for a numerical variable.

    Args:
        dataframe: Input dataset.
        column: Numerical column to plot.
        output_path: Destination path for the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.histplot(
        dataframe[column],
        kde=True,
        edgecolor="black"
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Boxplots
# ==========================================================

def plot_boxplot(
    dataframe: pd.DataFrame,
    column: str,
    output_path: Path,
    figsize: tuple[int, int] = (8, 5),
    show: bool = True
) -> None:
    """
    Generate and save a boxplot for a numerical variable.

    Args:
        dataframe: Input dataset.
        column: Numerical column to plot.
        output_path: Destination path for the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.boxplot(
        x=dataframe[column]
    )

    plt.title(f"Boxplot of {column}")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Correlation Heatmap
# ==========================================================

def plot_correlation_heatmap(
    dataframe: pd.DataFrame,
    output_path: Path,
    figsize: tuple[int, int] = (10, 8),
    show: bool = True
) -> None:
    """
    Generate and save a correlation heatmap.

    Args:
        dataframe: Input dataset.
        output_path: Destination path for the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    correlation = dataframe.corr(numeric_only=True)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Count Plot
# ==========================================================

def plot_countplot(
    dataframe: pd.DataFrame,
    column: str,
    output_path: Path,
    figsize: tuple[int, int] = (8, 5),
    show: bool = True
) -> None:
    """
    Generate and save a count plot for a categorical variable.

    Args:
        dataframe: Input dataset.
        column: Categorical column to plot.
        output_path: Destination path for the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.countplot(
        data=dataframe,
        x=column
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


# ==========================================================
# Target Distribution
# ==========================================================

def plot_target_distribution(
    dataframe: pd.DataFrame,
    target_column: str,
    output_path: Path,
    figsize: tuple[int, int] = (6, 5),
    show: bool = True
) -> None:
    """
    Generate and save the target class distribution.

    Args:
        dataframe: Input dataset.
        target_column: Target variable.
        output_path: Destination path for the figure.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.countplot(
        data=dataframe,
        x=target_column
    )

    plt.title("Target Class Distribution")
    plt.xlabel(target_column)
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()


            
# ==========================================================
# Representation Distribution
# ==========================================================

def plot_representation_distribution(
    dataframe: pd.DataFrame,
    column: str,
    output_path: Path,
    figsize: tuple[int, int] = (6, 5),
    show: bool = True
) -> None:
    """
    Generate and save a representation distribution plot.

    Args:
        dataframe: Input dataset.
        column: Categorical variable.
        output_path: Destination figure path.
        figsize: Figure size.
        show: Whether to display the figure.
    """

    plt.figure(figsize=figsize)

    sns.countplot(
        data=dataframe,
        x=column
    )

    plt.title(f"Representation Distribution: {column}")
    plt.xlabel(column)
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    if show:
        plt.show()

    plt.close()
    
"""
Dataset auditing functions for the empirical validation pipeline.

This module provides reusable functions for inspecting dataset
structure, quality, and completeness before analysis.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd

# ==========================================================
# Dataset Structure
# ==========================================================

def dataset_shape(dataframe: pd.DataFrame) -> tuple[int, int]:
    """
    Return the number of rows and columns in the dataset.

    Args:
        dataframe: Input dataset.

    Returns:
        A tuple containing:
            - Number of rows
            - Number of columns
    """
    return dataframe.shape

# ==========================================================
# Dataset Columns
# ==========================================================

def dataset_columns(dataframe: pd.DataFrame) -> list[str]:
    """
    Return the column names of the dataset.

    Args:
        dataframe: Input dataset.

    Returns:
        A list containing the dataset column names.
    """
    return dataframe.columns.tolist()

# ==========================================================
# Dataset Data Types
# ==========================================================

def dataset_dtypes(dataframe: pd.DataFrame) -> pd.Series:
    """
    Return the data types of each column.

    Args:
        dataframe: Input dataset.

    Returns:
        A pandas Series containing the data type of each column.
    """
    return dataframe.dtypes

# ==========================================================
# Summary Statistics
# ==========================================================

def dataset_summary(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics for the dataset.

    Args:
        dataframe: Input dataset.

    Returns:
        A pandas DataFrame containing descriptive statistics.
    """
    return dataframe.describe(include="all")

# ==========================================================
# Dataset Information
# ==========================================================

def dataset_info(dataframe: pd.DataFrame) -> None:
    """
    Display general information about the dataset.

    Args:
        dataframe: Input dataset.
    """
    dataframe.info()


# ==========================================================
# Duplicate Records
# ==========================================================

def count_duplicates(dataframe: pd.DataFrame) -> int:
    """
    Count duplicate rows in the dataset.

    Args:
        dataframe: Input dataset.

    Returns:
        Number of duplicate rows.
    """
    return dataframe.duplicated().sum()
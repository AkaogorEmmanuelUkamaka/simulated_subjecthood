"""
Data preprocessing functions for the empirical validation pipeline.

This module provides reusable functions for preparing datasets
before analysis and modelling.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import pandas as pd

# ==========================================================
# Missing Value Handling
# ==========================================================
def check_missing_values(dataframe: pd.DataFrame) -> pd.Series:
    """
    Count missing values in each column.

    Args:
        dataframe: Input dataset.

    Returns:
        A pandas Series containing missing value counts.
    """
    return dataframe.isnull().sum()

# ==========================================================
# Data Preparation
# ==========================================================

def copy_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Create a copy of the input dataset.

    Args:
        dataframe: Input dataset.

    Returns:
        A copy of the dataset.
    """
    return dataframe.copy()

# ==========================================================
# Categorical Encoding
# ==========================================================

def encode_categorical_variables(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical variables using one-hot encoding.

    Args:
        dataframe: Input dataset.

    Returns:
        Dataset with categorical variables encoded.
    """
    return pd.get_dummies(dataframe, drop_first=True)

# ==========================================================
# Feature and Target Separation
# ==========================================================

def split_features_target(
    dataframe: pd.DataFrame,
    target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split a dataset into features (X) and target (y).

    Args:
        dataframe: Input dataset.
        target_column: Name of the target variable.

    Returns:
        A tuple containing:
            - Feature DataFrame (X)
            - Target Series (y)
    """
    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]

    return X, y
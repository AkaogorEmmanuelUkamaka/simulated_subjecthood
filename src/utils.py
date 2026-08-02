"""
Utility functions for the empirical validation pipeline.

This module contains reusable helper functions shared across
notebooks and Python modules.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path
from typing import Any

import joblib
import pandas as pd


# ==========================================================
# Directory Utilities
# ==========================================================
def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.

    Args:
        directory: Path to the directory to create.
    """
    directory.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Data Utilities
# ==========================================================

def load_data(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV dataset into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame.
    """
    return pd.read_csv(file_path)

# ==========================================================
# Output Utilities
# ==========================================================

def save_dataframe(dataframe: pd.DataFrame, file_path: Path) -> None:
    """
    Save a pandas DataFrame as a CSV file.

    Args:
        dataframe: DataFrame to save.
        file_path: Destination file path.
    """
    dataframe.to_csv(file_path, index=False)


# ==========================================================
# Model Persistence
# ==========================================================

def save_model(
    model,
    output_path: Path
) -> None:
    """
    Save a trained machine learning model.

    Args:
        model: Trained model.
        output_path: Destination file path.
    """

    joblib.dump(model, output_path)


def load_model(
    model_path: Path,
):
    """
    Load a previously saved machine learning model.

    Args:
        model_path: Path to the saved model.

    Returns:
        Loaded model.
    """

    return joblib.load(model_path)
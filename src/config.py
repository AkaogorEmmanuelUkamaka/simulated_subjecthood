"""
Project configuration settings.

This module defines all project paths and global configuration
variables used throughout the empirical validation pipeline.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

from pathlib import Path

# ==========================================================
# Project Root Directory
# ==========================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# Data Directories
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ==========================================================
# Output Directories
# ==========================================================

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
METRICS_DIR = OUTPUTS_DIR / "metrics"
MODELS_DIR = OUTPUTS_DIR / "models"
REPORTS_DIR = OUTPUTS_DIR / "reports"

# ==========================================================
# Other Project Directories
# ==========================================================

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

SRC_DIR = PROJECT_ROOT / "src"

DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

# ==========================================================
# Dataset Paths
# ==========================================================

HEART_DATA_PATH = RAW_DATA_DIR / "heart.csv"

# ==========================================================
# Global Configuration
# ==========================================================

RANDOM_STATE = 42
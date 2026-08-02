"""
Exploratory Data Analysis Dashboard Page.

This page presents the exploratory data analysis (EDA)
performed during the empirical validation pipeline.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import sys
from pathlib import Path

import streamlit as st

# Make project root importable
sys.path.append(str(Path(__file__).resolve().parents[2]))

from dashboard.utils import (
    section_header,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊",
    layout="wide",
)

section_header("📊 Exploratory Data Analysis")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
The **Exploratory Data Analysis (EDA)** provides an overview of
the distributions and characteristics of the Heart Disease dataset
before governance experiments are conducted.

The analyses presented here help establish an understanding of the
dataset structure and support interpretation of subsequent
machine learning and governance evaluations.

As with every page in this dashboard, the visualisations shown
here are generated from saved outputs produced by the analytical
pipeline.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Observations",
        "918",
    )

with col2:
    st.metric(
        "Variables",
        "12",
    )

with col3:
    st.metric(
        "Categorical Variables",
        "7",
    )

with col4:
    st.metric(
        "Numerical Variables",
        "5",
    )


# ==========================================================
# Dataset Variables
# ==========================================================

section_header("🧾 Dataset Variables")

variables = {
    "Variable": [
        "Age",
        "Sex",
        "ChestPainType",
        "RestingBP",
        "Cholesterol",
        "FastingBS",
        "RestingECG",
        "MaxHR",
        "ExerciseAngina",
        "Oldpeak",
        "ST_Slope",
        "HeartDisease",
    ],
    "Type": [
        "Numerical",
        "Categorical",
        "Categorical",
        "Numerical",
        "Numerical",
        "Categorical",
        "Categorical",
        "Numerical",
        "Categorical",
        "Numerical",
        "Categorical",
        "Target",
    ],
}

st.dataframe(
    variables,
    use_container_width=True,
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The exploratory analysis confirms that the Heart Disease dataset
contains a mixture of numerical and categorical variables suitable
for classification modelling.

Understanding the composition of the dataset provides important
context for interpreting the governance experiments that follow,
particularly those relating to representation, fairness,
calibration, and accountability.
"""
)


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- The dataset combines demographic and clinical variables.
- Both numerical and categorical predictors are represented.
- The target variable is HeartDisease.
- These variables form the basis of all subsequent governance analyses.
"""
)
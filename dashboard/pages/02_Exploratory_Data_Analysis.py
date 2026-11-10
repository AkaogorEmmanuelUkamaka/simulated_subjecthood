
"""
Exploratory Data Analysis Dashboard Page.

This page presents an overview of the structure, variable
composition, and descriptive distributions of the Heart Failure
Prediction Dataset used in the empirical validation pipeline.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import sys
from pathlib import Path

import streamlit as st

# Make project root importable
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from dashboard.utils import section_header


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
# Figure Paths and Display Helper
# ==========================================================

FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


def display_figure(filename, caption):
    """Display an existing EDA figure if the file is available."""

    figure_path = FIGURES_DIR / filename

    if figure_path.exists():
        st.image(
            str(figure_path),
            caption=caption,
            use_container_width=True,
        )
    else:
        st.warning(f"Figure not found: {filename}")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
The **Exploratory Data Analysis (EDA)** page provides an overview
of the structure, variable composition, and descriptive
distributions of the Heart Failure Prediction Dataset before
the governance experiments are examined.

It distinguishes numerical and categorical predictors from
the target variable and presents selected distributions and
relationships among the dataset variables.

These descriptive views provide context for interpreting the
subsequent analyses of representation, predictive performance,
calibration, and governance.

The figures displayed here are existing outputs from the
analytical pipeline. This dashboard page does not independently
regenerate the exploratory computations.
"""
)

st.caption(
    "The visualisations on this page are supplementary EDA outputs "
    "and are not included in the publication figure numbering."
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Dataset Composition")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Observations", "918")

with col2:
    st.metric("Total Variables", "12")

with col3:
    st.metric("Numerical Predictors", "5")

with col4:
    st.metric("Categorical Predictors", "6")


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
        "Numerical predictor",
        "Categorical predictor",
        "Categorical predictor",
        "Numerical predictor",
        "Numerical predictor",
        "Categorical predictor",
        "Categorical predictor",
        "Numerical predictor",
        "Categorical predictor",
        "Numerical predictor",
        "Categorical predictor",
        "Categorical target",
    ],
}

st.dataframe(
    variables,
    use_container_width=True,
    hide_index=True,
)


# ==========================================================
# Outcome Distribution
# ==========================================================

section_header("❤️ Heart Disease Distribution")

st.markdown(
    """
The target variable, **HeartDisease**, represents the
classification outcome used in the predictive modelling
experiments.
"""
)

display_figure(
    "heart_disease_distribution.png",
    "Distribution of the HeartDisease target variable.",
)


# ==========================================================
# Numerical Variable Distribution
# ==========================================================

section_header("📈 Numerical Variable Distribution")

st.markdown(
    """
The age histogram provides a descriptive view of the
distribution of one of the dataset's numerical predictors.
"""
)

display_figure(
    "age_histogram.png",
    "Distribution of Age across the dataset observations.",
)


# ==========================================================
# Categorical Variable Distributions
# ==========================================================

section_header("📊 Categorical Variable Distributions")

st.markdown(
    """
The following figures show the observed distributions of
selected categorical predictors. They describe the composition
of the dataset and do not, by themselves, establish whether
the observations are representative of a wider population.
"""
)

col1, col2 = st.columns(2)

with col1:
    display_figure(
        "sex_countplot.png",
        "Distribution of observations by Sex.",
    )

with col2:
    display_figure(
        "chestpaintype_countplot.png",
        "Distribution of Chest Pain Type categories.",
    )

col3, col4 = st.columns(2)

with col3:
    display_figure(
        "exerciseangina_countplot.png",
        "Distribution of Exercise-Induced Angina categories.",
    )

with col4:
    display_figure(
        "st_slope_countplot.png",
        "Distribution of ST Slope categories.",
    )


# ==========================================================
# Relationships Among Variables
# ==========================================================

section_header("🔗 Correlation Analysis")

st.markdown(
    """
The correlation heatmap provides a descriptive overview of
the pairwise relationships among numerical variables.

Correlation indicates association within this dataset.
It does not establish causation or independently demonstrate
the predictive or clinical importance of a variable.
"""
)

display_figure(
    "correlation_heatmap.png",
    "Correlation heatmap of numerical dataset variables.",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The dataset comprises five numerical predictors and six
categorical predictors, alongside the binary categorical
target variable, HeartDisease.

The selected visualisations provide descriptive information
about the outcome distribution, age distribution, selected
categorical features, and relationships among numerical
variables.

These observations help establish the structure and
characteristics of the dataset used in the subsequent
classification and governance analyses. They should not
be interpreted as evidence of population representativeness,
clinical validity, or fairness on their own.
"""
)


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- The dataset contains **918 observations** and **12 variables**.
- Five variables are numerical predictors.
- Six variables are categorical predictors.
- HeartDisease is the binary categorical target variable.
- The displayed figures describe selected outcome, predictor,
  and correlation distributions.
- These supplementary visualisations provide context for
  subsequent predictive and governance evaluations.
- Dataset distributions alone do not establish
  representativeness or clinical validity.
"""
)

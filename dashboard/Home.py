
"""
Home page for the Simulated Subjecthood research dashboard.

This dashboard presents computational analyses, illustrative
evaluations, and supporting research outputs for:

Simulated Subjecthood and the Governance of Computational
Representation: From Predictive Performance to Institutional Power.

The dashboard is a presentation layer. Analytical computations
are performed in the project's scripts and notebooks.
"""

import streamlit as st


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Simulated Subjecthood Research Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================================
# Project Title
# ==========================================================

st.title(
    "Simulated Subjecthood and the Governance of Computational Representation"
)

st.caption(
    "Research Dashboard | Computational Representation, "
    "Institutional Authority and AI Governance"
)


# ==========================================================
# Research Objective
# ==========================================================

st.markdown("## Research Objective")

st.write(
    """
This research examines how computational systems construct
representations of individuals and how institutions use those
representations to inform decisions.

The concept of **simulated subjecthood** draws attention to the
institutional status acquired by computational representations:
they may become consequential proxies through which individuals
are classified, evaluated, prioritised, or governed.

The central argument is that predictive performance alone cannot
establish the legitimacy of these representations. Their use must
also be examined in relation to representational accuracy,
institutional authority, accountability, and governance.
"""
)


# ==========================================================
# Project Summary
# ==========================================================

st.markdown("## Research Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Research Focus",
        value="Simulated Subjecthood",
    )

with col2:
    st.metric(
        label="Computational Case",
        value="Healthcare ML",
    )

with col3:
    st.metric(
        label="Governance Risks Examined",
        value="6",
    )


# ==========================================================
# Research Structure
# ==========================================================

st.markdown("## Research Structure")

st.info(
    """
The dashboard brings together dataset examination,
machine-learning evaluation, and six governance-oriented
risk analyses.

These components serve different evidential purposes:
some report computational results, while others use
illustrative scenarios to examine potential governance
implications under specified assumptions.
"""
)

st.markdown(
    """
**1. Data and computational foundation**

- Dataset audit and characteristics
- Exploratory data analysis
- Machine-learning model development and evaluation

**2. Governance risk analyses**

- Demographic Representation Imbalance
- Subgroup Predictive Disparity
- Validation–Governance Gap
- Threshold-Dependent Decision Governance
- Feedback Contamination
- Governance Misfit

**3. Research interpretation**

- Integrated governance results
- Methodological limitations and assumptions
- Implications for institutional authority and AI governance
"""
)


# ==========================================================
# Dashboard Navigation
# ==========================================================

st.markdown("## Dashboard Navigation")

st.write(
    """
Use the navigation menu in the left sidebar to explore the
research components and their associated outputs.

The pages present analytical procedures, tables, figures,
and interpretations. Where an analysis is illustrative
or scenario-based, its assumptions and limitations should
be considered alongside the results.
"""
)


# ==========================================================
# About the Research
# ==========================================================

st.divider()

st.markdown("## About the Research")

st.write(
    """
Artificial intelligence increasingly informs decisions in
healthcare, finance, education, criminal justice, and public
administration.

In many of these settings, institutions do not act solely on
direct engagement with individuals. They also rely on
computational representations produced through data collection,
classification, prediction, and automated assessment.

This research investigates the philosophical and governance
implications of treating such representations as consequential
substitutes for the individuals they represent.

It examines how representational distortion, institutional
authority, and governance arrangements shape the consequences
of computational decision-making.
"""
)


# ==========================================================
# Interpreting the Results
# ==========================================================

st.divider()

st.markdown("## Interpreting the Results")

st.write(
    """
The dashboard distinguishes between three important forms of
analysis:

- **Computational findings:** Results obtained from the dataset,
  machine-learning models, and associated evaluation procedures.

- **Illustrative analyses:** Scenario-based examinations used
  to explore possible governance consequences under specified
  assumptions.

- **Conceptual interpretation:** Philosophical and normative
  arguments concerning simulated subjecthood, institutional
  power, and the legitimacy of computational representation.

These categories should not be treated as interchangeable.
An illustrative scenario does not, by itself, establish that
the corresponding outcome occurs in real institutions.
"""
)


# ==========================================================
# Reproducibility and Research Materials
# ==========================================================

st.divider()

st.markdown("## Research Materials and Reproducibility")

st.write(
    """
The project includes Python scripts, computational notebooks,
data files, analytical outputs, and supporting visualisations.

The dashboard presents selected outputs produced by the
research workflow. It does not independently rerun the
analyses or modify the underlying results.

Interpretation of each result should take account of the
relevant methodology, assumptions, data limitations, and
computational procedures documented in the accompanying
research materials.
"""
)


# ==========================================================
# Technologies Used
# ==========================================================

st.divider()

st.markdown("## Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
### Programming and Analysis

- Python
- Pandas
- NumPy
- Scikit-learn
"""
    )

with col2:
    st.markdown(
        """
### Machine Learning

- Logistic Regression
- Random Forest
- XGBoost
"""
    )

with col3:
    st.markdown(
        """
### Visualisation

- Streamlit
- Matplotlib
- Seaborn
"""
    )


# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    """
Simulated Subjecthood and the Governance of Computational Representation

Research Dashboard

Computational analysis and governance-oriented interpretation.
"""
)

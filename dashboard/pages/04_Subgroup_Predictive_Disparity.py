
"""
Subgroup Predictive Disparity Dashboard Page.

This page presents the model performance and subgroup evaluation
results associated with Section 4.2 of the paper.

Project:
Simulated Subjecthood and the Governance of Computational Representation
"""

import sys
from pathlib import Path

import streamlit as st

# Make project root importable
sys.path.append(str(Path(__file__).resolve().parents[2]))

from dashboard.utils import (
    section_header,
    display_figure,
    load_table,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Subgroup Predictive Disparity",
    page_icon="⚖️",
    layout="wide",
)

section_header("⚖️ Subgroup Predictive Disparity")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the model performance and subgroup evaluation
results associated with **Section 4.2** of the paper.

Three machine-learning models were evaluated: Logistic Regression,
Random Forest, and XGBoost. Their predictive performance was examined
alongside group-level evaluation metrics using the
Heart Failure Prediction Dataset.

**Subgroup Predictive Disparity** refers to observed differences
in predictive performance across the demographic groups evaluated
in the study. These differences provide information about how
model performance varies between groups and identify areas
that may warrant further investigation.

**Interpretive limitation:** Differences in subgroup performance
do not, by themselves, establish discrimination or amplification
of pre-existing bias. Demonstrating amplification requires an
explicitly defined baseline and evidence that the disparity
increased relative to that baseline.
"""
)


# ==========================================================
# Models Evaluated
# ==========================================================

section_header("🤖 Models Evaluated")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model 1", "Logistic Regression")

with col2:
    st.metric("Model 2", "Random Forest")

with col3:
    st.metric("Model 3", "XGBoost")


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Model Discrimination")

display_figure(
    "figure_3_roc_curves.png",
    caption="Figure 2. ROC Curves for the Three Classification Models.",
)

st.markdown(
    """
The Receiver Operating Characteristic (ROC) curves illustrate
the discriminative performance of the three classification models.

They provide a comparative view of how well each model distinguishes
between the outcome classes across different classification
thresholds.

These overall discrimination results complement, but do not
replace, the subgroup-level performance evaluation.
"""
)


# ==========================================================
# Table 3: Model Performance
# ==========================================================

section_header("📄 Table 3. Model Performance")

st.markdown(
    """
Table 3 summarises the predictive performance estimates
reported for the three classification models.
"""
)

performance_table = load_table(
    "table_3_model_performance.csv"
)

if performance_table is not None and not performance_table.empty:

    st.dataframe(
        performance_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 3 could not be loaded or contains no data."
    )


# ==========================================================
# Table 4: Subgroup Predictive Disparity Metrics
# ==========================================================

section_header(
    "⚖️ Table 4. Subgroup Predictive Disparity Metrics"
)

st.markdown(
    """
Table 4 presents the subgroup-level evaluation metrics
reported in the study.

The metrics provide an additional perspective on model evaluation
by showing how predictive performance differs across the
demographic groups examined.

Observed differences should be interpreted in the context of
the selected metrics, group sizes, outcome distributions, and
the limitations of the available dataset.

These results identify potential disparities requiring further
investigation. They do not independently establish discrimination,
causation, or amplification of pre-existing disparities.
"""
)

fairness_table = load_table(
    "table_4_fairness_metrics.csv"
)

if fairness_table is not None and not fairness_table.empty:

    st.dataframe(
        fairness_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 4 could not be loaded or contains no data."
    )


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

col1, col2 = st.columns(2)

with col1:
    if performance_table is not None and not performance_table.empty:
        st.download_button(
            label="📥 Download Table 3. Model Performance",
            data=performance_table.to_csv(index=False).encode("utf-8"),
            file_name="table_3_model_performance.csv",
            mime="text/csv",
        )

with col2:
    if fairness_table is not None and not fairness_table.empty:
        st.download_button(
            label="📥 Download Table 4. Subgroup Predictive Disparity Metrics",
            data=fairness_table.to_csv(index=False).encode("utf-8"),
            file_name="table_4_fairness_metrics.csv",
            mime="text/csv",
        )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.markdown(
    """
- Three classification models were evaluated: Logistic Regression,
  Random Forest, and XGBoost.
- ROC analysis was used to compare overall model discrimination.
- Table 3 presents the overall model performance estimates.
- Table 4 presents subgroup differences in predictive performance.
- The observed differences identify areas that may warrant
  further investigation.
- These findings support an examination of subgroup predictive
  disparity as a governance concern.
- The results do not, on their own, demonstrate discrimination,
  causation, or amplification of pre-existing bias.
"""
)

"""
Synthetic Bias Amplification Dashboard Page.

This page presents the empirical results for Section 4.2:
Synthetic Bias Amplification.

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
    display_figure,
    load_table,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Synthetic Bias Amplification",
    page_icon="⚖️",
    layout="wide",
)

section_header("⚖️ Synthetic Bias Amplification")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Synthetic Bias
Amplification**, corresponding to **Section 4.2** of the paper.

Three machine learning models were trained and evaluated to
investigate how predictive systems may amplify representational
imbalances through automated decision-making.

The experiments compare predictive performance and fairness
metrics to evaluate whether high predictive accuracy necessarily
corresponds to equitable governance outcomes.
"""
)


# ==========================================================
# Models Evaluated
# ==========================================================

section_header("🤖 Models Evaluated")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model 1",
        "Logistic Regression",
    )

with col2:
    st.metric(
        "Model 2",
        "Random Forest",
    )

with col3:
    st.metric(
        "Model 3",
        "XGBoost",
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_3_roc_curves.png",
    caption="Figure 3. ROC Curves for the Three Classification Models",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The ROC curves compare the discrimination ability of the three
classification models evaluated during the empirical validation.

While strong predictive performance is desirable, governance
evaluation requires consideration of fairness alongside accuracy.
Consequently, the subsequent fairness metrics complement the
performance results by examining whether prediction quality is
achieved equitably across different groups.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Model Performance")

st.markdown(
    """
The table below summarises the predictive performance of the
three classification models evaluated in this study.
"""
)

performance_table = load_table(
    "table_3_model_performance.csv"
)

st.dataframe(
    performance_table,
    use_container_width=True,
)


# ==========================================================
# Fairness Metrics
# ==========================================================

section_header("⚖️ Fairness Metrics")

st.markdown(
    """
Fairness metrics provide an additional governance perspective by
evaluating whether predictive performance differs across groups.
"""
)

fairness_table = load_table(
    "table_4_fairness_metrics.csv"
)

st.dataframe(
    fairness_table,
    use_container_width=True,
)


# ==========================================================
# Robustness Analysis
# ==========================================================

section_header("🧪 Robustness Analysis")

st.markdown(
    """
Bootstrap confidence intervals were computed to assess the
stability of the model performance estimates across repeated
samples.
"""
)

bootstrap_table = load_table(
    "table_5_bootstrap_confidence_intervals.csv"
)

st.dataframe(
    bootstrap_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

col1, col2, col3 = st.columns(3)

with col1:
    st.download_button(
        label="📥 Model Performance",
        data=performance_table.to_csv(index=False).encode("utf-8"),
        file_name="table_3_model_performance.csv",
        mime="text/csv",
    )

with col2:
    st.download_button(
        label="📥 Fairness Metrics",
        data=fairness_table.to_csv(index=False).encode("utf-8"),
        file_name="table_4_fairness_metrics.csv",
        mime="text/csv",
    )

with col3:
    st.download_button(
        label="📥 Bootstrap Results",
        data=bootstrap_table.to_csv(index=False).encode("utf-8"),
        file_name="table_5_bootstrap_confidence_intervals.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Three machine learning models were evaluated: Logistic Regression, Random Forest, and XGBoost.
- Model performance was assessed using ROC analysis and standard classification metrics.
- Fairness metrics complemented predictive performance by examining governance implications across groups.
- Bootstrap confidence intervals demonstrated the robustness of the empirical results.
- Figure 3, Table 3, Table 4, and the robustness analysis together provide the publication-ready outputs for this module.
"""
)    
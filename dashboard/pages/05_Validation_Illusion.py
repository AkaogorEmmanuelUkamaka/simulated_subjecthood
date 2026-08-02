"""
Validation Illusion Dashboard Page.

This page presents the empirical results for Section 4.3:
Validation Illusion.

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
    page_title="Validation Illusion",
    page_icon="🎯",
    layout="wide",
)

section_header("🎯 Validation Illusion")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Validation
Illusion**, corresponding to **Section 4.3** of the paper.

Validation Illusion refers to situations where conventional
performance metrics suggest that a predictive model performs
well, while important governance concerns remain undetected.

Calibration analysis provides an additional perspective by
examining whether predicted probabilities correspond closely to
observed outcomes.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Evaluation",
        "Calibration",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 4 • Table 5",
    )

with col3:
    st.metric(
        "Objective",
        "Reliability",
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_4_calibration_curves.png",
    caption="Figure 4. Calibration Curves",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
Calibration analysis evaluates whether predicted probabilities
accurately reflect observed outcomes.

A well-calibrated model may still produce governance risks if
institutional decisions rely exclusively on predictive accuracy
without considering representation, fairness, accountability,
and policy context.

This illustrates the concept of Validation Illusion developed
in the accompanying paper.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Publication Table")

st.markdown(
    """
The table below summarises the calibration metrics generated
during the empirical validation pipeline.
"""
)

calibration_table = load_table(
    "table_5_calibration_metrics.csv"
)

st.dataframe(
    calibration_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

with st.container():

    csv = calibration_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Table 5 (CSV)",
        data=csv,
        file_name="table_5_calibration_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Calibration analysis evaluated the reliability of predicted probabilities.
- Good calibration alone does not guarantee responsible AI governance.
- Governance evaluation requires calibration to be considered alongside representation, fairness, accountability, feedback dynamics, and institutional context.
- Figure 4 and Table 5 constitute the publication-ready outputs for the Validation Illusion module.
"""
)    



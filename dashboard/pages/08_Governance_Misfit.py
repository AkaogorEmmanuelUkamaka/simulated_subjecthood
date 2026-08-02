"""
Governance Misfit Dashboard Page.

This page presents the empirical results for Section 4.6:
Governance Misfit.

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
    page_title="Governance Misfit",
    page_icon="⚖️",
    layout="wide",
)

section_header("⚖️ Governance Misfit")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Governance
Misfit**, corresponding to **Section 4.6** of the paper.

Governance Misfit occurs when institutional policies,
decision thresholds, or operational constraints are
misaligned with the behaviour of AI-enabled decision systems.

The empirical simulations evaluate policy threshold shifts
and constrained review capacity to illustrate how governance
structures can influence algorithmic outcomes independently
of predictive model performance.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Governance Scenarios",
        "2",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 8 • Table 8",
    )

with col3:
    st.metric(
        "Evaluation Focus",
        "Policy Alignment",
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_8_governance_tradeoff.png",
    caption="Figure 8. Governance Trade-off",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The Governance Misfit experiments demonstrate that governance
outcomes depend not only on model performance but also on the
alignment between institutional policies and operational
implementation.

Policy threshold adjustments and limited review capacity can
substantially alter decision outcomes, even when predictive
performance remains unchanged. These findings emphasise that
effective AI governance requires both technically robust models
and governance frameworks that are appropriately aligned with
their operational context.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Publication Table")

st.markdown(
    """
The table below summarises the governance misfit metrics
generated during the empirical validation pipeline.
"""
)

governance_table = load_table(
    "table_8_governance_summary.csv"
)

st.dataframe(
    governance_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

with st.container():

    csv = governance_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Table 8 (CSV)",
        data=csv,
        file_name="table_8_governance_summary.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Governance Misfit was evaluated through policy threshold and resource constraint simulations.
- Institutional governance decisions can significantly influence AI outcomes independently of predictive accuracy.
- Aligning governance policies with operational realities is essential for trustworthy AI deployment.
- Figure 8 and Table 8 constitute the publication-ready outputs for this module.
"""
)    
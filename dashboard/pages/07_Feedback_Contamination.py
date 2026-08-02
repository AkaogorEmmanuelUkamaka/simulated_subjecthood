"""
Feedback Contamination Dashboard Page.

This page presents the empirical results for Section 4.5:
Feedback Contamination.

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
    page_title="Feedback Contamination",
    page_icon="🔄",
    layout="wide",
)

section_header("🔄 Feedback Contamination")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Feedback
Contamination**, corresponding to **Section 4.5** of the paper.

Feedback Contamination arises when the outputs of AI systems are
fed back into subsequent decision-making processes, reinforcing
existing patterns and potentially amplifying governance risks over
time.

The empirical simulations examine differential follow-up,
documentation completeness, and recursive performance degradation
resulting from repeated governance feedback loops.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Scenarios",
        "2",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 7 • Table 7",
    )

with col3:
    st.metric(
        "Governance Focus",
        "Feedback Loops",
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_7_feedback_decay.png",
    caption="Figure 7. Feedback Decay",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The feedback contamination simulation demonstrates how governance
risks can accumulate when algorithmic outputs are repeatedly fed
back into future decision-making processes.

Differential follow-up and incomplete documentation introduce
systematic distortions that compound over successive iterations,
leading to gradual performance degradation and reinforcing existing
biases. These findings highlight the importance of monitoring
feedback loops within AI-enabled governance systems.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Publication Table")

st.markdown(
    """
The table below summarises the feedback contamination metrics
generated during the empirical validation pipeline.
"""
)

feedback_table = load_table(
    "table_7_feedback_metrics.csv"
)

st.dataframe(
    feedback_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

with st.container():

    csv = feedback_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Table 7 (CSV)",
        data=csv,
        file_name="table_7_feedback_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Two feedback contamination scenarios were evaluated: differential follow-up and documentation completeness.
- Recursive governance feedback loops can progressively degrade system performance over time.
- Continuous monitoring of feedback mechanisms is essential to prevent the reinforcement of governance risks.
- Figure 7 and Table 7 constitute the publication-ready outputs for the Feedback Contamination module.
"""
)



"""
Accountability Diffusion Dashboard Page.

This page presents the empirical results for Section 4.4:
Accountability Diffusion.

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
    page_title="Accountability Diffusion",
    page_icon="👥",
    layout="wide",
)

section_header("👥 Accountability Diffusion")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Accountability
Diffusion**, corresponding to **Section 4.4** of the paper.

Accountability Diffusion occurs when responsibility for automated
decisions becomes dispersed across multiple actors, making it
difficult to identify where governance failures originate.

The empirical simulation illustrates how automated allocation
mechanisms can reduce transparency and obscure decision-making
responsibility.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Simulation",
        "Allocation",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 6 • Table 6",
    )

with col3:
    st.metric(
        "Governance Focus",
        "Accountability",
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_6_allocation_simulation.png",
    caption="Figure 6. Allocation Simulation",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The allocation simulation demonstrates how automated decision
systems can distribute decision-making responsibility across
multiple organisational actors.

As responsibility becomes increasingly fragmented, identifying
the source of governance failures becomes more difficult.
This diffusion of accountability is a central governance risk
associated with AI-mediated decision systems and highlights the
importance of maintaining clear oversight structures.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Publication Table")

st.markdown(
    """
The table below summarises the allocation metrics generated
during the empirical validation pipeline.
"""
)

allocation_table = load_table(
    "table_6_allocation_metrics.csv"
)

st.dataframe(
    allocation_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

with st.container():

    csv = allocation_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Table 6 (CSV)",
        data=csv,
        file_name="table_6_allocation_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Accountability Diffusion was evaluated through an allocation simulation.
- Automated allocation mechanisms can obscure responsibility for decisions.
- Effective AI governance requires clear accountability structures alongside technical performance.
- Figure 6 and Table 6 constitute the publication-ready outputs for this module.
"""
)    
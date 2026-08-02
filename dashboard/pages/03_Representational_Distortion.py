"""
Representational Distortion Dashboard Page.

This page presents the empirical results for Section 4.1:
Representational Distortion.

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
    page_title="Representational Distortion",
    page_icon="📈",
    layout="wide",
)

section_header("📈 Representational Distortion")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the empirical evaluation of **Representational
Distortion**, corresponding to **Section 4.1** of the paper.

Representational Distortion occurs when the characteristics of
individuals are unevenly represented within a dataset, leading to
systematic differences in how groups are modelled by machine
learning systems.

The analysis evaluates representation across demographic groups
using the Representational Integrity Index (RII) and related
distributional summaries generated during the empirical
validation pipeline.
"""
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Groups Evaluated",
        "2",
    )

with col2:
    st.metric(
        "Representation Metrics",
        "RII",
    )

with col3:
    st.metric(
        "Publication Outputs",
        "Figure 2 • Table 2",
    )



# ==========================================================
# Publication Figure
# ==========================================================

section_header("📈 Publication Figure")

display_figure(
    "figure_2_representation_distribution.png",
    caption="Figure 2. Representation Distribution",
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
The Representational Integrity Index (RII) evaluates whether
demographic groups are proportionally represented within the
dataset.

Uneven representation increases the risk that machine learning
models learn patterns that favour majority groups while
underrepresenting minority populations. Such distortions form one
of the earliest governance risks explored in this research and
provide the foundation for the subsequent analyses of fairness,
validation, accountability, feedback, and governance misfit.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("📄 Publication Table")

st.markdown(
    """
The table below presents the publication-ready representation
summary generated during the empirical validation pipeline.
"""
)

representation_table = load_table(
    "table_2_representational_integrity_metrics.csv"
)

st.dataframe(
    representation_table,
    use_container_width=True,
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

with st.container():

    csv = representation_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Table 2 (CSV)",
        data=csv,
        file_name="table_2_representational_integrity_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.success(
    """
- Representational Distortion was evaluated using the Representational Integrity Index (RII).
- Distributional differences between demographic groups were examined before model development.
- Figure 2 and Table 2 provide the publication-ready outputs for this module.
- These findings establish the empirical basis for the fairness analyses presented in the next section.
"""
)    

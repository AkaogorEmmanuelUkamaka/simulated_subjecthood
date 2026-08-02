"""
Overall Governance Report Dashboard Page.

This page consolidates the results of all empirical validation
modules into a single executive summary.

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
    load_table,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Overall Governance Report",
    page_icon="📑",
    layout="wide",
)

section_header("📑 Overall Governance Report")


# ==========================================================
# Executive Summary
# ==========================================================

st.markdown(
    """
This page consolidates the findings from the complete empirical
validation pipeline developed for the study:

**The Risks of Governing Through Simulated Subjects**

The dashboard summarises the outputs of six governance
experiments that operationalise the theoretical framework
presented in the accompanying paper.

Rather than presenting isolated analyses, this report provides
an integrated view of how representational distortion,
algorithmic bias, validation artefacts, accountability
diffusion, recursive feedback contamination, and governance
misalignment collectively contribute to governance risks in
AI-mediated decision systems.
"""
)


# ==========================================================
# Research Overview
# ==========================================================

section_header("📊 Research Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Governance Experiments",
        "6",
    )

with col2:
    st.metric(
        "Publication Figures",
        "8",
    )

with col3:
    st.metric(
        "Publication Tables",
        "10",
    )

with col4:
    st.metric(
        "Notebook Modules",
        "9",
    )


# ==========================================================
# Integrated Results Summary
# ==========================================================

section_header("📋 Integrated Results Summary")

st.markdown(
    """
The table below consolidates the principal findings from each
empirical validation module. Together, these results provide
operational evidence supporting the theoretical framework of
simulated subjecthood developed in the accompanying paper.
"""
)

integrated_results = load_table(
    "table_9_integrated_results_summary.csv"
)

st.dataframe(
    integrated_results,
    use_container_width=True,
)


# ==========================================================
# Publication Outputs Summary
# ==========================================================

section_header("📈 Publication Outputs Summary")

st.markdown(
    """
The following table provides an index of the publication-ready
figures generated throughout the empirical validation pipeline.
These figures collectively illustrate the progression from data
audit through governance evaluation.
"""
)

figures_summary = load_table(
    "table_10_figures_summary.csv"
)

st.dataframe(
    figures_summary,
    use_container_width=True,
)


# ==========================================================
# Empirical Synthesis
# ==========================================================

section_header("🧠 Empirical Synthesis")

st.markdown(
    """
The empirical validation pipeline demonstrates that governance
risks associated with **simulated subjecthood** do not arise from
a single point of failure. Instead, they emerge through a sequence
of interacting mechanisms that collectively shape algorithmic
decision-making.

The progression begins with **Representational Distortion**, where
uneven data representation influences how individuals are modelled.
These imbalances create conditions under which predictive models
may amplify existing disparities, as demonstrated in the
**Synthetic Bias Amplification** experiments.

Although predictive performance may appear satisfactory according
to conventional evaluation metrics, the **Validation Illusion**
analysis shows that acceptable statistical performance does not
necessarily imply trustworthy governance outcomes.

The **Accountability Diffusion** simulations further demonstrate
that institutional responsibility becomes increasingly fragmented
when automated decision systems distribute authority across
multiple actors and processes.

Over time, the **Feedback Contamination** experiments illustrate
how recursive retraining on previously generated outputs can
reinforce and perpetuate governance errors, creating self-
reinforcing cycles of algorithmic behaviour.

Finally, the **Governance Misfit** analysis highlights that
institutional policies and operational constraints can alter
decision outcomes independently of predictive model quality,
emphasising that effective AI governance requires alignment
between technical systems and governance frameworks.

Collectively, these findings provide operational evidence
supporting the theoretical framework proposed in
*The Risks of Governing Through Simulated Subjects* and
demonstrate that governance risks emerge through the interaction
of representation, prediction, validation, accountability,
feedback, and institutional governance.
"""
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

col1, col2 = st.columns(2)

with col1:

    csv = integrated_results.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Integrated Results (Table 9)",
        data=csv,
        file_name="table_9_integrated_results_summary.csv",
        mime="text/csv",
    )

with col2:

    csv = figures_summary.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Figures Summary (Table 10)",
        data=csv,
        file_name="table_10_figures_summary.csv",
        mime="text/csv",
    )


# ==========================================================
# Final Conclusions
# ==========================================================

section_header("🏁 Final Conclusions")

st.success(
    """
The empirical validation pipeline has successfully operationalised
the theoretical framework developed in this research into a fully
reproducible analytical workflow.

Across six governance experiments, the study demonstrates that
governance risks associated with simulated subjecthood emerge
through multiple interacting mechanisms, including
representational distortion, synthetic bias amplification,
validation artefacts, accountability diffusion, recursive
feedback contamination, and governance misalignment.

All publication-ready tables, figures, models, metrics, and
reports presented throughout this dashboard were generated
directly from the analytical pipeline without manual
modification, ensuring transparency, reproducibility, and
consistency.

This dashboard serves as the interactive dissemination layer of
the project and reflects the completed empirical evaluation of
governance risks in AI-mediated decision systems.
"""
)    
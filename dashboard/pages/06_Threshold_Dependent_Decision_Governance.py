
"""
Threshold-Dependent Decision Governance Dashboard Page.

This page presents the allocation analysis associated with
Section 4.4 of the paper.

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
    page_title="Threshold-Dependent Decision Governance",
    page_icon="⚖️",
    layout="wide",
)

section_header("⚖️ Threshold-Dependent Decision Governance")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the allocation analysis associated with
**Section 4.4** of the paper.

**Threshold-Dependent Decision Governance** examines how
alternative classification thresholds influence the allocation
outcomes produced by a computational decision mechanism.

Decision thresholds determine how predicted probabilities
are translated into classification or allocation decisions.
Changing these thresholds can alter the number of positive
and negative decisions, with potential implications for
resource distribution and institutional decision-making.

**Interpretive limitation:** Threshold sensitivity describes
changes in allocation outcomes under specified decision rules.
It does not, by itself, establish discrimination, institutional
accountability diffusion, or the distribution of responsibility
among organisational actors.
"""
)


# ==========================================================
# Analysis Overview
# ==========================================================

section_header("📊 Analysis Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Analysis",
        "Allocation Simulation",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 5 • Table 7",
    )

with col3:
    st.metric(
        "Governance Focus",
        "Decision Thresholds",
    )


# ==========================================================
# Figure 5: Allocation Outcomes
# ==========================================================

section_header("📈 Allocation Outcomes")

display_figure(
    "figure_6_allocation_simulation.png",
    caption=(
        "Figure 5. Allocation Outcomes Across Alternative "
        "Decision Thresholds."
    ),
)

st.markdown(
    """
The figure presents allocation outcomes under alternative
decision thresholds.

The results illustrate how changing the classification
threshold affects the number of positive and negative
decisions produced by the evaluated mechanism.

These outcomes are conditional on the dataset, model
predictions, and threshold settings used in the simulation.
They should not be interpreted as direct evidence of
institutional resource allocation or actual organisational
decision-making.
"""
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
Decision thresholds are important governance parameters
because they influence how model predictions are translated
into operational decisions.

A stricter threshold may reduce the number of positive
decisions, while a more permissive threshold may increase
them. Such changes can affect who receives a positive
classification under the specified decision mechanism.

However, threshold selection also involves contextual
considerations, including the consequences of false-positive
and false-negative decisions, resource constraints, and
institutional priorities.

The simulation illustrates threshold-dependent allocation
behaviour. It does not establish which threshold is
institutionally appropriate or demonstrate how responsibility
is distributed among decision-makers.
"""
)


# ==========================================================
# Table 7: Allocation Metrics
# ==========================================================

section_header("📄 Table 7. Allocation Metrics")

st.markdown(
    """
Table 7 presents the allocation metrics generated
by the empirical analysis pipeline.
"""
)

allocation_table = load_table(
    "table_6_allocation_metrics.csv"
)

if allocation_table is not None and not allocation_table.empty:

    st.dataframe(
        allocation_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 7 could not be loaded or contains no data."
    )


# ==========================================================
# Scope and Limitations
# ==========================================================

section_header("🔎 Scope and Limitations")

st.markdown(
    """
The allocation results should be interpreted within the
following boundaries:

- **Allocation behaviour:** Describes how the simulated
  mechanism distributes positive and negative decisions
  under specified conditions.

- **Threshold sensitivity:** Describes how alternative
  decision thresholds affect allocation outcomes.

- **Decision consequences:** The simulation does not
  independently establish the real-world consequences
  of the resulting allocation decisions.

- **Institutional accountability:** Concerns decision
  authority, responsibility assignments, human oversight,
  and mechanisms for reviewing or challenging decisions.

- **Governance suitability:** Requires contextual evidence
  about institutional objectives, affected populations,
  available resources, and the consequences of errors.

The computational results inform the governance discussion
but do not independently establish these institutional
conditions.
"""
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

if allocation_table is not None and not allocation_table.empty:

    st.download_button(
        label="📥 Download Table 7: Allocation Metrics",
        data=allocation_table.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="table_7_allocation_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.markdown(
    """
- The study includes an allocation simulation.
- Alternative decision thresholds produce different
  allocation outcomes under the specified conditions.
- Threshold sensitivity is relevant to the governance
  of computational decision mechanisms.
- The simulation does not independently establish
  discrimination or accountability diffusion.
- Institutional accountability requires attention to
  decision authority, oversight, responsibility, and
  answerability.
- Figure 5 and Table 7 present the outputs associated
  with this analysis.
"""
)

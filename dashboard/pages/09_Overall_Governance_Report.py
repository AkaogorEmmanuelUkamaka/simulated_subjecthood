
"""
Integrated Governance Report Dashboard Page.

This page consolidates the computational analyses and
illustrative scenarios associated with the six governance
risks discussed in the paper.

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
    load_table,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Integrated Governance Report",
    page_icon="📑",
    layout="wide",
)

section_header("📑 Integrated Governance Report")


# ==========================================================
# Executive Summary
# ==========================================================

st.markdown(
    """
This report consolidates the computational analyses and
illustrative scenarios developed for the study:

**Simulated Subjecthood and the Governance of Computational Representation:
From Predictive Performance to Institutional Power**

The research examines six governance risks associated with
the use of computational representations in institutional
decision-making:

1. Demographic Representation Imbalance
2. Subgroup Predictive Disparity
3. Validation–Governance Gap
4. Threshold-Dependent Decision Governance
5. Feedback Contamination
6. Governance Misfit

The dashboard brings together the corresponding analytical
outputs to support an integrated examination of these risks.

An important distinction is maintained throughout:
computational results, illustrative simulations, conceptual
interpretations, and normative governance arguments represent
different forms of contribution. Each should be interpreted
within the scope and limitations of its underlying analysis.
"""
)


# ==========================================================
# Research Overview
# ==========================================================

section_header("📊 Research Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Governance Risks",
        "6",
    )

with col2:
    st.metric(
        "Publication Figures",
        "7",
    )

with col3:
    st.metric(
        "Publication Tables",
        "9",
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
The table below consolidates the principal outputs associated
with the analytical modules.

These results provide computational and illustrative material
for examining the governance framework. Their evidential
strength depends on the methods, assumptions, and limitations
of the individual analyses.
"""
)

integrated_results = load_table(
    "table_9_integrated_results_summary.csv"
)

if integrated_results is not None and not integrated_results.empty:

    st.markdown("**Dashboard Summary: Integrated Results**")

    st.dataframe(
        integrated_results,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "The integrated results summary could not be loaded "
        "or contains no data."
    )


# ==========================================================
# Publication Outputs Summary
# ==========================================================

section_header("📈 Publication Outputs Summary")

st.markdown(
    """
The following table provides an index of the figures generated
throughout the analytical workflow.

The figures cover the progression from dataset examination
and model evaluation to the analysis of governance-related
scenarios.
"""
)

figures_summary = load_table(
    "table_10_figures_summary.csv"
)

if figures_summary is not None and not figures_summary.empty:

    st.markdown("**Dashboard Summary: Publication Figures**")

    st.dataframe(
        figures_summary,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "The publication figures summary could not be loaded "
        "or contains no data."
    )


# ==========================================================
# Integrated Research Synthesis
# ==========================================================

section_header("🧠 Integrated Research Synthesis")

st.markdown(
    """
The six governance risks provide complementary perspectives
on the relationship between computational representation
and institutional power.

**1. Demographic Representation Imbalance**

Examines the distribution of demographic characteristics
within the dataset. The Representation Imbalance Index (RII)
of 0.710 indicates deviation from the equal-representation
reference used in the analysis. This benchmark is normative
and does not independently establish population
representativeness, fairness, or clinical validity.

**2. Subgroup Predictive Disparity**

Examines model performance across demographic subgroups.
Differences in accuracy, precision, recall, and F1-score
identify disparities that may warrant further investigation.
These observed differences do not establish bias amplification,
which would require comparison with an appropriate baseline.

**3. Validation–Governance Gap**

Examines the distinction between technical validation
and broader governance suitability. Bootstrap confidence
intervals and calibration metrics provide information
about particular dimensions of model evaluation. They do
not independently establish institutional readiness,
clinical suitability, or comprehensive governance quality.

**4. Threshold-Dependent Decision Governance**

Examines how alternative decision thresholds change
allocation outcomes. The simulation demonstrates that
decision rules can influence which cases receive positive
decisions. Threshold sensitivity does not independently
measure accountability or establish how responsibility
is distributed among institutional actors.

**5. Feedback Contamination**

Considers how computational outputs may enter subsequent
data and decision-making processes. The performance
trajectory uses a fixed decrement of 0.020 per simulated
iteration. It does not involve retraining on feedback-modified
data and therefore does not establish recursive performance
degradation or empirical bias propagation.

**6. Governance Misfit**

Examines potential mismatches between computational
decision systems, institutional policies, and operational
constraints. The simulations illustrate possible trade-offs
involving decision thresholds and review capacity. Establishing
actual institutional misfit requires contextual evidence
about real policies, responsibilities, and practices.
"""
)


# ==========================================================
# Conceptual Integration
# ==========================================================

section_header("🔗 Conceptual Integration")

st.markdown(
    """
Taken together, these six risks provide a framework for
examining how computational representations may acquire
significance beyond their original predictive function.

The framework connects questions about who and what is
represented in data with questions about how models are
evaluated, how their outputs influence decisions, how
decision rules shape allocation, and how institutional
arrangements condition their use.

The risks are conceptually related, but their inclusion
in a common framework does not establish that they form
a causal sequence or empirically propagate into one another.

The broader argument concerns the institutional authority
that computational representations may acquire when they
are incorporated into decision-making processes.

This distinction between predictive performance and
institutional power is central to the research.
"""
)


# ==========================================================
# Evidential Scope
# ==========================================================

section_header("🔎 Evidential Scope and Limitations")

st.markdown(
    """
The dashboard brings together different forms of analytical
and theoretical contribution:

- **Computational evidence:** Results produced through
  dataset analysis, model evaluation, subgroup comparisons,
  bootstrap estimation, and calibration assessment.

- **Illustrative simulations:** Scenario-based analyses
  demonstrating possible outcomes under specified
  assumptions, including threshold adjustments, feedback
  trajectories, and review capacity constraints.

- **Conceptual interpretation:** The theoretical connections
  developed between computational representation and
  institutional governance.

- **Normative argument:** The governance implications
  and institutional safeguards discussed in the research.

These forms of contribution should not be treated as
interchangeable. In particular:

- An equal-representation benchmark does not establish
  population representativeness.
- Subgroup performance differences do not automatically
  establish bias amplification.
- Technical validation does not establish comprehensive
  institutional readiness.
- Threshold simulations do not measure accountability
  distribution.
- A fixed performance decrement does not demonstrate
  recursive feedback effects.
- Scenario-based governance results do not establish
  actual institutional misfit.

The study also does not establish a causal chain connecting
the six risks. Their integration is conceptual and analytical,
rather than evidence of empirically demonstrated lifecycle
propagation.
"""
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

col1, col2 = st.columns(2)

with col1:
    if integrated_results is not None and not integrated_results.empty:

        st.download_button(
            label="📥 Download Integrated Results Summary",
            data=integrated_results.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="table_10_integrated_results_summary.csv",
            mime="text/csv",
        )

with col2:
    if figures_summary is not None and not figures_summary.empty:

        st.download_button(
            label="📥 Download Publication Figures Summary",
            data=figures_summary.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="table_11_figures_summary.csv",
            mime="text/csv",
        )


# ==========================================================
# Final Conclusions
# ==========================================================

section_header("🏁 Final Conclusions")

st.markdown(
    """
This research examines the governance implications of
computational representations through the framework
of simulated subjecthood.

Its central contribution is to shift attention beyond
predictive performance towards the institutional conditions
under which computational representations acquire authority
and influence decisions about individuals.

The six governance risks provide a structured vocabulary
for examining demographic representation, subgroup
performance, technical validation, decision thresholds,
feedback mechanisms, and institutional constraints.

The computational analyses provide evidence about the
specific dataset and models examined. The illustrative
simulations demonstrate possible outcomes under stated
assumptions, while the broader conceptual and normative
arguments establish their significance for AI governance.

The findings should be interpreted within these evidential
boundaries. They do not establish causal propagation among
the six risks or independently demonstrate actual institutional
governance failures.

The dashboard serves as an interactive presentation of
the project's analytical outputs and research framework.
"""
)


"""
Feedback Contamination Dashboard Page.

This page presents the feedback analysis associated with
Section 4.5 of the paper.

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
This page presents the feedback analysis associated with
**Section 4.5** of the paper.

**Feedback Contamination** describes the potential for outputs
from computational systems to influence subsequent data,
decisions, or system operations. When these outputs are reused
without adequate scrutiny, existing patterns and errors may
be carried into later decision-making processes.

The analysis includes an illustrative performance trajectory
and feedback-related scenarios involving differential follow-up
and documentation completeness.

**Interpretive limitation:** The performance trajectory uses
a fixed decrement of 0.020 per iteration. It does not involve
retraining the model on feedback-modified data. Consequently,
it illustrates a hypothetical decline in performance rather
than empirically demonstrating recursive feedback, cumulative
bias propagation, or actual model degradation.
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
        "Illustrative Feedback Simulation",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figure 6 • Table 8",
    )

with col3:
    st.metric(
        "Governance Focus",
        "Feedback Contamination",
    )


# ==========================================================
# Figure 6: Illustrative Performance Trajectory
# ==========================================================

section_header("📈 Illustrative Performance Trajectory")

display_figure(
    "figure_7_feedback_decay.png",
    caption=(
        "Figure 6. Performance Trajectory Across Simulated "
        "Deployment Iterations."
    ),
)

st.markdown(
    """
The figure presents an illustrative performance trajectory
across simulated deployment iterations.

The simulation applies a fixed decrement of 0.020 to the
initial accuracy estimate at each successive iteration.
The resulting trajectory therefore represents a specified
scenario rather than performance measured through repeated
model training or evaluation on feedback-modified data.

It should not be interpreted as independent evidence that
deployed systems necessarily experience the same pattern.
"""
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
Feedback mechanisms are important to AI governance because
system outputs may influence the information and decisions
used in subsequent stages of a process.

For example, differential follow-up may affect which cases
receive additional attention, while incomplete documentation
may affect the information available to later decision-makers.

These mechanisms raise questions about how information is
retained, reviewed, and reused.

However, demonstrating cumulative performance degradation
requires a clearly specified iterative model, documented
parameters, and evidence from successive evaluations using
appropriately updated data or model states.

The current performance trajectory uses a fixed decrement.
It therefore illustrates a hypothetical pattern rather than
establishing that feedback has caused actual performance
degradation or bias reinforcement.
"""
)


# ==========================================================
# Table 8: Feedback Metrics
# ==========================================================

section_header("📄 Table 8. Feedback Metrics")

st.markdown(
    """
Table 8 presents the feedback-related metrics generated
by the analysis pipeline. These results should be interpreted
in the context of the assumptions and procedures used to
construct the simulation.
"""
)

feedback_table = load_table(
    "table_7_feedback_metrics.csv"
)

if feedback_table is not None and not feedback_table.empty:

    st.dataframe(
        feedback_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 8 could not be loaded or contains no data."
    )


# ==========================================================
# Scope and Limitations
# ==========================================================

section_header("🔎 Scope and Limitations")

st.markdown(
    """
The feedback analysis should be interpreted with attention
to the following distinctions:

- **Feedback mechanism:** Describes how system outputs may
  enter subsequent data or decision-making processes.

- **Illustrative simulation:** Demonstrates a hypothetical
  performance trajectory under specified assumptions.

- **Fixed decrement:** The performance trajectory applies
  a predetermined reduction of 0.020 per iteration.

- **Recursive propagation:** Requires evidence that effects
  persist or change through successive feedback processes.

- **Model retraining:** The current simulation does not
  retrain the model using feedback-modified observations.

- **Performance degradation:** The simulated decline does
  not independently establish empirically observed
  performance degradation.

- **Bias reinforcement:** Requires an appropriate baseline
  and evidence that disparities are maintained or increased.

These are related but distinct claims. The illustrative
simulation does not independently establish all of them.
"""
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

if feedback_table is not None and not feedback_table.empty:

    st.download_button(
        label="📥 Download Table 8: Feedback Metrics",
        data=feedback_table.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="table_8_feedback_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.markdown(
    """
- The analysis examines feedback-related governance risks.
- The performance trajectory applies a fixed decrement
  of 0.020 per simulated iteration.
- The simulation does not involve retraining on
  feedback-modified data.
- Differential follow-up and documentation completeness
  illustrate possible feedback-related mechanisms.
- Actual recursive propagation and performance degradation
  require additional specification and direct testing.
- The results provide an illustrative basis for discussing
  feedback contamination in computational systems.

**Publication outputs:** Figure 6 (Performance Trajectory),
Table 8 (Feedback Metrics).
"""
)

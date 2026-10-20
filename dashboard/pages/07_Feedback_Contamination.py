"""
Feedback scenario dashboard page.

The displayed accuracy sequence is predefined and illustrative. It is not
the result of retraining a model on feedback-modified data.
"""

import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[2]))

from dashboard.utils import section_header, display_figure, load_table

st.set_page_config(
    page_title="Illustrative Feedback Scenario",
    page_icon="🔄",
    layout="wide",
)

section_header("🔄 Illustrative Feedback-Decay Scenario")

st.markdown(
    """
This page presents a hypothetical accuracy sequence used to discuss why
AI governance may need to consider changes in data and institutional
practice after deployment. The saved sequence subtracts 0.02 from an
initial value at each labelled iteration. The model is not retrained,
the dataset is not modified between iterations, and accuracy is not
recalculated from new predictions.
"""
)

st.warning(
    "Do not interpret the displayed decline as measured feedback contamination "
    "or as evidence that a real model would deteriorate by these amounts."
)

section_header("📈 Illustrative figure")
display_figure(
    "figure_7_feedback_decay.png",
    caption="Figure 7. Predefined illustrative feedback-decay sequence",
)

section_header("📋 Saved scenario values")
table = load_table("table_7_feedback_metrics.csv")
if table is not None:
    st.dataframe(table, use_container_width=True, hide_index=True)
else:
    st.warning("The saved feedback summary table could not be loaded.")

section_header("💡 Interpretation and limitation")
st.write(
    """
Real feedback effects require evidence that decisions alter subsequent
observations or labels, followed by an explicit analysis of how those
changes affect later model training or evaluation. This page does not
simulate that full mechanism. It presents a deterministic scenario to
support conceptual discussion only.
"""
)

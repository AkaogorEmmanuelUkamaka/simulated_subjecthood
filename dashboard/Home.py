"""
Home page for the Simulated Subjecthood governance case-study dashboard.

The dashboard displays saved analysis outputs and scenario illustrations.
It does not establish real-world clinical validity or institutional failure.
"""

import streamlit as st

st.set_page_config(
    page_title="Simulated Subjecthood Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Simulated Subjecthood: Governance Case Study")
st.caption("Computational case study and interactive research dashboard")

st.markdown("## Research focus")
st.write(
    """
This dashboard accompanies a computational case study exploring how
data-derived representations of people may become consequential when
AI outputs are used in institutional decisions. It presents dataset
auditing, predictive-model evaluation, subgroup comparisons, calibration,
and scenario-based analyses of thresholds, feedback, and review capacity.
"""
)

st.info(
    """
**Interpretation note:** Dataset and model metrics describe this benchmark
and its held-out evaluation. Threshold and review-capacity outputs are
simulations. The feedback-decay chart is a predefined illustration, not
repeated model retraining. None of these outputs alone establishes causal
discrimination, real-world institutional failure, or governance readiness.
"""
)

st.markdown("## Project summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Analytical modules", "8")
col2.metric("Saved summary tables", "10")
col3.metric("Selected figures", "8")
col4.metric("Governance scenarios", "Illustrative")

st.markdown("## Analytical workflow")
st.markdown(
    """
1. Dataset audit and exploratory analysis
2. Demographic representation description
3. Predictive modelling and subgroup performance
4. Bootstrap assessment of fixed held-out predictions
5. Probability calibration
6. Threshold-based allocation scenarios
7. Illustrative feedback-decay scenario
8. Policy-threshold and review-capacity scenarios
"""
)

st.markdown("## How to use this dashboard")
st.write(
    """
Use the navigation menu to inspect each analytical module. Each page
should be read alongside its assumptions and limitations. Downloaded
tables and figures are saved analysis artefacts; they should not be
interpreted as evidence beyond the design that produced them.
"""
)

st.divider()
st.markdown("## Reproducibility")
st.write(
    """
The repository contains the notebooks, Python source modules, dataset,
and saved outputs. See the README for setup instructions. The published
tables should be regenerated from the notebooks before final publication
or deployment, and the software environment should be tested in a clean
installation before exact package versions are pinned.
"""
)

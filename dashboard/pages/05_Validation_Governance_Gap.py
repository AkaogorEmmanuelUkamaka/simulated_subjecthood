
"""
Validation–Governance Gap Dashboard Page.

This page presents bootstrap uncertainty and calibration
results associated with Section 4.3 of the paper.

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
    page_title="Validation–Governance Gap",
    page_icon="🎯",
    layout="wide",
)

section_header("🎯 Validation–Governance Gap")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page presents the bootstrap uncertainty and calibration
analyses associated with **Section 4.3** of the paper.

The **Validation–Governance Gap** describes the distinction
between what technical validation results establish and what
may be required to justify the use of a computational model
in institutional decision-making.

Two evaluation dimensions are presented:

- **Bootstrap uncertainty:** examines the variability of
  evaluation metrics through resampling of the held-out test
  predictions.
- **Calibration:** examines the correspondence between
  predicted probabilities and observed outcome frequencies.

These analyses provide information about specific aspects
of model evaluation. Neither independently establishes
fairness, representativeness, generalisability, or institutional
governance readiness.

The results should therefore be interpreted within the scope
of the dataset and experimental procedures used in this study.
"""
)


# ==========================================================
# Analysis Overview
# ==========================================================

section_header("📊 Analysis Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Evaluation Dimensions",
        "Bootstrap and Calibration",
    )

with col2:
    st.metric(
        "Publication Outputs",
        "Figures 3–4 • Tables 5–6",
    )

with col3:
    st.metric(
        "Primary Focus",
        "Uncertainty and Probability Reliability",
    )


# ==========================================================
# Table 5: Bootstrap Confidence Intervals
# ==========================================================

section_header("📐 Table 5. Bootstrap Confidence Intervals")

st.markdown(
    """
Bootstrap resampling was used to estimate uncertainty around
the evaluation metrics obtained from the Logistic Regression
model on the held-out test partition.

The analysis used 1,000 bootstrap resamples to estimate
95% confidence intervals.

These intervals describe uncertainty conditional on the
existing held-out predictions and evaluation sample. They
do not represent repeated model training, independent
external validation, or performance in a deployment
population.
"""
)

bootstrap_table = load_table(
    "table_5_bootstrap_confidence_intervals.csv"
)

if bootstrap_table is not None and not bootstrap_table.empty:

    st.dataframe(
        bootstrap_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 5 could not be loaded or contains no data."
    )


# ==========================================================
# Figure 3: Calibration Curves
# ==========================================================

section_header("📈 Calibration Curves")

display_figure(
    "figure_4_calibration_curves.png",
    caption=(
        "Figure 3. Calibration Curves of the Evaluated "
        "Predictive Models."
    ),
)

st.markdown(
    """
Calibration curves compare predicted probabilities with
observed outcome frequencies.

A model whose predicted probabilities correspond more
closely to observed frequencies demonstrates better
calibration over the evaluated probability ranges.

The curves should be interpreted within the limits of the
dataset, sample size, and evaluation procedure used in
this study.
"""
)


# ==========================================================
# Table 6: Calibration Metrics
# ==========================================================

section_header("📄 Table 6. Calibration Metrics")

st.markdown(
    """
Table 6 presents the Brier scores obtained from the
evaluated models. The Brier score measures the accuracy
of probabilistic predictions, with lower values indicating
better performance.
"""
)

calibration_table = load_table(
    "table_5_calibration_metrics.csv"
)

if calibration_table is not None and not calibration_table.empty:

    st.dataframe(
        calibration_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "Table 6 could not be loaded or contains no data."
    )


# ==========================================================
# Figure 4: Brier Score Comparison
# ==========================================================

section_header("📊 Brier Score Comparison")

display_figure(
    "figure_5_brier_scores.png",
    caption=(
        "Figure 4. Brier Score Comparison Across "
        "Predictive Models."
    ),
)

st.markdown(
    """
The Brier score comparison provides an additional
perspective on the probabilistic performance of the
evaluated models.

A lower Brier score indicates better agreement between
predicted probabilities and observed outcomes. However,
this measure should not be interpreted as evidence of
fairness, representativeness, or institutional suitability.
"""
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("💡 Interpretation")

st.info(
    """
Bootstrap confidence intervals and calibration results
provide complementary information about model evaluation.

Bootstrap estimates indicate the uncertainty associated
with the evaluated metrics under the specified resampling
procedure. Calibration analysis examines the relationship
between predicted probabilities and observed outcomes.

However, favourable results in these dimensions do not
independently establish that a model is suitable for a
particular institutional decision.

The Validation–Governance Gap highlights the need to
distinguish technical evidence from broader governance
requirements, including fairness assessment, external
validation, contextual suitability, institutional oversight,
and accountability.

The analyses presented here illustrate this distinction.
They do not demonstrate that an institution actually
misinterpreted or improperly relied on the evaluated model.
"""
)


# ==========================================================
# Scope and Limitations
# ==========================================================

section_header("🔎 Scope and Limitations")

st.markdown(
    """
The following distinctions are important when interpreting
the results:

- **Bootstrap uncertainty:** The confidence intervals are
  conditional on resampling the held-out evaluation results.
  They do not capture uncertainty from repeated model
  training or independent datasets.

- **Calibration:** Examines the relationship between
  predicted probabilities and observed outcome frequencies.

- **Discrimination:** Examines the model's ability to
  distinguish between outcome classes.

- **Fairness:** Requires additional analysis of model
  outcomes and performance across relevant population groups.

- **Generalisability:** Requires evidence beyond performance
  on the evaluated dataset.

- **Governance suitability:** Depends on institutional
  context, decision consequences, oversight arrangements,
  and accountability mechanisms.

Consequently, neither bootstrap confidence intervals nor
calibration metrics should be treated as comprehensive
evidence of model reliability or governance readiness.
"""
)


# ==========================================================
# Downloads
# ==========================================================

section_header("📥 Downloads")

col1, col2 = st.columns(2)

with col1:
    if bootstrap_table is not None and not bootstrap_table.empty:
        st.download_button(
            label="📥 Download Table 5: Bootstrap Confidence Intervals",
            data=bootstrap_table.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="table_5_bootstrap_confidence_intervals.csv",
            mime="text/csv",
        )

with col2:
    if calibration_table is not None and not calibration_table.empty:
        st.download_button(
            label="📥 Download Table 6: Calibration Metrics",
            data=calibration_table.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="table_6_calibration_metrics.csv",
            mime="text/csv",
        )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("✅ Key Takeaways")

st.markdown(
    """
- Bootstrap confidence intervals provide estimates of
  uncertainty around the evaluated model metrics.
- The bootstrap results are conditional on the held-out
  predictions and do not constitute external validation.
- Calibration examines the correspondence between predicted
  probabilities and observed outcomes.
- Brier scores provide an additional measure of probabilistic
  prediction performance.
- Technical validation results do not independently establish
  fairness, generalisability, or governance readiness.
- The Validation–Governance Gap distinguishes the scope of
  computational evidence from broader institutional
  requirements.

**Publication outputs:** Figure 3 (Calibration Curves),
Figure 4 (Brier Score Comparison), Table 5 (Bootstrap
Confidence Intervals), and Table 6 (Calibration Metrics).
"""
)

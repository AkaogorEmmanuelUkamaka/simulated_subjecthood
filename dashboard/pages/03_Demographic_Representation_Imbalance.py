
"""
Demographic Representation Imbalance Dashboard Page.

Presents the distributional analysis of the Sex variable
and the Representational Integrity Index (RII).

The RII compares an observed distribution against a specified
reference distribution. The equal 50:50 reference used here
is a normative benchmark, not an established population standard.

Project:
Operational Evaluation of Governance Risks in Simulated Subjecthood
"""

import sys
from pathlib import Path

import streamlit as st

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
    page_title="Demographic Representation Imbalance",
    page_icon="📈",
    layout="wide",
)

section_header("📈 Demographic Representation Imbalance")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This section examines **Demographic Representation Imbalance**
through the distribution of the **Sex** variable in the
Heart Failure Prediction Dataset used for the computational
case study.

The analysis uses the **Representational Integrity Index (RII)**
to quantify the degree of alignment between the observed
distribution and a specified reference distribution.

The RII is calculated as:

\\[
RII = 1 - \\frac{1}{2}\\sum_i |p_i-r_i|
\\]

where \\(p_i\\) represents the observed proportion and
\\(r_i\\) represents the reference proportion for category \\(i\\).

The index ranges from 0 to 1. Higher values indicate greater
similarity between the observed and reference distributions,
while lower values indicate greater divergence.
"""
)


# ==========================================================
# Reference Distribution and Methodological Scope
# ==========================================================

section_header("Reference Distribution and Methodological Scope")

st.markdown(
    """
The primary comparison uses an equal reference distribution
of 50% female and 50% male.

This benchmark provides a transparent basis for examining
distributional deviation. However, it should be interpreted
as a **normative analytical assumption**, not as evidence
that the underlying population necessarily has an equal
distribution across the two recorded Sex categories.

Consequently, the RII measures similarity to the selected
benchmark. It does not independently establish population
representativeness, discrimination, or representational
injustice.
"""
)

st.warning(
    """
The reference distribution influences the resulting RII score.
Different reference populations or normative benchmarks may
produce different scores. The choice of reference must therefore
be justified when interpreting representational adequacy.
"""
)


# ==========================================================
# Load Publication Table
# ==========================================================

representation_table = load_table(
    "table_2_representational_integrity_metrics.csv"
)


# ==========================================================
# Summary Statistics
# ==========================================================

section_header("Demographic Distribution")

rii_value = "Unavailable"

if (
    representation_table is not None
    and not representation_table.empty
    and "Variable" in representation_table.columns
    and "Representational Integrity Index"
    in representation_table.columns
):
    sex_result = representation_table.loc[
        representation_table["Variable"] == "Sex",
        "Representational Integrity Index",
    ]

    if not sex_result.empty:
        rii_value = f"{float(sex_result.iloc[0]):.3f}"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Categories Examined",
        "2",
    )

with col2:
    st.metric(
        "Variable",
        "Sex",
    )

with col3:
    st.metric(
        "RII (50:50 Benchmark)",
        rii_value,
    )


# ==========================================================
# Publication Figure
# ==========================================================

section_header("Distribution of Observed Representation")

display_figure(
    "figure_2_representation_distribution.png",
    caption=(
        "Figure 1. Demographic representation distribution "
        "of the Sex variable in the Heart Failure Prediction Dataset."
    ),
)


# ==========================================================
# Interpretation
# ==========================================================

section_header("Interpretation")

st.info(
    """
The observed distribution shows that male participants
substantially outnumber female participants in the dataset.
The resulting RII of 0.710 indicates measurable deviation
from the specified equal reference distribution.

This finding establishes an observed demographic imbalance
within the computational dataset before predictive modelling.

However, the result should not be interpreted as proof that
the dataset is unrepresentative of its source population.
That conclusion would require an appropriate population-level
reference.

Likewise, distributional differences alone cannot establish
that a machine-learning model systematically favours one group.
Such conclusions require additional evidence from subgroup
performance evaluation and relevant institutional context.
"""
)


# ==========================================================
# Publication Table
# ==========================================================

section_header("Representational Integrity Index")

st.markdown(
    """
The following table presents the RII result generated by
the analytical pipeline. The score should be interpreted
in relation to the equal reference distribution used in
its calculation.
"""
)

if representation_table is not None and not representation_table.empty:

    st.dataframe(
        representation_table,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.warning(
        "The representational integrity metrics table "
        "could not be loaded or contains no data."
    )


# ==========================================================
# Downloads
# ==========================================================

section_header("Downloads")

if representation_table is not None and not representation_table.empty:

    csv = representation_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Table 2 (CSV)",
        data=csv,
        file_name="table_2_representational_integrity_metrics.csv",
        mime="text/csv",
    )


# ==========================================================
# Key Takeaways
# ==========================================================

section_header("Key Takeaways")

st.markdown(
    """
- The analysis examines the distribution of the Sex variable.
- The observed dataset contains more male than female participants.
- The RII of **0.710** indicates deviation from the equal
  reference distribution.
- The 50:50 reference is a normative benchmark, not an
  independently established population standard.
- RII measures distributional alignment; it is not a direct
  measure of fairness, model performance, or clinical validity.
- Further subgroup evaluation is required to examine
  differences in predictive behaviour.
"""
)

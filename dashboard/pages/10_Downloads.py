
"""
Research Artefacts and Downloads Dashboard Page.

This page provides access to the datasets, analytical tables,
figures, and supplementary reports associated with the study.

Project:
Simulated Subjecthood and the Governance of Computational Representation
"""

import sys
from pathlib import Path

import streamlit as st

# Make project root importable
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from dashboard.utils import section_header


# ==========================================================
# Project Directories
# ==========================================================

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

TABLES_DIR = OUTPUTS_DIR / "tables"
FIGURES_DIR = OUTPUTS_DIR / "figures"
REPORTS_DIR = OUTPUTS_DIR / "reports"

DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "heart.csv"

if not DATASET_PATH.exists():
    DATASET_PATH = OUTPUTS_DIR / "dataset" / "heart.csv"


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Research Artefacts and Downloads",
    page_icon="📥",
    layout="wide",
)

section_header("📥 Research Artefacts & Downloads")


# ==========================================================
# Introduction
# ==========================================================

st.markdown(
    """
This page provides access to the dataset, analytical tables,
figures, and supplementary materials associated with the study:

**Simulated Subjecthood and the Governance of Computational
Representation: From Predictive Performance to Institutional Power**

The downloadable materials provide access to selected outputs
from the computational analyses and illustrative scenarios
presented throughout the research.

Their interpretation should remain consistent with the
methodological scope and limitations of the individual analyses.
"""
)


# ==========================================================
# Project Outputs Overview
# ==========================================================

section_header("📊 Project Outputs")

table_files = (
    sorted(
        [
            path
            for path in TABLES_DIR.glob("table_*.csv")
            if path.is_file()
        ],
        key=lambda path: (
            int(path.stem.split("_")[1]),
            path.stem,
        ),
    )
    if TABLES_DIR.exists()
    else []
)

figure_files = (
    sorted(
        [
            path
            for path in FIGURES_DIR.glob("figure_*.png")
            if path.is_file()
        ]
    )
    if FIGURES_DIR.exists()
    else []
)

report_files = (
    sorted(
        [
            path
            for path in REPORTS_DIR.iterdir()
            if path.is_file() and not path.name.startswith(".")
        ]
    )
    if REPORTS_DIR.exists()
    else []
)

# Search the entire project, including subdirectories.
# Exclude virtual environments and common cache directories.
EXCLUDED_NOTEBOOK_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".ipynb_checkpoints",
}

notebook_files = [
    path
    for path in PROJECT_ROOT.rglob("*.ipynb")
    if not any(
        excluded_dir in path.parts
        for excluded_dir in EXCLUDED_NOTEBOOK_DIRS
    )
]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Available CSV Downloads", len(table_files))

with col2:
    st.metric("Publication Figures", len(figure_files))

with col3:
    st.metric("Notebook Modules", len(notebook_files))

with col4:
    st.metric("Governance Risks", "6")


# ==========================================================
# Table Display Names
# ==========================================================

table_labels = {
    "table_1_dataset_characteristics.csv":
        "Table 1 — Dataset Characteristics",

    "table_2_representational_integrity_metrics.csv":
        "Table 2 — Representational Integrity Metrics",

    "table_3_model_performance.csv":
        "Table 3 — Model Performance",

    "table_4_fairness_metrics.csv":
        "Table 4 — Subgroup Predictive Disparity Metrics",

    "table_5_bootstrap_confidence_intervals.csv":
        "Table 5 — Bootstrap Confidence Intervals",

    "table_5_calibration_metrics.csv":
        "Table 6 — Calibration Metrics",

    "table_6_allocation_metrics.csv":
        "Table 7 — Allocation Metrics",

    "table_7_feedback_metrics.csv":
        "Table 8 — Feedback Metrics",

    "table_8_governance_summary.csv":
        "Table 9 — Governance Summary",

    "table_9_integrated_results_summary.csv":
        "Dashboard Summary — Integrated Results",

    "table_10_figures_summary.csv":
        "Dashboard Summary — Publication Figures",
}


# ==========================================================
# Publication Figure Captions
# ==========================================================

figure_captions = {
    "figure_1_demographic_representation.png":
        "Figure 1 — Demographic Representation",

    "figure_2_roc_curves.png":
        "Figure 2 — Receiver Operating Characteristic Curves",

    "figure_3_calibration_curves.png":
        "Figure 3 — Calibration Curves",

    "figure_4_brier_scores.png":
        "Figure 4 — Brier Score Comparison",

    "figure_5_allocation_simulation.png":
        "Figure 5 — Threshold-Dependent Allocation Simulation",

    "figure_6_feedback_decay.png":
        "Figure 6 — Feedback Contamination Simulation",

    "figure_7_governance_tradeoff.png":
        "Figure 7 — Governance Misfit Scenarios",
}


# ==========================================================
# Source Dataset
# ==========================================================

section_header("📂 Source Dataset")

st.markdown(
    """
The computational analyses use the **Heart Failure Prediction
Dataset** attributed to **Fedesoriano** and available through
Kaggle.

The dataset contains demographic and clinical variables
used in a binary heart disease classification task.

The source dataset is provided here for reference alongside
the analytical outputs.
"""
)

st.markdown(
    """
**Dataset Information**

- **Dataset:** Heart Failure Prediction Dataset
- **Author:** Fedesoriano
- **Platform:** Kaggle
- **Source:** Original dataset page on Kaggle

Refer to the original dataset page for its licensing,
attribution, and usage conditions.
"""
)

if DATASET_PATH.exists():

    try:
        st.download_button(
            label="📥 Download heart.csv",
            data=DATASET_PATH.read_bytes(),
            file_name="heart.csv",
            mime="text/csv",
            key="heart_dataset",
        )

    except OSError:
        st.warning("The source dataset could not be read.")

else:

    st.warning(
        "The source dataset could not be found. Please ensure "
        "`data/raw/heart.csv` exists in the project directory."
    )

st.link_button(
    "🌐 View Original Kaggle Dataset",
    "https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction",
)


# ==========================================================
# Dataset Context
# ==========================================================

section_header("🎯 Dataset Context")

st.markdown(
    """
The Heart Failure Prediction Dataset provides a structured
classification task for examining selected computational
and governance questions.

Its relevant characteristics include:

- Demographic attributes, including age and sex.
- Clinical variables associated with the classification task.
- A binary outcome suitable for classification modelling.
- Structured tabular observations that support exploratory
  data analysis and model evaluation.
- Variables that permit selected subgroup evaluations.

The dataset offers a bounded computational case study.
It should not be treated as representative of all healthcare
populations or as sufficient evidence for generalising
the findings to other institutional settings.

The predictive results should also not be interpreted as
independent evidence of clinical validity or suitability
for real-world medical decision-making.
"""
)


# ==========================================================
# Analytical Tables
# ==========================================================

section_header("📄 Analytical Tables")

st.markdown(
    """
The following CSV files contain the tabular outputs
available in the project's outputs directory.

Publication tables retain their manuscript numbering.
Additional integrated summaries are identified separately
as dashboard outputs.
"""
)

if table_files:

    for path in table_files:

        label = table_labels.get(
            path.name,
            path.stem.replace("_", " ").title(),
        )

        try:
            st.download_button(
                label=f"📥 {label}",
                data=path.read_bytes(),
                file_name=path.name,
                mime="text/csv",
                key=path.name,
            )

        except OSError:
            st.warning(f"Could not read {path.name}.")

else:

    st.info("No analytical table files were found.")


# ==========================================================
# Publication Figures
# ==========================================================

section_header("🖼️ Analytical Figures")

st.markdown(
    """
The figures below provide visual representations of selected
results from the analytical workflow.

Where a figure corresponds to a numbered manuscript figure,
its publication caption is displayed below.
"""
)

if figure_files:

    for path in figure_files:

        caption = figure_captions.get(
            path.name,
            path.stem.replace("_", " ").title(),
        )

        try:
            st.image(
                str(path),
                caption=caption,
                use_container_width=True,
            )

            st.download_button(
                label=f"📥 Download {path.name}",
                data=path.read_bytes(),
                file_name=path.name,
                mime="image/png",
                key=f"fig_{path.name}",
            )

        except OSError:
            st.warning(f"Could not read {path.name}.")

else:

    st.info("No analytical figure files were found.")


# ==========================================================
# Supplementary Reports
# ==========================================================

if report_files:

    section_header("📑 Supplementary Reports")

    st.markdown(
        """
The following supplementary files are available in the
project's reports directory.
"""
    )

    for path in report_files:

        try:
            st.download_button(
                label=f"📥 Download {path.name}",
                data=path.read_bytes(),
                file_name=path.name,
                key=f"report_{path.name}",
            )

        except OSError:
            st.warning(f"Could not read {path.name}.")


# ==========================================================
# Study Limitations
# ==========================================================

section_header("⚠️ Study Limitations")

st.markdown(
    """
The research and its computational outputs should be interpreted
in light of the following limitations:

- The computational evaluation relies on a single publicly
  available healthcare benchmark dataset.
- The analyses focus on structured tabular data rather than
  multimodal or longitudinal healthcare records.
- The dataset does not capture the full range of institutional,
  demographic, and operational contexts in which computational
  representations may be used.
- Selected simulations illustrate possible governance
  mechanisms under specified assumptions; they do not
  independently establish real-world institutional effects.
- Further evaluations using datasets from different domains
  and additional institutional evidence would strengthen
  the scope of the research.

These limitations are important when interpreting the
computational findings and considering their broader
implications for AI governance.
"""
)

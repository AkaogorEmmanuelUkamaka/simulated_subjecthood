# Simulated Subjecthood: Computational Governance Case Study

An interactive Streamlit dashboard and Python analysis project exploring
how data-derived representations may be used in AI-assisted institutional
decisions.

## Dashboard

https://simulated-subjecthood.streamlit.app

## Scope and interpretation

The project uses the public Heart Failure Prediction Dataset as a
computational case study. It includes dataset auditing, Logistic
Regression, Random Forest and XGBoost evaluation, subgroup performance
comparisons, bootstrap intervals for fixed held-out predictions,
calibration metrics, threshold-based allocation scenarios, a predefined
feedback-decay illustration, and review-capacity scenarios.

**Important limitations**

- The equal-representation RII reference is a descriptive benchmark, not
  a justified target-population distribution.
- Subgroup metric gaps are descriptive and do not establish causal
  discrimination or bias amplification.
- Bootstrap resampling uses fixed held-out predictions; it does not
  retrain models in each resample.
- Threshold and review-capacity results are simulations, not observed
  institutional decisions.
- The feedback-decay sequence subtracts a fixed decrement; it does not
  retrain a model or demonstrate a causal feedback mechanism.
- High predictive performance does not establish governance readiness.

## Repository layout

- `data/raw/`: benchmark dataset
- `notebooks/`: analysis notebooks
- `src/`: reusable analysis functions
- `outputs/tables/`: saved CSV tables
- `outputs/figures/`: saved figures
- `dashboard/`: Streamlit app

## Local setup

Use Python 3.11 or newer in a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run dashboard/Home.py
```

Package versions are not pinned yet because a clean installation and
deployment test have not been completed. After testing the app and
notebooks in a fresh environment, record the exact working versions in
a lock file or a fully pinned requirements file.

## Reproducibility

Run notebooks from the repository root so that imports from `src/` resolve.
The saved outputs are artefacts from a previous run and should be regenerated
and compared with the manuscript tables before publication. Do not treat
scenario outputs as empirical findings about a real institution.

## License

MIT. See [LICENSE](LICENSE).

from pathlib import Path
import pandas as pd

from src.config import HEART_DATA_PATH
from src.utils import load_data
from src.preprocessing import encode_categorical_variables, split_features_target
from src.modelling import (
    split_train_test,
    train_logistic_regression,
    predict_model,
)
from src.governance import (
    simulate_policy_misfit,
    simulate_resource_constraints,
    create_governance_summary,
)

df = load_data(HEART_DATA_PATH)
encoded_df = encode_categorical_variables(df)
X, y = split_features_target(encoded_df, "HeartDisease")
X_train, X_test, y_train, y_test = split_train_test(X, y)

model = train_logistic_regression(X_train, y_train)
_, y_prob = predict_model(model, X_test)

governance_df = simulate_policy_misfit(
    y_prob=pd.Series(y_prob, index=y_test.index),
    threshold=0.50,
    policy_shift=0.10,
)

governance_df = simulate_resource_constraints(
    governance_df,
    review_capacity=0.75,
)

fresh = create_governance_summary(governance_df)
saved_path = Path("outputs/tables/table_8_governance_summary.csv")
saved = pd.read_csv(saved_path)

print("\n=== FRESH GOVERNANCE SUMMARY ===")
print(fresh.to_string(index=False))

print("\n=== SAVED GOVERNANCE SUMMARY ===")
print(saved.to_string(index=False))

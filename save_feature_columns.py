import pandas as pd
import joblib
import os

# ===============================
# PATHS
# ===============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv(DATA_PATH)

# ❗ Remove target column
TARGET_COLUMN = "prognosis"   # change if different
X = df.drop(columns=[TARGET_COLUMN])

# ===============================
# SAVE FEATURE COLUMNS
# ===============================
feature_columns = list(X.columns)

joblib.dump(feature_columns, OUTPUT_PATH)

print("✅ feature_columns.pkl created successfully")
print("Total features:", len(feature_columns))

import pandas as pd
import joblib
import os

DATA_PATH = "data/test_data.csv"

df = pd.read_csv(DATA_PATH)
print("Original dataset shape:", df.shape)

df.drop(columns=[c for c in df.columns if "Unnamed" in c], inplace=True, errors="ignore")
df.fillna(0, inplace=True)

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# Load trained encoder
label_encoder = joblib.load("models/label_encoder.pkl")
y_encoded = label_encoder.transform(y)

os.makedirs("processed_data", exist_ok=True)

X.to_csv("processed_data/cleaned_test_features.csv", index=False)
pd.DataFrame(y_encoded, columns=["prognosis"]).to_csv(
    "processed_data/cleaned_test_labels.csv", index=False
)

print("✅ Test data preprocessing completed")

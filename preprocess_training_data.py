import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

DATA_PATH = "data/training_data.csv"

df = pd.read_csv(DATA_PATH)
print("Original dataset shape:", df.shape)

# Remove unwanted columns
unnamed_cols = [c for c in df.columns if "Unnamed" in c]
df.drop(columns=unnamed_cols, inplace=True, errors="ignore")

df.fillna(0, inplace=True)

# Split
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# Encode target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save outputs
os.makedirs("processed_data", exist_ok=True)
os.makedirs("models", exist_ok=True)

X.to_csv("processed_data/cleaned_train_features.csv", index=False)
pd.DataFrame(y_encoded, columns=["prognosis"]).to_csv(
    "processed_data/cleaned_train_labels.csv", index=False
)

joblib.dump(label_encoder, "models/label_encoder.pkl")

# Save symptom order
joblib.dump(list(X.columns), "models/symptom_list.pkl")

print("✅ Training data preprocessing completed")

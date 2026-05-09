import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os


DATA_PATH = "data/diabetes.csv"
df = pd.read_csv(DATA_PATH)

print("Original shape:", df.shape)


df.drop(columns=[c for c in df.columns if "Unnamed" in c],
        inplace=True, errors="ignore")


df.fillna(df.mean(), inplace=True)


X = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)


os.makedirs("processed_data", exist_ok=True)
os.makedirs("models", exist_ok=True)

X_scaled.to_csv("processed_data/cleaned_diabetes_features.csv", index=False)
y.to_csv("processed_data/cleaned_diabetes_labels.csv", index=False)

joblib.dump(scaler, "models/scaler.pkl")

print("✅ Preprocessing completed successfully")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ===============================
# STEP 1: Load cleaned data
# ===============================
X = pd.read_csv("processed_data/cleaned_train_features.csv")
y = pd.read_csv("processed_data/cleaned_train_labels.csv").values.ravel()

print("Features shape:", X.shape)
print("Labels shape:", y.shape)

# ===============================
# STEP 2: Train-test split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ===============================
# STEP 3: Train model
# ===============================
disease_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

disease_model.fit(X_train, y_train)

# ===============================
# STEP 4: Evaluate model
# ===============================
y_pred = disease_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ===============================
# STEP 5: Save model
# ===============================
os.makedirs("models", exist_ok=True)
joblib.dump(disease_model, "models/disease_model.pkl")

print("✅ Disease prediction model trained & saved successfully")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

X = pd.read_csv("processed_data/cleaned_diabetes_features.csv")
y = pd.read_csv("processed_data/cleaned_diabetes_labels.csv").values.ravel()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)



print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/diabetes_rf_model.pkl")

print("✅ Model training & saving completed")

import pandas as pd
import joblib


model = joblib.load("models/diabetes_rf_model.pkl")
scaler = joblib.load("models/scaler.pkl")


user_data = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 85,
    "BMI": 26.5,
    "DiabetesPedigreeFunction": 0.45,
    "Age": 23
}

input_df = pd.DataFrame([user_data])


input_scaled = scaler.transform(input_df)
prediction = model.predict(input_scaled)[0]

if prediction == 1:
    print("⚠️ High Diabetes Risk")
else:
    print("✅ Low Diabetes Risk")

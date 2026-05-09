import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "models", "disease_model.pkl")
)

X_train = pd.read_csv(
    os.path.join(BASE_DIR, "processed_data", "cleaned_train_features.csv")
)

feature_columns = X_train.columns.tolist()

disease_map = pd.read_csv(
    os.path.join(BASE_DIR, "models", "disease_mapping.csv"),
    header=None,
    index_col=0
)[1].to_dict()


def predict_disease(symptoms):

    # Create user input vector
    X_user = pd.DataFrame(
        [[1 if col in symptoms else 0 for col in feature_columns]],
        columns=feature_columns
    )

    # Get probabilities
    probabilities = model.predict_proba(X_user)[0] * 100

    classes = model.classes_

    # Map disease names with probabilities
    results = {
        disease_map[int(cls)]: float(round(prob,2))
        for cls, prob in zip(classes, probabilities)
    }

    # Sort by probability (high → low)
    results = dict(
        sorted(results.items(),
        key=lambda x:x[1],
        reverse=True)
    )

    # Take highest probability disease
    top_disease=list(results.items())[0]

    disease_name=top_disease[0]

    confidence=top_disease[1]

    # Risk level logic
    if confidence >= 75:

        risk="High"

    elif confidence >= 50:

        risk="Medium"

    else:

        risk="Low"

    # Advice logic
    if risk=="High":

        advice="Consult a doctor immediately."

    elif risk=="Medium":

        advice="Monitor symptoms and consult doctor if needed."

    else:

        advice="Low risk but maintain precautions."

    return disease_name,confidence,risk,advice


# Testing block
if __name__ == "__main__":

    test_symptoms=[
        "fatigue",
        "headache",
        "cough",
        "chest_pain"
    ]

    result=predict_disease(test_symptoms)

    print(result)
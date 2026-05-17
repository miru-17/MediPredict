import sys
import os

# Allow backend to access root files
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from predict_disease import predict_disease


def run_prediction(user_email, symptoms):
    prediction = predict_disease(symptoms)

    return {
        "email": user_email,
        "symptoms": symptoms,
        "prediction": prediction
    }


if __name__ == "__main__":
    result = run_prediction(
        user_email="test@gmail.com",
        symptoms=["fatigue", "headache"]
    )
    print(result)

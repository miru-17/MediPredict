import sys
import os

# Allow backend to access root files
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from predict_disease import predict_disease


def run_prediction(symptoms):

    prediction = predict_disease(symptoms)

    # prediction currently returns:
    # ('Hypertension ', 26.0, 'Low', 'Low risk but maintain precautions.')

    disease = prediction[0]
    confidence = prediction[1]
    risk = prediction[2]
    advice = prediction[3]

    return {

        "disease": disease,
        "confidence": confidence,
        "risk": risk,
        "advice": advice,
        "symptoms": symptoms

    }


if __name__ == "__main__":

    result = run_prediction(

        symptoms=["fatigue","headache","cough","chest_pain"]

    )

    print(result)
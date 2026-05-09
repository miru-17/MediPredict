import joblib
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "models/random_forest_model.pkl")

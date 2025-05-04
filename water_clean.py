import joblib
import numpy as np

# Load your saved XGBoost model
model = joblib.load("xgboost_model.joblib")
sample_input = np.array([[6.66,193.68,47580.99,7.16,359.94,526.42,13.89,66.68,4.43	]])  # Shape must match training features

# Predict
prediction = model.predict(sample_input)

if prediction == 1:
    print(f"the water is safe bcz the potability of water  is {prediction}")
else:
    print(f"the water is not safe bcz the potability of water is {prediction}")
print(model)
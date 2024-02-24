from flask import current_app
import numpy as np

from app.services.ml_model.compute_hypothesis import compute_hypothesis

def predict_phishing_status(phishing_features_array):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    threshold = current_app.config["THRESHOLD"]
    
    try:
        x = np.array(phishing_features_array)

        prediction = compute_hypothesis(x)

        if prediction >= threshold:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print("Error predicting phishing status: " + str(e))
        return phishing_status

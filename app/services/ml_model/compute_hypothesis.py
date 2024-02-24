import numpy as np
from flask import current_app

def compute_hypothesis(x):
    try:
        w = np.load("app/services/ml_model/w.npy")
        b = np.load("app/services/ml_model/b.npy")

        prediction = 1 / (1 + np.exp(-np.dot(x, w) - b))
        
        return prediction
    except Exception as e:
        print("Error computing hypothesis: " + str(e))
        suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
        return suspicious_status

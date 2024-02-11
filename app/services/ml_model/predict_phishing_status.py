from flask import current_app
import numpy as np

from app.services.ml_model.compute_hypothesis import compute_hypothesis

def predict_phishing_status(phishing_features_array):
    """
    Summary: 
        Predicts the phishing status.

    Description: 
        The phishing features array is converted to a numpy array.\n
        The hypothesis is computed using the compute_hypothesis function.\n
        If the prediction is greater than or equal to 0.5, the phishing status is 1, otherwise it's 0.\n

    Arguments: 
        phishing_features_array (list): The phishing features array.

    Returns: 
        phishing_status (int): The phishing status.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        x = np.array(phishing_features_array)

        prediction = compute_hypothesis(x)

        if prediction >= 0.5:
            return 1
        else:
            return 0
    except Exception as e:
        print("Error predicting phishing status: " + str(e))
        return 1

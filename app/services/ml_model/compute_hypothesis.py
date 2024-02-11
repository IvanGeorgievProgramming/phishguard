import numpy as np

def compute_hypothesis(x):
    """
    Summary: 
        Computes the hypothesis.

    Description: 
        Computes the hypothesis using the weights and bias from the trained model.

    Arguments: 
        phishing_features_array (list): The phishing features array.

    Returns: 
        phishing_status (int): The phishing status.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        w = np.load("app/services/ml_model/w.npy")
        b = np.load("app/services/ml_model/b.npy")

        prediction = 1 / (1 + np.exp(-np.dot(x, w) - b))
        
        return prediction
    except Exception as e:
        print("Error computing hypothesis: " + str(e))
        return 0.5

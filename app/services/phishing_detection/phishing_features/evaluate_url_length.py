# 2
from flask import current_app

def evaluate_url_length(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    suspicious_treshold_min = current_app.config["URL_LENGTH_SUSPICIOUS_TRESHOLD_MIN"]
    suspicious_treshold_max = current_app.config["URL_LENGTH_SUSPICIOUS_TRESHOLD_MAX"]
    
    try:
        length = len(url)

        if length < suspicious_treshold_min:
            return legitimate_status
        elif length >= suspicious_treshold_min and length <= suspicious_treshold_max:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in evaluate_url_length: {e}")
        return suspicious_status
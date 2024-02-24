# 10
from flask import current_app

from app.utils.url_utils import is_same_domain

def evaluate_favicon_origin(url, favicon):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if favicon == "":
            return legitimate_status
        elif is_same_domain(url, favicon):
            return legitimate_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in evaluate_favicon_origin: {e}")
        return suspicious_status

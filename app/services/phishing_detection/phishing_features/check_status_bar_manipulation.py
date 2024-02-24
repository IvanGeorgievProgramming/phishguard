# 19
from flask import current_app

def check_status_bar_manipulation(is_status_bar_customized):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if is_status_bar_customized:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in check_status_bar_manipulation: {e}")
        return suspicious_status

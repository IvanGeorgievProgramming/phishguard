# 20
from flask import current_app

def detect_right_click_disablement(is_right_click_disabled):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if is_right_click_disabled:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in detect_right_click_disablement: {e}")
        return suspicious_status

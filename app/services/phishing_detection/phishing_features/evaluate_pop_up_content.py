# 21
from flask import current_app

def evaluate_pop_up_content(is_popup_asking_personal_info):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if is_popup_asking_personal_info:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in evaluate_pop_up_content: {e}")
        return suspicious_status

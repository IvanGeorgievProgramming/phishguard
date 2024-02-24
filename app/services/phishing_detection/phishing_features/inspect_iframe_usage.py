# 22
from flask import current_app

def inspect_iframe_usage(iframe_hidden_count, iframe_visible_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if iframe_hidden_count > 0:
            return phishing_status
        elif iframe_visible_count > 0:
            return suspicious_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in inspect_iframe_usage: {e}")
        return suspicious_status

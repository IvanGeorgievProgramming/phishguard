# 4
from flask import current_app

def inspect_at_symbol_in_url(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if "@" in url:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in inspect_at_symbol_in_url: {e}")
        return suspicious_status

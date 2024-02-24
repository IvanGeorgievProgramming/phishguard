# 5
from urllib.parse import urlparse
from flask import current_app

def verify_double_slash_position(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        parsed_url = urlparse(url)
        scheme = parsed_url.scheme

        expected_double_slash_pos = len(scheme) + 1

        last_double_slash = url.rfind("//")

        if last_double_slash == expected_double_slash_pos:
            return legitimate_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in verify_double_slash_position: {e}")
        return suspicious_status

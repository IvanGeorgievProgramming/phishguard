# 6
from urllib.parse import urlparse
from flask import current_app

def analyze_dash_in_domain(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        if "-" in domain:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in analyze_dash_in_domain: {e}")
        return suspicious_status

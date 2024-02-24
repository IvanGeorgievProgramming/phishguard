# 18
from flask import current_app

def count_website_redirections(redirections_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    redirections_count_legitimate_max = current_app.config["REDIRECTIONS_COUNT_LEGITIMATE_MAX"]
    redirections_count_suspicious_min = current_app.config["REDIRECTIONS_COUNT_SUSPICIOUS_MIN"]
    redirections_count_suspicious_max = current_app.config["REDIRECTIONS_COUNT_SUSPICIOUS_MAX"]
    
    try:
        if redirections_count <= redirections_count_legitimate_max:
            return legitimate_status
        elif redirections_count >= redirections_count_suspicious_min and redirections_count <= redirections_count_suspicious_max:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in count_website_redirections: {e}")
        return suspicious_status

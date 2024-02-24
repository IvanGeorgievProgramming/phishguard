# 16
from flask import current_app

def validate_sfh_domain_relevance(form_blank_links_count, form_external_links_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        if form_blank_links_count > 0:
            return phishing_status
        elif form_external_links_count > 0:
            return suspicious_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in validate_sfh_domain_relevance: {e}")
        return suspicious_status

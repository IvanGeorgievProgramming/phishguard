# 14
from flask import current_app

def assess_anchor_domain_similarity(a_internal_links_count, a_external_links_count, a_relative_links_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    suspicious_treshhold_min = current_app.config["ANCHOR_DOMAIN_SIMILARITY_SUSPICIOUS_THRESHOLD_MIN"]
    suspicious_treshhold_max = current_app.config["ANCHOR_DOMAIN_SIMILARITY_SUSPICIOUS_THRESHOLD_MAX"]
    
    try:
        if a_external_links_count == 0:
            return legitimate_status
        
        ratio = (a_internal_links_count + a_relative_links_count) / a_external_links_count
        percentage = ratio * 100

        if percentage < suspicious_treshhold_min:
            return legitimate_status
        elif percentage >= suspicious_treshhold_min and percentage <= suspicious_treshhold_max:
            return suspicious_status
        else:
            return phishing_status
        
    except Exception as e:
        print(f"Error in assess_anchor_domain_similarity: {e}")
        return suspicious_status

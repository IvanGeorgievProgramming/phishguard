# 15
from flask import current_app

def check_tag_links_domain_congruence(script_internal_links_count, script_external_links_count, script_relative_links_count, link_internal_links_count, link_external_links_count, link_relative_links_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    suspicious_treshold_min = current_app.config["TAG_LINKS_CONGRUENCE_SUSPICIOUS_THRESHOLD_MIN"]
    suspicious_treshold_max = current_app.config["TAG_LINKS_CONGRUENCE_SUSPICIOUS_THRESHOLD_MAX"]
    
    try:
        internal_links_count = script_internal_links_count + link_internal_links_count
        external_links_count = script_external_links_count + link_external_links_count
        relative_links_count = script_relative_links_count + link_relative_links_count

        if external_links_count == 0:
            return legitimate_status
        
        ratio = (internal_links_count + relative_links_count) / external_links_count
        percentage = ratio * 100

        if percentage < suspicious_treshold_min:
            return legitimate_status
        elif percentage >= suspicious_treshold_min and percentage <= suspicious_treshold_max:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in check_tag_links_domain_congruence: {e}")
        return 0.5

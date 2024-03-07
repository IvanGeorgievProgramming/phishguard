# 7
import tldextract
from flask import current_app

def count_subdomains_in_url(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    subdomain_count_legitimate_max = current_app.config["SUBDOMAIN_COUNT_LEGITIMATE_MAX"]
    subdomain_count_suspicious = current_app.config["SUBDOMAIN_COUNT_SUSPICIOUS"]
    
    try:
        extracted_url = tldextract.extract(url)
        subdomain = extracted_url.subdomain

        if subdomain and subdomain != "www":
            subdomain_count = subdomain.count(".") + 1
        else:
            subdomain_count = 0
        
        if subdomain_count <= subdomain_count_legitimate_max:
            return legitimate_status
        elif subdomain_count == subdomain_count_suspicious:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in count_subdomains_in_url: {e}")
        return suspicious_status

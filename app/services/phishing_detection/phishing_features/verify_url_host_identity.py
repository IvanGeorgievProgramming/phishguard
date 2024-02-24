# 17
import whois
from urllib.parse import urlparse
from flask import current_app

def verify_url_host_identity(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        domain = urlparse(url).netloc
            
        domain_info = whois.whois(domain)
            
        if domain_info.domain_name and any(hostname in url for hostname in domain_info.domain_name):
            return legitimate_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in verify_url_host_identity: {e}")
        return suspicious_status

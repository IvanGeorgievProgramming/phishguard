# 23
import whois
from urllib.parse import urlparse
from datetime import datetime, timedelta
from flask import current_app

def assess_domain_age(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        domain = urlparse(url).netloc
        
        domain_info = whois.whois(domain)
        
        if domain_info.creation_date:
            creation_date = domain_info.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]

            age = datetime.now() - creation_date

            if age >= timedelta(days=6*30):
                return legitimate_status
            else:
                return phishing_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in assess_domain_age: {e}")
        return suspicious_status

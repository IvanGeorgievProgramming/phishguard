# 9
import whois
from flask import current_app

def check_domain_registration_duration(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    minimum_registration_duration_for_legitimacy = current_app.config["MINIMUM_REGISTRATION_DURATION_FOR_LEGITIMACY"]
    
    try:
        domain_info = whois.whois(url)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date

        if type(creation_date) is list:
            creation_date = creation_date[0]
        if type(expiration_date) is list:
            expiration_date = expiration_date[0]

        if creation_date is not None and expiration_date is not None:
            paid_duration = expiration_date - creation_date
            if paid_duration.days <= minimum_registration_duration_for_legitimacy:
                return phishing_status
            else:
                return legitimate_status
        else:
            return suspicious_status
    except Exception as e:
        print(f"Error in check_domain_registration_duration: {e}")
        return suspicious_status

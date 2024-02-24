# 12
import re
from urllib.parse import urlparse, urlunparse
from flask import current_app

def inspect_https_token_in_domain(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        parsed_url = urlparse(url)

        url_without_scheme = urlunparse(parsed_url._replace(scheme=""))

        https_token_pattern = r"https"

        if re.search(https_token_pattern, url_without_scheme):
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in inspect_https_token_in_domain: {e}")
        return suspicious_status

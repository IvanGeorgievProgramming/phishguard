# 25
import tldextract
from flask import current_app

def analyze_statistical_report_ranking(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        extracted_url = tldextract.extract(url)
        top_level_domain = extracted_url.suffix

        dangerous_top_level_domains = [
            "tk", "buzz", "top", "ga", "ml", "info", "cf", "gq", "icu", "wang", "live", "host"
        ]

        if top_level_domain in dangerous_top_level_domains:
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in analyze_statistical_report_ranking: {e}")
        return suspicious_status

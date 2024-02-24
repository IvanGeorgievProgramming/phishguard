# 24
import socket
from urllib.parse import urlparse
from flask import current_app

def check_dns_record_presence(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        domain = urlparse(url).netloc

        try:
            socket.gethostbyname(domain)
            return legitimate_status
        except socket.gaierror:
            return phishing_status
    except Exception as e:
        print(f"Error in check_dns_record_presence: {e}")
        return suspicious_status

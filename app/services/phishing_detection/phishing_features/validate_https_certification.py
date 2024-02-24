# 8
from urllib.parse import urlparse
import socket
import ssl
from flask import current_app

def validate_https_certification(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    https_port = current_app.config["HTTPS_PORT"]
    
    try:
        is_https = url.startswith("https://")

        hostname = urlparse(url).netloc
        issued_by = ""

        if is_https:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, https_port)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    certificate = ssock.getpeercert()
            
            issuer = dict(x[0] for x in certificate["issuer"])
            issued_by = issuer.get("organizationName", "")

        trusted_issuers = ["GeoTrust", "GoDaddy", "Network Solutions", "Thawte", "Comodo", "Doster", "VeriSign", "Google", "IdenTrust", "RapidSSL", "Symantec", "DigiCert", "GlobalSign", "Trustwave"]
        
        if any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and is_https:
            return legitimate_status
        elif any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and not is_https:
            return suspicious_status
        elif not any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and is_https:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in validate_https_certification: {e}")
        return suspicious_status

# 1
import re
from flask import current_app

def check_ip_address_in_domain(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        decimal_ip = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        hex_ip = r"(0x[0-9A-Fa-f]{1,2})"
        octal_ip = r"(0[0-7]{1,3})"

        ip_pattern = (
            rf"(?:(?:{decimal_ip}\.){3}{decimal_ip})" +

            rf"|(?:(?:{hex_ip}\.){3}{hex_ip})" +

            rf"|(?:(?:{octal_ip}\.){3}{octal_ip})" +

            rf"|(?:(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip}))"
        )

        if re.search(ip_pattern, url):
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in check_ip_address_in_domain: {e}")
        return suspicious_status

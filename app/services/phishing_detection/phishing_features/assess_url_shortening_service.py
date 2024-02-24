# 3
from urllib.parse import urlparse
from flask import current_app

def assess_url_shortening_service(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()

        shortening_services = [
            "bit.ly", "rebrand.ly", "branch.io", "short.io", "getsocial.io",
            "oslash.com", "bl.ink", "gshiftlabs.com", "neontools.io", "toinsh.com",
            "foxly.io", "linkjoy.io", "t2mio.com", "geniuslink.com",
            "campaigntracker.io", "utm.io", "pixelme.me", "rocketlink.io",
            "myshorten.com", "pixelfy.me", "sqr.one", "exil.ink", "smarturl.it",
            "clickmeter.com", "boost.link", "tiny.cc", "goqshortener.com",
            "bulkurlshortener.com", "emitto.net", "tinyurl.com", "hop2.page",
            "lnnkin.com", "linklyhq.com", "budurl.com", "switchy.io", "adf.ly",
        ]

        if any(service in domain for service in shortening_services):
            return phishing_status
        else:
            return legitimate_status
    except Exception as e:
        print(f"Error in assess_url_shortening_service: {e}")
        return suspicious_status

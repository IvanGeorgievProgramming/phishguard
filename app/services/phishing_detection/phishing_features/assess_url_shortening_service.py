# 3
from urllib.parse import urlparse

def assess_url_shortening_service(url):
    """
    Summary: 
        Assess if the URL is a shortened URL.

    Description: 
        The domain is extracted from the URL.\n
        A list of known URL shortening services is created.\n
        If the domain contains a URL shortening service, 1 is returned.\n
        If the domain does not contain a URL shortening service, 0 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 1 or 0

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
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
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error in assess_url_shortening_service: {e}")
        return 0.5

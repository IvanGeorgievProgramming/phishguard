# 17
# Possible values: -1, 1
import whois
from urllib.parse import urlparse

def verify_url_host_identity(url):
    """
    Summary: 
        Verifies the identity of the host of the URL.

    Description: 
        The domain is extracted from the URL.\n
        The domain information is retrieved using the whois library.\n
        If the domain information contains a domain name, it is extracted.\n
        If the domain name is present in the URL, -1 is returned.\n
        If the domain name is not present in the URL, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        domain = urlparse(url).netloc
            
        domain_info = whois.whois(domain)
            
        if domain_info.domain_name and any(hostname in url for hostname in domain_info.domain_name):
            return -1
        else:
            return 1
    except Exception as e:
        print(f"Error in verify_url_host_identity: {e}")
        return 0

# 24
# Possible values: -1, 1
import socket
from urllib.parse import urlparse

def check_dns_record_presence(url):
    """
    Summary: 
        Check if the domain has a DNS record.

    Description: 
        The domain is extracted from the URL.\n
        Using try-except, check if the domain has a DNS record.\n
        If the DNS record exists, -1 is returned.\n
        If the DNS record does not exist, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        domain = urlparse(url).netloc

        try:
            socket.gethostbyname(domain)
            return -1
        except socket.gaierror:
            return 1
    except Exception as e:
        print(f"Error in check_dns_record_presence: {e}")
        return 0

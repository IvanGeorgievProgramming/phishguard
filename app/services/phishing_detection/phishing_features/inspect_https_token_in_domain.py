# 12
import re
from urllib.parse import urlparse, urlunparse

def inspect_https_token_in_domain(url):
    """
    Summary: 
        Inspect if the domain contains the HTTPS token.

    Description: 
        The URL is parsed.\n
        The scheme is removed from the URL.\n
        A regular expression is created to match the HTTPS token.\n
        If the HTTPS token is found in the URL without scheme, 1 is returned.\n
        If the HTTPS token is not found in the URL without scheme, 0 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 1 or 0

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        parsed_url = urlparse(url)

        url_without_scheme = urlunparse(parsed_url._replace(scheme=""))

        https_token_pattern = r"https"

        if re.search(https_token_pattern, url_without_scheme):
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error in inspect_https_token_in_domain: {e}")
        return 0.5

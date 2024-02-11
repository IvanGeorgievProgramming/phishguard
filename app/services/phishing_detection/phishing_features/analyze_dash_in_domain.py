# 6
from urllib.parse import urlparse

def analyze_dash_in_domain(url):
    """
    Summary: 
        Analyzes if the domain contains a dash.

    Description: 
        The domain is extracted from the URL.\n
        If the domain contains a dash, 1 is returned.\n
        If the domain does not contain a dash, 0 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 1 or 0

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        if "-" in domain:
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error in analyze_dash_in_domain: {e}")
        return 0.5

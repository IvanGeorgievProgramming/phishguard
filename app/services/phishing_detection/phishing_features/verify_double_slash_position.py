# 5
from urllib.parse import urlparse

def verify_double_slash_position(url):
    """
    Summary: 
        If the URL contains the double slash in the correct position, 0 is returned.

    Description: 
        The URL is parsed.\n
        The scheme is extracted from the URL.\n
        The expected position of the double slash is calculated.\n
        The position of the last double slash is calculated.\n
        If the position of the last double slash is equal to the expected position, 0 is returned.\n
        If the position of the last double slash is not equal to the expected position, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        parsed_url = urlparse(url)
        scheme = parsed_url.scheme

        expected_double_slash_pos = len(scheme) + 1

        last_double_slash = url.rfind("//")

        if last_double_slash == expected_double_slash_pos:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error in verify_double_slash_position: {e}")
        return 0.5

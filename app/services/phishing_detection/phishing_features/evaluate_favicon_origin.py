# 10
# Possible values: -1, 1
from app.utils.url_utils import is_same_domain

def evaluate_favicon_origin(url, favicon):
    """
    Summary: 
        Evaluates the origin of the favicon.

    Description: 
        If the URL of the favicon is empty, -1 is returned.\n
        If the favicon is from the same domain, -1 is returned.\n
        If the favicon is not from the same domain, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.
        favicon (str): The URL of the favicon.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        if favicon == "":
            return -1
        elif is_same_domain(url, favicon):
            return -1
        else:
            return 1
    except Exception as e:
        print(f"Error in evaluate_favicon_origin: {e}")
        return 0

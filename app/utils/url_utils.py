import base64
from urllib.parse import urlparse, urljoin

def generate_route_name(url):
    """
    Summary: 
        Generate a route name for the url.

    Description: 
        Encode the url using base64.\n
        If the encoded url is longer than 100 characters, truncate it to 100 characters.\n
        Return the encoded url.\n

    Arguments: 
        url (str): The url of the website.

    Returns: 
        encoded_url (str): The encoded url.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        encoded_url = base64.urlsafe_b64encode(url.encode()).decode()

        max_length = 100
        if len(encoded_url) > max_length:
            encoded_url = encoded_url[:max_length]

        return encoded_url
    except Exception as e:
        print(f"Error generating route name: {e}")
        return None

def reconstruct_url(encoded_route_name):
    """
    Summary: 
        Reconstruct the url from the encoded url.

    Description: 
        Decode the encoded url using base64.\n
        Return the decoded url.\n

    Arguments: 
        encoded_route_name (str): The encoded url.

    Returns: 
        decoded_url (str): The decoded url.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        decoded_bytes = base64.urlsafe_b64decode(encoded_route_name.encode())
        return decoded_bytes.decode()
    except Exception as e:
        print(f"Error reconstructing url: {e}")
        return None

def is_same_domain(url1, url2):
    """
    Summary: 
        Check if the urls are from the same domain.

    Description: 
        Get the domain name of each url.\n
        If the domain names are the same, return True.\n
        If the domain names are different, return False.\n

    Arguments: 
        url1 (str): The first url.\n
        url2 (str): The second url.\n

    Returns: 
        (bool): Either True or False.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and False is returned.
    """
    try:
        domain_name1 = urlparse(url1).netloc
        domain_name2 = urlparse(url2).netloc

        if domain_name1 == domain_name2:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking if urls are from the same domain: {e}")
        return False

def is_relative_link(url):
    """
    Summary: 
        Check if the url is relative.

    Description: 
        Parse the url.\n
        If the scheme and netloc are empty, return True.\n
        If the scheme and netloc are not empty, return False.\n

    Arguments: 
        url (str): The url.

    Returns: 
        (bool): Either True or False.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and False is returned.
    """
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme == "" and parsed_url.netloc == "":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking if url is relative: {e}")
        return False

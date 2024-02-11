# 23
import whois
from urllib.parse import urlparse
from datetime import datetime, timedelta

def assess_domain_age(url):
    """
    Summary: 
        Calculates the age of the domain of the URL.

    Description: 
        The domain is extracted from the URL.\n
        The domain information is retrieved using the whois library.\n
        If the domain information contains a creation date, it is extracted.\n
        The age of the domain is calculated by subtracting the creation date from the current date.\n
        If the age of the domain is greater than or equal to 6 months, 0 is returned.\n
        If the age of the domain is less than 6 months, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        domain = urlparse(url).netloc
        
        domain_info = whois.whois(domain)
        
        if domain_info.creation_date:
            creation_date = domain_info.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]

            age = datetime.now() - creation_date

            if age >= timedelta(days=6*30):
                return 0
            else:
                return 1
        else:
            return 1
    except Exception as e:
        print(f"Error in assess_domain_age: {e}")
        return 0.5

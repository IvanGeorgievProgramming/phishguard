# 9
# Possible values: -1, 1
import whois

def check_domain_registration_duration(url):
    """
    Summary: 
        Check if the domain registration duration is less than or equal to 1 year.

    Description: 
        Using the whois library, the domain registration date and the domain expiration date are extracted.\n
        If there are multiple registration dates or expiration dates, the first one is used.\n
        If both dates are available, the difference between them is calculated.\n
        If the difference is less than or equal to 365 days, 1 is returned.\n
        If the difference is greater than 365 days, -1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        domain_info = whois.whois(url)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date

        if type(creation_date) is list:
            creation_date = creation_date[0]
        if type(expiration_date) is list:
            expiration_date = expiration_date[0]

        if creation_date is not None and expiration_date is not None:
            paid_duration = expiration_date - creation_date
            if paid_duration.days <= 365:
                return 1
            else:
                return -1
        else:
            return 0
    except Exception as e:
        print(f"Error in check_domain_registration_duration: {e}")
        return 0

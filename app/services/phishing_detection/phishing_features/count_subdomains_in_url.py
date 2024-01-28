# 7
# Possible values: -1, 0, 1
import tldextract

def count_subdomains_in_url(url):
    """
    Summary: 
        Counts the number of subdomains in the URL.

    Description: 
        The URL is extracted using tldextract.
        If the URL has a subdomain and the subdomain is not "www", the number of subdomains is counted.\n
        If the URL has no subdomain or the subdomain is "www", the number of subdomains is 0.\n
        If the number of subdomains is less than or equal to 1, -1 is returned.\n
        If the number of subdomains is equal to 2, 0 is returned.\n
        If the number of subdomains is greater than 2, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1, 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        extracted_url = tldextract.extract(url)
        subdomain = extracted_url.subdomain

        if subdomain and subdomain != "www":
            subdomain_count = subdomain.count(".") + 1
        else:
            subdomain_count = 0
        
        if subdomain_count <= 1:
            return -1
        elif subdomain_count == 2:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error in count_subdomains_in_url: {e}")
        return 0

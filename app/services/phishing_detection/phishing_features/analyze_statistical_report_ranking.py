# 25
import tldextract

def analyze_statistical_report_ranking(url):
    """
    Summary: 
        Analyze the statistical report ranking of the top-level domain of the URL.

    Description: 
        The top-level domain is extracted from the URL.\n
        If the top-level domain is in the list of dangerous top-level domains, 1 is returned.\n
        If the top-level domain is not in the list of dangerous top-level domains, 0 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 1 or 0

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        extracted_url = tldextract.extract(url)
        top_level_domain = extracted_url.suffix

        dangerous_top_level_domains = [
            "tk", "buzz", "top", "ga", "ml", "info", "cf", "gq", "icu", "wang", "live", "host"
        ]

        if top_level_domain in dangerous_top_level_domains:
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error in analyze_statistical_report_ranking: {e}")
        return 0.5

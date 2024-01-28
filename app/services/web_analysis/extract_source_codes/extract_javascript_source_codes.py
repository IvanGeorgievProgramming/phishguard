import requests
from bs4 import BeautifulSoup

from app.utils.url_utils import is_relative_link, is_same_domain

def extract_javascript_source_codes(html_source_codes):
    """
    Summary: 
        Extracts JavaScript source codes from a list of HTML source codes.

    Description: 
        Creates a set of processed scripts and a list of JavaScript source codes.\n
        For each HTML source code, it creates a BeautifulSoup object, and for each script in the BeautifulSoup object, it gets the src attribute.\n
        If the src attribute exists, it checks if the link is not relative and is from the same domain.\n
        If the link is not relative and is from the same domain, it gets the page source code using Requests, and if the response status code is 200, it adds the page source code to the list of JavaScript source codes.\n
        If the src attribute does not exist, it gets the string of the script, and if the string exists and has not been processed, it adds the string to the list of JavaScript source codes.\n
        Returns the list of JavaScript source codes.\n

    Arguments: 
        html_source_codes (list): The list of HTML source codes.

    Returns: 
        javascript_source_codes (list): The list of JavaScript source codes.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        javascript_source_codes = []
        processed_scripts = set()

        for html_code in html_source_codes:
            soup = BeautifulSoup(html_code, "html.parser")
            
            for script in soup.find_all("script"):
                content = ""

                src = script.get("src")
                if src:
                    if not is_relative_link(src) and is_same_domain(src, soup.base_url):
                        try:
                            response = requests.get(src)
                            
                            if response.status_code == 200:
                                content = response.text
                        except requests.RequestException as e:
                            print(f"Error fetching JavaScript file {src}: {e}")
                else:
                    content = script.string if script.string else ""

                if content and content not in processed_scripts:
                    processed_scripts.add(content)
                    javascript_source_codes.append(content)

        return javascript_source_codes
    except Exception as e:
        print("Error extracting JavaScript source codes: " + str(e))
        return None
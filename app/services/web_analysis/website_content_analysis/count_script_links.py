from app.utils.url_utils import is_relative_link, is_same_domain

def count_script_links(soup, base_url):
    """
    Summary: 
        Count all script tag links in the soup object and return the count of internal, external and relative links.

    Description: 
        Create a set to store all processed script tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external and relative script tag links count.\n
        Find all script tags in the soup object.\n
        For each script tag, get the script tag link.\n
        If the script tag link is not in the processed script tag links set, add it to the set.\n
        If the script tag link is relative, increment relative script tag links count.\n
        If the script tag link is internal, increment internal script tag links count.\n
        If the script tag link is external, increment external script tag links count.\n
        Return internal, external and relative script tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_script_links_count (int): The count of internal script tag links.
        external_script_links_count (int): The count of external script tag links.
        relative_script_links_count (int): The count of relative script tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_script_links = set()
        internal_script_links_count = 0
        external_script_links_count = 0
        relative_script_links_count = 0

        script_tags = soup.find_all("script", src=True)
        for script_tag in script_tags:
            script_link = script_tag["src"]
            if script_link and script_link not in processed_script_links:
                processed_script_links.add(script_link)
                if is_relative_link(script_link):
                    relative_script_links_count += 1
                elif is_same_domain(script_link, base_url):
                    internal_script_links_count += 1
                else:
                    external_script_links_count += 1

        return internal_script_links_count, external_script_links_count, relative_script_links_count
        
    except Exception as e:
        print("Error counting script links: " + str(e))
        return 0, 0, 0
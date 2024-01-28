from app.utils.url_utils import is_relative_link, is_same_domain

def count_a_links(soup, base_url):
    """
    Summary: 
        Count all a tag links in the soup object and return the count of internal, external and relative a tag links.

    Description: 
        Create a set to store all processed a tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external and relative a tag links count.\n
        Find all a tags in the soup object.\n
        For each a tag, get the a tag link.\n
        If the a tag link is not in the processed a tag links set, add it to the set.\n
        If the a tag link is relative, increment relative a tag links count.\n
        If the a tag link is internal, increment internal a tag links count.\n
        If the a tag link is external, increment external a tag links count.\n
        Return internal, external and relative a tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_a_links_count (int): The count of internal a tag links.
        external_a_links_count (int): The count of external a tag links.
        relative_a_links_count (int): The count of relative a tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_a_links = set()
        internal_a_links_count = 0
        external_a_links_count = 0
        relative_a_links_count = 0

        a_tags = soup.find_all("a", href=True)
        for a_tag in a_tags:
            a_link = a_tag["href"]
            if a_link and a_link not in processed_a_links:
                processed_a_links.add(a_link)
                if is_relative_link(a_link):
                    relative_a_links_count += 1
                elif is_same_domain(a_link, base_url):
                    internal_a_links_count += 1
                else:
                    external_a_links_count += 1

        return internal_a_links_count, external_a_links_count, relative_a_links_count
        
    except Exception as e:
        print("Error counting a tag links: " + str(e))
        return 0, 0, 0
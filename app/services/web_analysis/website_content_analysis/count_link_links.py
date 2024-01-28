from app.utils.url_utils import is_relative_link, is_same_domain

def count_link_links(soup, base_url):
    """
    Summary: 
        Count all link tag links in the soup object and return the count of internal, external and relative links.

    Description: 
        Create a set to store all processed link tag links to avoid counting the same link tag multiple times.\n
        Create variables to store internal, external and relative link tag links count.\n
        Find all link tags in the soup object.\n
        For each link tag, get the link tag link.\n
        If the link tag link is not in the processed link tag links set, add it to the set.\n
        If the link tag link is relative, increment relative link tag links count.\n
        If the link tag link is internal, increment internal link tag links count.\n
        If the link tag link is external, increment external link tag links count.\n
        Return internal, external and relative link tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_link_links_count (int): The count of internal link tag links.
        external_link_links_count (int): The count of external link tag links.
        relative_link_links_count (int): The count of relative link tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_link_links = set()
        internal_link_links_count = 0
        external_link_links_count = 0
        relative_link_links_count = 0

        link_tags = soup.find_all("link", href=True)
        for link_tag in link_tags:
            link_link = link_tag["href"]
            if link_link and link_link not in processed_link_links:
                processed_link_links.add(link_link)
                if is_relative_link(link_link):
                    relative_link_links_count += 1
                elif is_same_domain(link_link, base_url):
                    internal_link_links_count += 1
                else:
                    external_link_links_count += 1

        return internal_link_links_count, external_link_links_count, relative_link_links_count
        
    except Exception as e:
        print("Error counting link tag links: " + str(e))
        return 0, 0, 0
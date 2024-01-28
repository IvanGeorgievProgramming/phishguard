from app.utils.url_utils import is_relative_link, is_same_domain

def count_img_links(soup, base_url):
    """
    Summary: 
        Count all img tag links in the soup object and return the count of internal, external and relative links.

    Description: 
        Create a set to store all processed img tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external and relative img tag links count.\n
        Find all img tags in the soup object.\n
        For each img tag, get the img tag link.\n
        If the img tag link is not in the processed img tag links set, add it to the set.\n
        If the img tag link is relative, increment relative img tag links count.\n
        If the img tag link is internal, increment internal img tag links count.\n
        If the img tag link is external, increment external img tag links count.\n
        Return internal, external and relative img tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_img_links_count (int): The count of internal img tag links.
        external_img_links_count (int): The count of external img tag links.
        relative_img_links_count (int): The count of relative img tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_img_links = set()
        internal_img_links_count = 0
        external_img_links_count = 0
        relative_img_links_count = 0

        img_tags = soup.find_all("img", src=True)
        for img_tag in img_tags:
            img_link = img_tag["src"]
            if img_link and img_link not in processed_img_links:
                processed_img_links.add(img_link)
                if is_relative_link(img_link):
                    relative_img_links_count += 1
                elif is_same_domain(img_link, base_url):
                    internal_img_links_count += 1
                else:
                    external_img_links_count += 1

        return internal_img_links_count, external_img_links_count, relative_img_links_count
        
    except Exception as e:
        print("Error counting img tag links: " + str(e))
        return 0, 0, 0
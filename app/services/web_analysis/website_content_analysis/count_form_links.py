from app.utils.url_utils import is_relative_link, is_same_domain

def count_form_links(soup, base_url):
    """
    Summary: 
        Count all form tag links in the soup object and return the count of blank, internal, external and relative links.

    Description: 
        Create a set to store all processed form tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external, relative and blank form tag links count.\n
        Find all form tags in the soup object.\n
        For each form tag, get the form tag link.\n
        If the form tag link is not in the processed form tag links set, add it to the set.\n
        If the form tag link is relative, increment relative form tag links count.\n
        If the form tag link is internal, increment internal form tag links count.\n
        If the form tag link is external, increment external form tag links count.\n
        If the form tag link is blank, increment blank form tag links count.\n
        Return internal, external, relative and blank form tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        blank_form_links_count (int): The count of blank form tag links.
        internal_form_links_count (int): The count of internal form tag links.
        external_form_links_count (int): The count of external form tag links.
        relative_form_links_count (int): The count of relative form tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0, 0 is returned.
    """
    try:
        processed_form_links = set()
        blank_form_links_count = 0
        internal_form_links_count = 0
        external_form_links_count = 0
        relative_form_links_count = 0

        form_tags = soup.find_all("form", action=True)
        for form_tag in form_tags:
            form_link = form_tag["action"]
            if form_link and form_link not in processed_form_links:
                processed_form_links.add(form_link)
                if is_relative_link(form_link):
                    if form_link == "":
                        blank_form_links_count += 1
                    else:
                        relative_form_links_count += 1
                elif is_same_domain(form_link, base_url):
                    internal_form_links_count += 1
                else:
                    external_form_links_count += 1

        return blank_form_links_count, internal_form_links_count, external_form_links_count, relative_form_links_count
        
    except Exception as e:
        print("Error counting form links: " + str(e))
        return 0, 0, 0, 0
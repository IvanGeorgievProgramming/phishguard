def find_favicon(soup):
    """
    Summary: 
        Find the favicon of the website.

    Description: 
        Find all link tags in the soup object.\n
        For each link tag, if the link tag has a rel attribute and the value of the rel attribute contains "icon", return the href attribute value.\n
        Else, return an empty string.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.

    Returns: 
        favicon (str): The favicon of the website.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and an empty string is returned.
    """
    try:
        link_tags = soup.find_all("link")
        for link_tag in link_tags:
            if link_tag.get("rel") and "icon" in link_tag["rel"]:
                return link_tag.get("href")
        return ""
    except Exception as e:
        print("Error finding favicon: " + str(e))
        return ""

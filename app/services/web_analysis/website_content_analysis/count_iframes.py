def count_iframes(soup):
    """
    Summary: 
        Count the number of hidden and visible iframe tags in the soup object.\n

    Description: 
        Create variables to store hidden and visible iframe tags count.\n
        Find all iframe tags in the soup object.\n
        For each iframe tag, get the iframe tag style.\n
        If the iframe tag style contains "display: none" or "visibility: hidden", increment hidden iframe tags count.\n
        Else, increment visible iframe tags count.\n
        Return hidden and visible iframe tags count.\n

    Arguments: 
        soup: The soup object of the website content.

    Returns: 
        hidden_iframes_count (int): The count of hidden iframe tags.
        visible_iframes_count (int): The count of visible iframe tags.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0 is returned.
    """
    try:
        hidden_iframes_count = 0
        visible_iframes_count = 0

        iframe_tags = soup.find_all("iframe")
        for iframe_tag in iframe_tags:
            style = iframe_tag.get("style")
            if "display: none" in style or "visibility: hidden" in style:
                hidden_iframes_count += 1
            else:
                visible_iframes_count += 1

        return hidden_iframes_count, visible_iframes_count

    except Exception as e:
        print("Error counting iframes: " + str(e))
        return 0, 0
# 16
def validate_sfh_domain_relevance(form_blank_links_count, form_external_links_count):
    """
    Summary: 
        Validates the domain relevance of the links in the form tags.

    Description: 
        If there are blank links in the form tags, 1 is returned.\n
        If there are external links in the form tags, 0.5 is returned.\n
        If there are no blank or external links in the form tags, 0 is returned.\n

    Arguments: 
        form_blank_links_count (int): The number of blank links in all form tags.
        form_external_links_count (int): The number of external links in all form tags.

    Returns: 
        (int): Either 0, 0.5 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        if form_blank_links_count > 0:
            return 1
        elif form_external_links_count > 0:
            return 0.5
        else:
            return 0
    except Exception as e:
        print(f"Error in validate_sfh_domain_relevance: {e}")
        return 0.5

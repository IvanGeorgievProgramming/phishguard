# 15
def check_tag_links_domain_congruence(script_internal_links_count, script_external_links_count, script_relative_links_count, link_internal_links_count, link_external_links_count, link_relative_links_count):
    """
    Summary: 
        Calculates the ratio of internal, external and relative links in the script and link tags and returns a value based on the ratio.

    Description: 
        Calculates the total number of internal, external and relative links in the script and link tags.\n
        If there are no external links, then the value returned is 0.\n
        A ratio is calculated based on the number of internal, external and relative links.\n
        If the ratio is less than 17%, then 0 is returned.\n
        If the ratio is between 17% and 81%, then 0.5 is returned.\n
        If the ratio is greater than 81%, then 1 is returned.\n

    Arguments: 
        script_internal_links_count (int): The number of internal links in all script tags.
        script_external_links_count (int): The number of external links in all script tags.
        script_relative_links_count (int): The number of relative links in all script tags.
        link_internal_links_count (int): The number of internal links in all link tags.
        link_external_links_count (int): The number of external links in all link tags.
        link_relative_links_count (int): The number of relative links in all link tags.

    Returns: 
        (int): Either 0, 0.5 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        internal_links_count = script_internal_links_count + link_internal_links_count
        external_links_count = script_external_links_count + link_external_links_count
        relative_links_count = script_relative_links_count + link_relative_links_count

        if external_links_count == 0:
            return 0
        
        ratio = (internal_links_count + relative_links_count) / external_links_count
        percentage = ratio * 100

        if percentage < 17.0:
            return 0
        elif percentage >= 17.0 and percentage <= 81.0:
            return 0.5
        else:
            return 1
    except Exception as e:
        print(f"Error in check_tag_links_domain_congruence: {e}")
        return 0.5

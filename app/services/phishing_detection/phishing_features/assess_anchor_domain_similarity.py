# 14
def assess_anchor_domain_similarity(a_internal_links_count, a_external_links_count, a_relative_links_count):
    """
    Summary: 
        Calculates the ratio of internal, external and relative links in the anchor tag and returns a value based on the ratio.

    Description: 
        If there are no external links, then the value returned is 0.\n
        A ratio is calculated based on the number of internal, external and relative links.\n
        If the ratio is less than 31%, then 0 is returned.\n
        If the ratio is between 31% and 67%, then 0.5 is returned.\n
        If the ratio is greater than 67%, then 1 is returned.\n

    Arguments: 
        a_internal_links_count (int): The number of internal links in all anchor tags.
        a_external_links_count (int): The number of external links in all anchor tags.
        a_relative_links_count (int): The number of relative links in all anchor tags.

    Returns: 
        (int): Either 0, 0.5 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        if a_external_links_count == 0:
            return 0
        
        ratio = (a_internal_links_count + a_relative_links_count) / a_external_links_count
        percentage = ratio * 100

        if percentage < 31.0:
            return 0
        elif percentage >= 31.0 and percentage <= 67.0:
            return 0.5
        else:
            return 1
        
    except Exception as e:
        print(f"Error in assess_anchor_domain_similarity: {e}")
        return 0.5

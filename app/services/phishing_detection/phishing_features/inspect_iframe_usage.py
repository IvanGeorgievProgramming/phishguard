# 22
# Possible values: -1, 1

def inspect_iframe_usage(iframe_hidden_count, iframe_visible_count):
    """
    Summary: 
        Inspect if the website uses iframes.

    Description: 
        If the iframe_hidden_count or the iframe_visible_count is greater than 0, 1 is returned.\n
        If there are no iframes, -1 is returned.\n

    Arguments: 
        iframe_hidden_count (int): The number of hidden iframes.
        iframe_visible_count (int): The number of visible iframes.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        if iframe_hidden_count > 0 or iframe_visible_count > 0:
            return 1
        else:
            return -1
    except Exception as e:
        print(f"Error in inspect_iframe_usage: {e}")
        return 0

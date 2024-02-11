# 4
def inspect_at_symbol_in_url(url):
    """
    Summary: 
        Inspect if the URL has an @ symbol in it.

    Description: 
        If the URL has an @ symbol in it, return 1.\n
        If the URL does not have an @ symbol in it, return 0.\n
    
    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        if "@" in url:
            return 1
        else:
            return 0
    except Exception as e:
        print(f"Error in inspect_at_symbol_in_url: {e}")
        return 0.5

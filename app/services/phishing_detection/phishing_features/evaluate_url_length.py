# 2
# Possible values: -1, 0, 1
def evaluate_url_length(url):
    """
    Summary: 
        Evaluate the length of the URL.

    Description: 
        The length of the URL is calculated.\n
        If the length is less than 54, -1 is returned.\n
        If the length is greater than or equal to 54 and less than or equal to 75, 0 is returned.\n
        If the length is greater than 75, 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1, 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        length = len(url)

        if length < 54:
            return -1
        elif length >= 54 and length <= 75:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error in evaluate_url_length: {e}")
        return 0

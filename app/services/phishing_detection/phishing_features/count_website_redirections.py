# 18
def count_website_redirections(redirections_count):
    """
    Summary: 
        Count the number of redirections in the URL.

    Description: 
        If the number of redirections is less than or equal to 1, 0 is returned.\n
        If the number of redirections is greater than or equal to 2 and less than 4, 0.5 is returned.\n
        If the number of redirections is greater than or equal to 4, 1 is returned.\n

    Arguments: 
        redirections_count (int): The number of redirections in the URL.

    Returns: 
        (int): Either 0, 0.5 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        if redirections_count <= 1:
            return 0
        elif redirections_count >= 2 and redirections_count < 4:
            return 0.5
        else:
            return 1
    except Exception as e:
        print(f"Error in count_website_redirections: {e}")
        return 0.5

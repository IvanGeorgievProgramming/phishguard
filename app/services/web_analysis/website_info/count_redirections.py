import requests

def count_redirections(url):
    """
    Summary: 
        Count the number of redirections for a given URL.

    Description: 
        Use the requests library to get the URL response.\n
        Get the number of redirections from the response history.\n
        Return the number of redirections.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        redirections_count (int): The count of redirections.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        response = requests.get(url)
        redirections_count = len(response.history)
        return redirections_count
    except Exception as e:
        print("Error counting redirections: " + str(e))
        return 0
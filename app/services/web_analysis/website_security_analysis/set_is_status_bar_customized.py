import re

def set_is_status_bar_customized(javascript_source_codes):
    """
    Summary: 
        Check if the status bar is customized.

    Description: 
        Create a pattern to check if the status bar is customized.\n
        For each javascript source code, if the javascript source code matches the pattern, return True.\n
        If no javascript source code matches the pattern return False.\n

    Arguments: 
        javascript_source_codes (list): The list of JavaScript source codes.

    Returns: 
        (bool): Either True or False.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        pattern = re.compile(r"onmouseover.*?window\.status\s*=", re.IGNORECASE | re.DOTALL)

        for javascript_source_code in javascript_source_codes:
            if javascript_source_code and pattern.search(javascript_source_code):
                return True
            
        return False
    except Exception as e:
        print(f"Error while checking if status bar is customized: {e}")
        return None

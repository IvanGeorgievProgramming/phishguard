# 20
# Possible values: -1, 1
import re

def detect_right_click_disablement(is_right_click_disabled):
    """
    Summary: 
        Detects if right click is disabled on the webpage.

    Description: 
        If the is_right_click_disabled is True, 1 is returned.\n
        If the is_right_click_disabled is False, -1 is returned.\n

    Arguments: 
        is_right_click_disabled (bool): A boolean value indicating if right click is disabled on the webpage.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        if is_right_click_disabled:
            return 1
        else:
            return -1
    except Exception as e:
        print(f"Error in detect_right_click_disablement: {e}")
        return 0

# 21
# Possible values: -1, 1

def evaluate_pop_up_content(is_popup_asking_personal_info):
    """
    Summary: 
        Evaluate if the pop-up is asking for personal information or not.

    Description: 
        If the is_popup_asking_personal_info is True, 1 is returned.\n
        If the is_popup_asking_personal_info is False, -1 is returned.\n

    Arguments: 
        is_popup_asking_personal_info (bool): A boolean value indicating if the pop-up is asking for personal information or not.

    Returns: 
        (int): Either -1 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        if is_popup_asking_personal_info:
            return 1
        else:
            return -1
    except Exception as e:
        print(f"Error in evaluate_pop_up_content: {e}")
        return 0

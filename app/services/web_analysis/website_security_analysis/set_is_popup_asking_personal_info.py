import re

def set_is_popup_asking_personal_info(javascript_source_codes):
    """
    Summary: 
        Check if a popup is asking for personal information.

    Description: 
        Create a list of patterns to check if a popup is asking for personal information.\n
        For each javascript source code, if the javascript source code matches any of the patterns, return True.\n
        If no javascript source code matches any of the patterns return False.\n

    Arguments: 
        javascript_source_codes (list): The list of JavaScript source codes.

    Returns: 
        (bool): Either True or False.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        popup_patterns = [
            re.compile(r"(window\.(alert|prompt|confirm)\()|(document\.getElementById\('.*'\)\.innerHTML\s*=)"),
            re.compile(r"<input\s+type=['\"]text['\"]")
        ]
        
        for js_code in javascript_source_codes:
            if js_code:
                if any(pattern.search(js_code) for pattern in popup_patterns):
                    if re.search(r"<input\s+type=['\"]text['\"]", js_code, re.IGNORECASE | re.DOTALL):
                        return True

        return False
    except Exception as e:
        print(f"Error while checking if popup is asking for personal info: {e}")
        return None

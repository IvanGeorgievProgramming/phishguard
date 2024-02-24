import re

def set_is_status_bar_customized(javascript_source_codes):
    try:
        pattern = re.compile(r"onmouseover.*?window\.status\s*=", re.IGNORECASE | re.DOTALL)

        for javascript_source_code in javascript_source_codes:
            if javascript_source_code and pattern.search(javascript_source_code):
                return True
            
        return False
    except Exception as e:
        print(f"Error while checking if status bar is customized: {e}")
        return None

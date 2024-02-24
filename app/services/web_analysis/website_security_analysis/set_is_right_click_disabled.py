import re

def set_is_right_click_disabled(javascript_source_codes):
    try:
        pattern = re.compile(r"event\.button\s*==\s*2.*?(preventDefault\(\)|return\s+false)", re.IGNORECASE | re.DOTALL)

        for javascript_source_code in javascript_source_codes:
            if javascript_source_code and pattern.search(javascript_source_code):
                return True
            
        return False
    except Exception as e:
        print(f"Error while checking if right click is disabled: {e}")
        return None

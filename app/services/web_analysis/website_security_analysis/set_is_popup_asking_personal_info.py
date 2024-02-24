import re

def set_is_popup_asking_personal_info(javascript_source_codes):
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

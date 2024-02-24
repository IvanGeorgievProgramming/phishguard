import requests
from bs4 import BeautifulSoup
from flask import current_app

from app.utils.url_utils import is_relative_link, is_same_domain

def extract_javascript_source_codes(html_source_codes):
    http_status_ok = current_app.config["HTTP_STATUS_OK"]
    
    try:
        javascript_source_codes = []
        processed_scripts = set()

        for html_code in html_source_codes:
            soup = BeautifulSoup(html_code, "html.parser")
            
            for script in soup.find_all("script"):
                content = ""

                src = script.get("src")
                if src:
                    if not is_relative_link(src) and is_same_domain(src, soup.base_url):
                        try:
                            response = requests.get(src)
                            
                            if response.status_code == http_status_ok:
                                content = response.text
                        except requests.RequestException as e:
                            print(f"Error fetching JavaScript file {src}: {e}")
                else:
                    content = script.string if script.string else ""

                if content and content not in processed_scripts:
                    processed_scripts.add(content)
                    javascript_source_codes.append(content)

        return javascript_source_codes
    except Exception as e:
        print("Error extracting JavaScript source codes: " + str(e))
        return None

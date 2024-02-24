import requests
from bs4 import BeautifulSoup

from app.utils.url_utils import is_same_domain, is_relative_link

def extract_html_quick_analysis(url, driver):
    processed_urls = set([url])
    html_source_codes = []

    driver.get(url)
    original_soup = BeautifulSoup(driver.page_source, "html.parser")
    html_source_codes.append(original_soup.prettify())

    for link in original_soup.find_all("a", href=True):
        href = link.get("href")
        if not is_relative_link(href) and is_same_domain(href, url) and href not in processed_urls:
            linked_response = requests.get(href)
            linked_soup = BeautifulSoup(linked_response.text, "html.parser")
            html_source_codes.append(linked_soup.prettify())
            processed_urls.add(href)

    return html_source_codes

from bs4 import BeautifulSoup

from app.utils.url_utils import is_same_domain, is_relative_link

def extract_html_complete_site_analysis(url, driver):
    urls_to_scrape = set([url])
    processed_urls = set()
    html_source_codes = []

    while urls_to_scrape:
        current_url = urls_to_scrape.pop()
        driver.get(current_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        html_source_codes.append(soup.prettify())
        processed_urls.add(current_url)

        for link in soup.find_all("a", href=True):
            href = link.get("href")
            if not is_relative_link(href) and is_same_domain(href, url) and href not in processed_urls:
                urls_to_scrape.add(href)

    return html_source_codes

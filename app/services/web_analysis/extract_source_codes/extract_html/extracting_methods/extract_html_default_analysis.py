from bs4 import BeautifulSoup

def extract_html_default_analysis(url, driver):
    html_source_codes = []

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    html_source_codes.append(soup.prettify())

    return html_source_codes

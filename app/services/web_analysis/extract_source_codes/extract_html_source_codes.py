import requests
from bs4 import BeautifulSoup

from app.utils.url_utils import is_same_domain, is_relative_link

def extract_html_source_codes(url, option, driver):
    """
    Summary: 
        Extracts the HTML source code of the given URL using the given option.

    Description: 
        Creates a set of URLs to scrape, a set of processed URLs, and a list of HTML source codes.\n
        If the selected otion is 1, while there are URLs to scrape, it pops the current URL from the set of URLs to scrape, gets the page source code using Selenium, adds the page source code to the list of HTML source codes, and adds the current URL to the set of processed URLs.
        Then, for each link in the page source code, it gets the href attribute, and if the link is not relative, is from the same domain, and has not been processed, it adds the link to the set of URLs to scrape.\n
        If the selected option is 2, it gets the page source code using Selenium, adds the page source code to the list of HTML source codes, and adds the current URL to the set of processed URLs.
        Then, for each link in the page source code, it gets the href attribute, and if the link is not relative, is from the same domain, and has not been processed, it gets the page source code using Requests, adds the page source code to the list of HTML source codes, and adds the link to the set of processed URLs.\n
        If the selected option is 3, it gets the page source code using Selenium, adds the page source code to the list of HTML source codes, and adds the current URL to the set of processed URLs.
        Then, for each link in the page source code, it gets the href attribute, and if the link is not relative, is from the same domain, and has not been processed, it gets the page source code using Selenium, adds the page source code to the list of HTML source codes, and adds the link to the set of processed URLs.\n
        If the selected option is 4, it gets the page source code using Selenium, adds the page source code to the list of HTML source codes, and adds the current URL to the set of processed URLs.
        Then, for each link in the page source code, it gets the href attribute, and if the link is not relative, is from the same domain, and has not been processed, it gets the page source code using Requests, adds the page source code to the list of HTML source codes, and adds the link to the set of processed URLs.\n
        If the selected option is not 1, 2, 3, or 4, it gets the page source code using Selenium and adds the page source code to the list of HTML source codes.\n
        Returns the list of HTML source codes.\n
    Arguments: 
        url (str): The URL to extract the HTML source code from.
        option (int): The option to use to extract the HTML source code.
        driver (WebDriver): The Selenium WebDriver to use to extract the HTML source code.

    Returns: 
        html_source_codes (list): The list of HTML source codes.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        urls_to_scrape = set([url])
        processed_urls = set()
        html_source_codes = []

        # * Option 1: Scraping all links with the same domain using Selenium
        if option == 1:
            while urls_to_scrape:
                current_url = urls_to_scrape.pop()
                driver.get(current_url)
                soup = BeautifulSoup(driver.page_source, "html.parser")

                html_source_codes.append(soup.prettify())
                processed_urls.add(current_url)

                for link in soup.find_all("a", href=True):
                    href = link.get("href")

                    if not is_relative_link(href):
                        if is_same_domain(href, url) and href not in processed_urls:
                            urls_to_scrape.add(href)

        # * Option 2: Scraping all links with the same domain, original with Selenium, others with Requests
        elif option == 2:
            driver.get(url)
            original_soup = BeautifulSoup(driver.page_source, "html.parser")
            html_source_codes.append(original_soup.prettify())
            processed_urls.add(url)

            for link in original_soup.find_all("a", href=True):
                href = link.get("href")

                if not is_relative_link(href):
                    if is_same_domain(href, url) and href not in processed_urls:
                        linked_response = requests.get(href)
                        linked_soup = BeautifulSoup(linked_response.text, "html.parser")
                        processed_urls.add(href)
                        html_source_codes.append(linked_soup.prettify())

        # * Option 3: Scraping connected links with the same domain using Selenium
        elif option == 3:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            html_source_codes.append(soup.prettify())
            processed_urls.add(url)

            for link in soup.find_all("a", href=True):
                href = link.get("href")

                if not is_relative_link(href):
                    if is_same_domain(href, url) and href not in processed_urls:
                        driver.get(href)
                        linked_soup = BeautifulSoup(driver.page_source, "html.parser")
                        html_source_codes.append(linked_soup.prettify())
                        processed_urls.add(href)

        # * Option 4: Scraping connected links with the same domain, original with Selenium, others with Requests
        elif option == 4:
            driver.get(url)
            original_soup = BeautifulSoup(driver.page_source, "html.parser")
            html_source_codes.append(original_soup.prettify())
            processed_urls.add(url)

            for link in original_soup.find_all("a", href=True):
                href = link.get("href")

                if not is_relative_link(href):
                    if is_same_domain(href, url) and href not in processed_urls:
                        linked_response = requests.get(href)
                        linked_soup = BeautifulSoup(linked_response.text, "html.parser")
                        html_source_codes.append(linked_soup.prettify())
                        processed_urls.add(href)
        
        # * Default: Scraping just the original URL with Selenium
        else:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            html_source_codes.append(soup.prettify())

        return html_source_codes

    except Exception as e:
        print("Error extracting HTML source code: " + str(e))
        return None

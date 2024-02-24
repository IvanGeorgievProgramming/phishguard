from flask import flash
from urllib.parse import urlparse

from app.services.web_analysis.setup_driver import setup_driver

def validate_and_check_website_url(website_url):
    if not website_url:
        flash("Website URL is required.", "error")
        return False

    parsed_url = urlparse(website_url)
    if not (parsed_url.scheme and parsed_url.netloc):
        flash("Invalid website URL format.", "error")
        return False

    driver = setup_driver()
    if driver is None:
        flash("Failed to initialize the website check.", "error")
        return False

    try:
        driver.get(website_url)
        driver.quit()
    except Exception as e:
        flash("Could not access the website. Please make sure the URL is correct and the site is online.", "error")
        driver.quit()
        return False

    return True

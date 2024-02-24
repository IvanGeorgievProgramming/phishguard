from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Your User Agent String")

        chrome_service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        return driver
    except Exception as e:
        print(f"Error setting up driver: {e}")
        return None

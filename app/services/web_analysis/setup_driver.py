from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """
    Summary: 
        Setup the Chrome driver.

    Description: 
        Create a ChromeOptions object.\n
        Add the headless argument to the ChromeOptions object.\n
        Add the no-sandbox argument to the ChromeOptions object.\n
        Add the disable-dev-shm-usage argument to the ChromeOptions object.\n
        Add the user-agent argument to the ChromeOptions object.\n
        Create a ChromeService object and pass the ChromeDriverManager().install() to it.\n
        Create a ChromeDriver object and pass the ChromeService and ChromeOptions objects to it.\n
        Return the ChromeDriver object.\n

    Arguments: 
        None: No arguments are required.

    Returns: 
        driver (ChromeDriver): The Chrome driver.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
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

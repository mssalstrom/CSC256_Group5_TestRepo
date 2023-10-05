from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.safari import SafariDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
import time
global driver


def initialize_driver(browser_type):
    global driver  # Global variable to store the browser driver
    if browser_type == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_type == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_type == 'safari':
        driver = webdriver.Safari(service=SafariService(SafariDriverManager().install()))
    return driver


def navigate_to_url(url):
    driver.get(url)  # Global variable driver calls the get() function to open the url
    time.sleep(5)



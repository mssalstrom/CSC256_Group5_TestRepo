from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def initialize_driver(browser_type):
    global driver  # Global variable to store the browser driver
    if browser_type == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver
    elif browser_type == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        return driver


def navigate_to_url(url):
    driver.get(url)  # Global variable driver calls the get() function to open the url
    while True:
        pass


def validate_page_title(expected_title):
    title = driver.title
    if title == expected_title:
        print('TRUE')
        return True


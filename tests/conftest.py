import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage
from decouple import config

@pytest.fixture(scope='session')
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(email= config('email'),password = config('password'))
    yield driver

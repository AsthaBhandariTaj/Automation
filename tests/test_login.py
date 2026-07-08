import pytest
from pages.login import LoginPage
from decouple import config
import time

class TestLogin:
    def test_valid_login(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(email= config('email'),password = config('password'))
        time.sleep(5)

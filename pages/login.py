from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = config("login_url")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get(self.url)

    def login(self, email : str, password: str):
        wait = WebDriverWait(self.driver , 10)

        email_field = wait.until(EC.visibility_of_element_located(self.email_input))
        email_field.send_keys(email)

        password_field = wait.until(EC.visibility_of_element_located(self.password_input))
        password_field.send_keys(password)

        login_button = wait.until(EC.visibility_of_element_located(self.login_button))
        login_button.click()

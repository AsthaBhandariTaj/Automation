from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Issue:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/stocktransfer/create?store_status=department&is_sub_store=1"
        self.list_url = "https://uattuth.dolphin.com.np/ims/inventory/stocktransfer/index/main?store_type_for_list=department"
        self.to_store = (By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        self.enter_to_store = (By.XPATH,"//input[@name='pos']")
        self.requisition = (By.XPATH,"//button[@id='requisitionListBtn']")
        self.load = (By.XPATH,"//button[normalize-space()='Load']")
        self.transfer = (By.XPATH,"//button[@id='transfer']")
        self.ok = (By.XPATH,"//button[normalize-space()='OK']")
        self.approve_btn = (By.XPATH,"//tbody/tr[1]/td[8]/button[4]")
        
    def open(self):
        self.driver.get(self.url)

    def open_list(self):
        self.driver.get(self.list_url)
    
    def issue(self):
        wait = WebDriverWait(self.driver, 10)

        to_store_element = wait.until(EC.visibility_of_element_located(self.to_store))
        to_store_element.click()
        time.sleep(2)

        enter_store_element = wait.until(EC.visibility_of_element_located(self.enter_to_store))
        enter_store_element.send_keys("account")
        time.sleep(2)
        enter_store_element.send_keys(Keys.ENTER)
        time.sleep(2)

        requisition = wait.until(EC.visibility_of_element_located(self.requisition))
        requisition.click()
        time.sleep(2)

        check_box = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//input[contains(@class, 'checkboxClick')]")))
        # check_box.click()
        # time.sleep(5)
        for check in check_box[:3]:
            check.click()
        time.sleep(3)

        load = wait.until(EC.visibility_of_element_located(self.load))
        load.click()
        time.sleep(2)

        transfer = wait.until(EC.visibility_of_element_located(self.transfer))
        transfer.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()
        time.sleep(2)

    def approve(self):
        wait = WebDriverWait(self.driver, 10)

        approve_btn = wait.until(EC.visibility_of_element_located(self.approve_btn))
        approve_btn.click()

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()
        time.sleep(2)






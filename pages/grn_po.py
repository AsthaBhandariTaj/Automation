from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Grn:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/grn/create/grn"
        self.pending_url = "https://uattuth.dolphin.com.np/ims/inventory/grn/pending?grnstatus=0&from_route=1"
        self.approved_url ="https://uattuth.dolphin.com.np/ims/inventory/grn/index/grn"
        self.po = (By.XPATH,"//i[@class='fa fa-list']")
        self.check_box = (By.CLASS_NAME,"checkboxClick")
        self.bill_number = (By.XPATH,"//input[@id='supplier_bill_no']")
        self.bill_date = (By.XPATH,"//input[@id='date_picker_s']")
        self.purchase_date = (By.XPATH,"//input[@id='date_picker_p']")
        self.save = (By.XPATH,"//button[@id='saveStock']")
        self.ok = (By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']")
        self.pre_approve_element = (By.XPATH,"//button[@title='Pre Approve']")
        self.approve_element = (By.XPATH,"//button[@title='Approve']")
        self.load = (By.XPATH,"//button[normalize-space()='Load']")

    def open(self):
        self.driver.get(self.url)
    
    def pending_open(self):
        self.driver.get(self.pending_url)

    def open_approve(self):
        self.driver.get(self.approved_url)

    def grn(self, quantity):
        wait = WebDriverWait(self.driver, 10)

        po = wait.until(EC.visibility_of_element_located(self.po))
        po.click()

        checkbox = wait.until(EC.visibility_of_all_elements_located(self.check_box))
        for check in checkbox[:3]:
            check.click()

        load = wait.until(EC.visibility_of_element_located(self.load))
        load.click()
        time.sleep(2)

        bill_number = str(int(time.time()))
        supplier_bill_no = wait.until(EC.visibility_of_element_located(self.bill_number))
        supplier_bill_no.send_keys(bill_number)
        supplier_bill_no.send_keys(Keys.ENTER)
        time.sleep(2)

        supplier_bill_date = wait.until(EC.visibility_of_element_located(self.bill_date))
        supplier_bill_date.send_keys("2025-12-25")
        supplier_bill_date.send_keys(Keys.ENTER)

        purchase_date = wait.until(EC.visibility_of_element_located(self.purchase_date))
        purchase_date.send_keys("2025-12-25")
        purchase_date.send_keys(Keys.ENTER)
        time.sleep(2)

        
        save = wait.until(EC.visibility_of_element_located(self.save))
        print("found")
        save.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        print("found1")
        ok.click()
        time.sleep(2)

    def pre_approve(self):
        wait = WebDriverWait(self.driver, 10)

        pre_approve = wait.until(EC.visibility_of_element_located(self.pre_approve_element))
        pre_approve.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        print("found preapprove")
        ok.click()
        time.sleep(2)

        approve = wait.until(EC.visibility_of_element_located(self.approve_element))
        approve.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        print("found approve")
        ok.click()
        time.sleep(2)

    
    def get_items_and_quantities(self):
        wait = WebDriverWait(self.driver, 5)
        table_body = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody")))

        rows = table_body.find_elements(By.TAG_NAME, "tr")
        items = []
        for row in rows[:3]:
            print("found 3s")
            item_name = row.find_element(By.XPATH, "./td[5]").text.strip()
            # quantity = quantity
            items.append((item_name))
        print(items)
        return items

        





            



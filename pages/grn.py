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
        self.supplier = (By.XPATH,"//div[@class='input-group']//div[@class='multiselect']//div[@class='multiselect__select']")
        self.enter_supplier = (By.XPATH,"//input[@placeholder='Select Supplier']")
        self.item = (By.XPATH,"//span[contains(text(),'Select Item')]")
        self.enter_items = (By.XPATH,"//input[@placeholder='Select Item']")
        self.quantity = (By.XPATH,"//input[@id='selected_item_qty']")
        self.cp = (By.XPATH,"//input[@id='selected_item_cp_before_tax']")
        self.add_element = (By.XPATH,"//button[@id='add_item']")
        self.bill_number = (By.XPATH,"//input[@id='supplier_bill_no']")
        self.bill_date = (By.XPATH,"//input[@id='date_picker_s']")
        self.purchase_date = (By.XPATH,"//input[@id='date_picker_p']")
        self.save = (By.XPATH,"//button[@id='saveStock']")
        self.ok = (By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']")
        self.pre_approve_element = (By.XPATH,"//button[@title='Pre Approve']")
        self.approve_element = (By.XPATH,"//button[@title='Approve']")

    def open(self):
        self.driver.get(self.url)
    
    def pending_open(self):
        self.driver.get(self.pending_url)

    def open_approve(self):
        self.driver.get(self.approved_url)

    def grn(self, quantity):
        wait = WebDriverWait(self.driver, 10)

        supplier = wait.until(EC.visibility_of_element_located(self.supplier))
        supplier.click()

        enter_supplier = wait.until(EC.visibility_of_element_located(self.enter_supplier))
        enter_supplier.send_keys("as")
        enter_supplier.send_keys(Keys.ENTER)
        time.sleep(2)

        item = wait.until(EC.visibility_of_element_located(self.item))
        item.click()
        print("clicked")

        enter_item = wait.until(EC.visibility_of_element_located(self.enter_items))
        enter_item.send_keys("liquid soap")
        time.sleep(5)
        print("entered")
        enter_item.send_keys(Keys.ENTER)
        time.sleep(5)

        item_quantity = wait.until(EC.visibility_of_element_located(self.quantity))
        item_quantity.clear()
        item_quantity.send_keys(Keys.BACKSPACE)
        item_quantity.send_keys(quantity)
        item_quantity.send_keys(Keys.ENTER)
        time.sleep(2)

        item_cp = wait.until(EC.visibility_of_element_located(self.cp))
        item_cp.clear()
        item_cp.send_keys("1000")
        item_cp.send_keys(Keys.ENTER)
        time.sleep(2)

        add_button = wait.until(EC.visibility_of_element_located(self.add_element))
        add_button.click()
        time.sleep(2)

        supplier_bill_no = wait.until(EC.visibility_of_element_located(self.bill_number))
        supplier_bill_no.send_keys("1234bcd")
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





        



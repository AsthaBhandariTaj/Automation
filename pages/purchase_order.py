from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PurchaseOrder:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/spurchase_order/create/purchaseOrd"
        self.pending_url = "https://uattuth.dolphin.com.np/ims/inventory/purchase_reorder/pendinglist?poStatus=1&from_route=1"
        self.approved_url = "https://uattuth.dolphin.com.np/ims/inventory/spurchase_order/index/purchase"
        self.supplier = (By.XPATH,"//div[@class='col-md-3 col-sm-3']//div[@class='input-group']")
        self.enter_supplier = (By.XPATH,"//input[@placeholder='Select Supplier']")
        self.item_element = (By.XPATH,"//div[@class='col-md-3 col-sm-4 xs-m-b-15']//div[@class='input-group custom-multiselect']")
        self.enter_item = (By.XPATH,"//input[@placeholder='Select Catelogue']")
        self.quantity = (By.XPATH,"//input[@id='selected_item_qty']")
        self.rate = (By.XPATH,"//input[@id='selected_item_rate']")
        self.add = (By.XPATH,"//button[@id='add_item']")
        self.save = (By.XPATH,"//div[contains(text(),'Save')]")
        self.ok = (By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']")
        self.verify_element = (By.XPATH,"//tbody/tr[1]/td[9]/button[4]")
        self.pre_approve_element = (By.XPATH,"//button[@title='PreApprove Purchase Order']")
        self.approve_element = (By.XPATH,"//button[@title='Approve Purchase Order']")

    def open(self):
        self.driver.get(self.url)

    def open_pending(self):
        self.driver.get(self.pending_url)
    
    def open_approved(self):
        self.driver.get(self.approved_url)

    def purchase_order(self):
        wait = WebDriverWait(self.driver, 10)

        supplier_element = wait.until(EC.visibility_of_element_located(self.supplier))
        supplier_element.click()
        time.sleep(2)

        enter_supplier_element = wait.until(EC.visibility_of_element_located(self.enter_supplier))
        enter_supplier_element.send_keys(Keys.ENTER)
        time.sleep(2)

        item = wait.until(EC.visibility_of_element_located(self.item_element))
        item.click()
        time.sleep(2)

        enter_element = wait.until(EC.visibility_of_element_located(self.enter_item))
        enter_element.send_keys("liquid soap")
        time.sleep(2)
        enter_element.send_keys(Keys.ENTER)

        quantity = wait.until(EC.visibility_of_element_located(self.quantity))
        quantity.clear()
        quantity.send_keys("5")
        quantity.send_keys(Keys.ENTER)

        rate = wait.until(EC.visibility_of_element_located(self.rate))
        rate.send_keys("1000")
        rate.send_keys(Keys.ENTER)
        time.sleep(2)

        add = wait.until(EC.visibility_of_element_located(self.add))
        add.click()
    
        save = wait.until(EC.visibility_of_element_located(self.save))
        save.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()
        time.sleep(2)

    def verify(self):
        wait = WebDriverWait(self.driver, 10)

        verify = wait.until(EC.visibility_of_element_located(self.verify_element))
        verify.click()

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()

    def pre_approve(self):
        wait = WebDriverWait(self.driver, 10)

        pre_approve = wait.until(EC.visibility_of_element_located(self.pre_approve_element))
        pre_approve.click()

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()
        time.sleep(2)
    
    def approve(self):
        wait = WebDriverWait(self.driver, 10)

        approve = wait.until(EC.visibility_of_element_located(self.approve_element))
        approve.click()

        ok = wait.until(EC.visibility_of_element_located(self.ok))
        ok.click()
        time.sleep(2)













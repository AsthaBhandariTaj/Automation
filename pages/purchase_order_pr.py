from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PurchaseOrderPr:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/spurchase_order/create/purchaseOrd"
        self.pending_url = "https://uattuth.dolphin.com.np/ims/inventory/purchase_reorder/pendinglist?poStatus=1&from_route=1"
        self.approved_url = "https://uattuth.dolphin.com.np/ims/inventory/spurchase_order/index/purchase"
        self.supplier = (By.XPATH,"//div[@class='col-md-3 col-sm-3']//div[@class='input-group']")
        self.enter_supplier = (By.XPATH,"//input[@placeholder='Select Supplier']")
        self.pr_element = (By.XPATH,"//button[@id='requisitionListBtn']")
        self.check_box = (By.CLASS_NAME,"checkboxClick")
        self.load_pr = (By.XPATH,"//button[@class='btn btn-primary btn-sm p-l-20 p-r-20 p-t-8 p-b-8']")
        self.discount = (By.XPATH,"//input[@id='catalogue_discount']")
        self.tax = (By.XPATH,"//input[@id='catalogue_tax']")
        self.save = (By.XPATH,"//button[@id='save_purchase_order']")
        self.ok = (By.XPATH,"//button[normalize-space()='OK']")
        self.verify_element = (By.XPATH,"//tbody/tr[1]/td[9]/button[4]")
        self.pre_approve_element = (By.XPATH,"//button[@title='PreApprove Purchase Order']")
        self.approve_element = (By.XPATH,"//button[@title='Approve Purchase Order']")


    def open(self):
        self.driver.get(self.url)

    
    def open_pending(self):
        self.driver.get(self.pending_url)
    
    def open_approved(self):
        self.driver.get(self.approved_url)


    def purchase_order_pr(self):
        wait = WebDriverWait(self.driver, 10)

        supplier_element = wait.until(EC.visibility_of_element_located(self.supplier))
        supplier_element.click()
        time.sleep(2)

        enter_supplier_element = wait.until(EC.visibility_of_element_located(self.enter_supplier))
        enter_supplier_element.send_keys(Keys.ENTER)
        time.sleep(2)

        purchase_request = wait.until(EC.visibility_of_element_located(self.pr_element))
        purchase_request.click()
        time.sleep(2)

        check_box = wait.until(EC.visibility_of_element_located(self.check_box))
        check_box.click()
        time.sleep(2)

        load_pr = wait.until(EC.visibility_of_element_located(self.load_pr))
        load_pr.click()
        time.sleep(2)

        discount_element = wait.until(EC.visibility_of_element_located(self.discount))
        discount_element.send_keys("2")
        discount_element.send_keys(Keys.ENTER)

        tax_element = wait.until(EC.visibility_of_element_located(self.tax))
        tax_element.send_keys("13")
        discount_element.send_keys(Keys.ENTER)
        time.sleep(2)

        save = wait.until(EC.visibility_of_element_located(self.save))
        save.click()

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




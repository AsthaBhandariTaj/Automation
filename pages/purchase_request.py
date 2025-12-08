from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PurchaseRequest:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/purchase_request/create/0/purchase_request"
        self.pending_url = "https://uattuth.dolphin.com.np/ims/inventory/purchase_request/pending/purchase_request"
        self.item_element = (By.XPATH,("//body/div[@id='app']/div[@class='page-container']/div[@class='page-content-wrapper']/div[@class='page-content']/div/div[@class='portlet light bordered']/div[@class='portlet-body']/div[@class='row']/div[@class='col-md-3 col-sm-4 xs-m-b-15']/div[@class='input-group custom-multiselect']/div[@class='multiselect']/div[@class='multiselect__tags']/span[1]"))
        self.enter_item = (By.XPATH,("//div[@class='multiselect multiselect--active']//input[@placeholder='Select Catalogue']"))
        self.quantity = (By.ID,("selected_item_qty"))
        self.add_button = (By.ID,("add_item"))
        self.save_button = (By.XPATH,"//div[contains(text(),'Save')]")
        self.ok_button = (By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']")
        self.approve_elemnt = (By.XPATH,"//tbody/tr[1]/td[7]/button[2]")
    def open(self):
        self.driver.get(self.url)
        self.driver.refresh()
    
    def open_pending(self):
        self.driver.get(self.pending_url)
    
    
    def purchase_request(self,item_name,quantity, first = True):
        wait = WebDriverWait(self.driver, 10)
        

        if first:
            item_field = wait.until(EC.visibility_of_element_located(self.item_element))
            item_field.click()
            time.sleep(2)

        item_keys = wait.until(EC.visibility_of_element_located(self.enter_item))
        item_keys.send_keys(item_name)
        time.sleep(2)

        item_keys.send_keys(Keys.DOWN)
        item_keys.send_keys(Keys.ENTER)
        time.sleep(2)

        item_quantity = wait.until(EC.visibility_of_element_located(self.quantity))
        item_quantity.clear()
        item_quantity.send_keys(quantity)
        item_quantity.send_keys(Keys.ENTER)
        time.sleep(2)

        add_item = wait.until(EC.visibility_of_element_located(self.add_button))
        add_item.click()

        if not first:
            save = wait.until(EC.visibility_of_element_located(self.save_button))
            save.click()
            time.sleep(2)

            ok = wait.until(EC.visibility_of_element_located(self.ok_button))
            ok.click()

        time.sleep(5)

    def approve(self):
        wait = WebDriverWait(self.driver, 10)
        
        approve_button = wait.until(EC.visibility_of_element_located(self.approve_elemnt))
        approve_button.click()
        time.sleep(2)

        ok = wait.until(EC.visibility_of_element_located(self.ok_button))
        ok.click()
        time.sleep(2)







    

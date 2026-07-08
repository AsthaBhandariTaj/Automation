from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ReceiveRequisition:
    def __init__(self , driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/stocktransfer/pending/receiveFromSubstore"
        self.view_element = (By.XPATH,"//tbody/tr[1]/td[6]/button[1]")
        self.close_view_element = (By.XPATH,"//div[@id='issue_print']//button[@aria-label='Close']")
        self.receive_element = (By.XPATH,"//tbody/tr[1]/td[6]/button[2]")
        self.ok_element = (By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']")
    
    def open(self):
        self.driver.get(self.url)

    def requisition_receive(self):
        wait = WebDriverWait(self.driver , 10)
        time.sleep(5)

        
        view_button = wait.until(EC.visibility_of_element_located(self.view_element))
        view_button.click()
        time.sleep(5)
    
        close_button = wait.until(EC.visibility_of_element_located(self.close_view_element))
        close_button.click()
          
        receive_button = wait.until(EC.visibility_of_element_located(self.receive_element))
        receive_button.click()

        ok_button = wait.until(EC.visibility_of_element_located(self.ok_element))
        ok_button.click()




    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class StockInHand:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uattuth.dolphin.com.np/ims/inventory/stockinhand"
        # self.search_button = (By.XPATH,"//button[@id='search']")
        # self.item_search = (By.XPATH,"//div[@tabulator-field='catalogue_name']//input[contains(@placeholder,'')]")
        ## self.quantity = (By.XPATH,"//div[@class='tabulator-row tabulator-selectable tabulator-row-odd']//div[@role='gridcell'][normalize-space()='462']")
        self.quick_view = (By.XPATH,"//span[normalize-space()='Quick Access']")
        self.quick_stock_view = (By.XPATH,"//li[@class='dropdown dropdown-user open']//li[1]//a[1]//a[1]")
        self.catalogue_search = (By.XPATH,"//span[@class='multiselect__single']")
        self.catalogue_enter = (By.XPATH,"//input[@id='catalogue']")
        self.quantity = (By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)")
    def open(self):
        self.driver.get(self.url)

    def stock_in_hand(self , items):
        wait = WebDriverWait(self.driver, 10)

        # search_button = wait.until(EC.visibility_of_element_located(self.search_button))
        # search_button.click()

        # item_search = wait.until(EC.visibility_of_element_located(self.item_search))
        # item_search.send_keys(items)
        # item_search.send_keys(Keys.ENTER)
        # time.sleep(2)

        ## quantity = wait.until(EC.visibility_of_element_located(self.quantity))
        ## time.sleep(5)
        ## print("found quantity", quantity)
        ## quantit.click()

        quick_view = wait.until(EC.visibility_of_element_located(self.quick_view))
        quick_view.click()
        time.sleep(1)

        quick_stock_view = wait.until(EC.visibility_of_element_located(self.quick_stock_view))
        quick_stock_view.click()
        time.sleep(1)

        search_catalogue = wait.until(EC.visibility_of_element_located(self.catalogue_search))
        search_catalogue.click()
        time.sleep(1)

        enter_catalogue = wait.until(EC.visibility_of_element_located(self.catalogue_enter))
        enter_catalogue.send_keys("liquid soap")
        enter_catalogue.send_keys(Keys.ENTER)
        time.sleep(1)

        quantity_element = wait.until(
            EC.visibility_of_element_located(
                (self.quantity))
            )
        
        # quantity_element = wait.until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//td[normalize-space()='General Main Store']/following-sibling::td[1]")
        #     )
        # )
        quantity_text = quantity_element.text.strip()
        print(f"Stock Quantity for 'General Main Store': {quantity_text}")
        return quantity_text

        



    
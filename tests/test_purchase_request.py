import pytest
from pages.purchase_request import PurchaseRequest
import time

class TestPurchaseRequest:
    def test_valid_purchase_request(self, logged_in_driver):
        purchase_request_page = PurchaseRequest(logged_in_driver)
        purchase_request_page.open()
        # purchase_request_page.open()
        purchase_request_page.purchase_request("a","5")
        time.sleep(5)
        purchase_request_page.purchase_request("de","3", first=False)
        purchase_request_page.open_pending()
        purchase_request_page.approve()
        time.sleep(5)
        purchase_request_page.open()
        time.sleep(5)




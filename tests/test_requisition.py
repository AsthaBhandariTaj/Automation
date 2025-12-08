import pytest 
from pages.requisition import Requisition
import time

class TestRequisition:
    def test_valid_test_requisition(self, logged_in_driver):
        requisition_page = Requisition(logged_in_driver)
        requisition_page.open()
        requisition_page.open()
        requisition_page.requisition("ap", "5")
        time.sleep(2)
        requisition_page.requisition("ds","3", first=False)
        time.sleep(2)
        requisition_page.open_pending()
        requisition_page.pre_approve()
        requisition_page.approve()
        time.sleep(5)
        requisition_page.open()
        time.sleep(5)
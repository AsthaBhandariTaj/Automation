from pages.purchase_order import PurchaseOrder
import time

class TestPurchaseOrder:
    def test_purchase_order(self, logged_in_driver):
        purchase_order_page = PurchaseOrder(logged_in_driver)
        purchase_order_page.open()
        purchase_order_page.purchase_order()
        purchase_order_page.open_pending()
        time.sleep(3)
        print("found verify")
        purchase_order_page.verify()
        print("verified")
        time.sleep(2)
        purchase_order_page.pre_approve()
        print("pre-approved")
        time.sleep(2)
        purchase_order_page.approve()
        print("approved")
        purchase_order_page.open_approved()
        time.sleep(5)

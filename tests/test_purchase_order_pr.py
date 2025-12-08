from pages.purchase_order_pr import PurchaseOrderPr
import time

class TestPurchaseOrderPr:
    def test_purchase_order_pr(self, logged_in_driver):
        purchase_order_pr_page = PurchaseOrderPr(logged_in_driver)
        purchase_order_pr_page.open()
        purchase_order_pr_page.purchase_order_pr()
        purchase_order_pr_page.open_pending()
        time.sleep(3)
        print("found verify")
        purchase_order_pr_page.verify()
        print("verified")
        time.sleep(2)
        purchase_order_pr_page.pre_approve()
        print("pre-approved")
        time.sleep(2)
        purchase_order_pr_page.approve()
        print("approved")
        purchase_order_pr_page.open_approved()
        time.sleep(5)

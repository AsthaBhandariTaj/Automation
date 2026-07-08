from pages.grn_po import Grn
from pages.stock_in_hand import StockInHand
import time

class TestGrn:
    def test_valid_grn(self, logged_in_driver):
      
        grn_page = Grn(logged_in_driver)
        grn_page.open()
        grn_page.open()

        # stock_in_hand = StockInHand(logged_in_driver)
        # stock_in_hand.open()
        # stock_in_hand.open()
        # time.sleep(5)
        # before_stock = stock_in_hand.stock_in_hand(item, quantity)
        # time.sleep(5)

        grn_page.grn(quantity=1)
        time.sleep(2)
        grn_page.get_items_and_quantities()
        # grn_page.pending_open()
        # grn_page.pre_approve()
        # grn_page.open_approve()
        # stock_in_hand.open()
        # stock_in_hand.open()
        # time.sleep(5)
        # after_stock = stock_in_hand.stock_in_hand(item, quantity)

        # expected = int(before_stock) + int(quantity)
        # print(expected)
        # assert expected == int(after_stock), ("Stock mismatch")

        
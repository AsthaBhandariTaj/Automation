from pages.stock_in_hand import StockInHand
import time

class TestStockInHand:
    def test_stock_in_hand(self, logged_in_driver):
        stock_in_hand_page = StockInHand(logged_in_driver)
        stock_in_hand_page.open()
        stock_in_hand_page.open()
        stock = stock_in_hand_page.stock_in_hand(items="liquid soap")
        print("stock is ", stock)
        time.slee(3)
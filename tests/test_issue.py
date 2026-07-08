from pages.issue import Issue
from pages.stock_in_hand import StockInHand
import time

class TestIssue:
    def test_issue(self, logged_in_driver):
        stock_in_hand_page = StockInHand(logged_in_driver)
        stock_in_hand_page.open()
        stock_in_hand_page.open()
        stock_in_hand_page.stock_in_hand(items="liquid")
        issue_page = Issue(logged_in_driver)
        issue_page.open()
        issue_page.open()
        issue_page.issue()
        issue_page.open_list()
        issue_page.approve()
        stock_in_hand_page = StockInHand(logged_in_driver)
        stock_in_hand_page.open()
        stock_in_hand_page.stock_in_hand(items="liquid")
        time.sleep(5)
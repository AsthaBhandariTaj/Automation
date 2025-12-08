from pages.requisition_receive import ReceiveRequisition
import time

class TestReceiveRequisition:
    def test_receive_requisition(self, logged_in_driver):
        receive_requisition_page = ReceiveRequisition(logged_in_driver)
        time.sleep(2)
        receive_requisition_page.open()
        time.sleep(3)
        receive_requisition_page.requisition_receive()
        
        
        

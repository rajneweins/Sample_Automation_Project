import re
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Config.config import TestData as TD, TestData
from Pages.PurchaseItemsPage import PurchaseItems
from Tests.test_base import BaseTest


class Test_Add_to_Cart(BaseTest):
    """positive test case"""

    def test_page_title(self):
        try:
            self.add_to_cart = PurchaseItems(self.driver)
            flag = self.add_to_cart.get_title(TD.LOGIN_PAGE_TITLE)
            assert flag
        except NoSuchElementException:
            time.sleep(2)

    @pytest.mark.parametrize(
        "item_name",
        [
            'Faded Short Sleeve T-shirts',
            'Blouse',
            'Printed Chiffon Dress'
        ]
    )
    def test_add_item_to_cart(self, item_name):
        self.add_to_cart = PurchaseItems(self.driver)
        self.add_to_cart.add_item_to_cart(item_name)

    def test_preoceed_to_checkout(self, item):
        self.add_to_cart = PurchaseItems(self.driver)
        self.add_to_cart.add_item_to_cart(TestData.ITEM)


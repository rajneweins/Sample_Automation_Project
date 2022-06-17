from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class PurchaseItems(BasePage):

    """By Locators"""
    SECTION_WOMEN = (By.XPATH, "//a[@title='Women']")

    """CATEGORIES"""
    PARENT_CATEGORIES = (By.XPATH, "//*[@id = 'ul_layered_category_0']/li")
    TOPS = (By.XPATH, "//input[@id='layered_category_4']")
    DRESSES = (By.XPATH, "//input[@id='layered_category_8']")

    """SIZES"""
    SMALL =  (By.XPATH, "//input[@id='layered_id_attribute_group_1']")
    MEDIUM = (By.XPATH, "//input[@id='layered_id_attribute_group_2']")
    LARGE = (By.XPATH,  "//input[@id='layered_id_attribute_group_3']")


    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")

    CONTINUE_SHOPPING = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[2]/div[4]/span")
    PROCEED_TO_CHECKOUT = (By.LINK_TEXT, "Proceed to checkout")


    """constructor of login page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def verify_categories(self, value):
        if value == 'TOPS':
            self.select_checkbox(self.TOPS)
        elif value == 'DRESSES':
            self.select_checkbox(self.DRESSES)
        else:
            return 0

    def add_item_to_cart(self, item):
        self.hover_and_click((By.LINK_TEXT, item), self.ADD_TO_CART)
        self.click_button(self.CONTINUE_SHOPPING)

    def proceed_checkout(self):
        self.click_button(self.CONTINUE_SHOPPING)

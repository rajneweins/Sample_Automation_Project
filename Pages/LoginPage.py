from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """By Locators"""
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SIGNIN_BUTTON = (By.ID, 'SubmitLogin')
    AUTHENTICATION_MESSAGE = (By.XPATH, "//*[@id='center_column']/div[1]/p")

    """constructor of login page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """method to check page title"""
    # def is_title_page(self, title):
    #     return self.is_title(title)

    """methods to check if user & password input are visible"""
    def is_username_input_box_visible(self):
        return self.is_visible(self.EMAIL)

    def is_password_input_box_visible(self):
        return self.is_visible(self.PASSWORD)

    """method to check if signin link is visible"""
    def is_signin_button_visible(self):
        return self.is_visible(self.SIGNIN_BUTTON)

    """method to login"""
    def do_sign_in(self,user_name, password):
        self.do_send_keys(self.EMAIL, user_name)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)

    def is_error_message_is_visible(self):
        return self.is_visible(self.AUTHENTICATION_MESSAGE)

    def get_authentication_error_message_text(self):
        return self.get_text(self.AUTHENTICATION_MESSAGE)


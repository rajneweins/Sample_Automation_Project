import re
import time

from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class UserRegistration(BasePage):
    """By Locators"""

    """1st Page of registration"""
    EMAIL_ID_CREATE = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    ERROR_MESSAGE = (By.XPATH, "//*[@id = 'create_account_error']//li")

    """2nd page of registration"""
    """Personal Information"""
    GENDER_M = (By.XPATH, "//input[@id='id_gender1']")
    GENDER_F = (By.ID, 'id_gender2')

    C_FIRST_NAME = (By.ID, "customer_firstname")
    C_LAST_NAME = (By.ID, "customer_lastname")
    PASSWORD = (By.ID, "passwd")

    """Date of Birth"""
    DAY = (By.XPATH, "//*[@id='days']/option")
    MONTH = (By.XPATH, "//*[@id='months']/option")
    YEAR = (By.XPATH, "//*[@id='years']/option")
    CHECK_BOX_NEWS_LETTER = (By.ID, "newsletter")

    """Address Information"""
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    ADDRESS = (By.ID, "address1")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    ZIP_CODE = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    MOBILE = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    REGISTER_BUTTON = (By.ID, "submitAccount")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """method to get page title"""
    def get_page_title(self, title):
        return self.get_title(title)

    def is_username_input_box_visible(self):
        return self.is_visible(self.EMAIL_ID_CREATE)

    """methods to give input"""
    """first page of registration"""
    def verify_email_new_user(self, new_email):
        self.do_send_keys(self.EMAIL_ID_CREATE, new_email)
        self.do_click(self.CREATE_ACCOUNT_BUTTON)

    def authenticate_user_existence(self):
        return self.get_text(self.ERROR_MESSAGE)

    """2nd page of registration"""
    def select_gender(self, gender):
        time.sleep(5)
        if gender == 'Mr.':
            self.select_radiobutton(self.GENDER_M)
        elif gender == 'Mrs.':
            self.select_radiobutton(self.GENDER_F)

    def fill_first_name(self, first_name):
        self.do_send_keys(self.C_FIRST_NAME, first_name)
        # print(a)

    def fill_last_name(self, last_name):
        self.do_send_keys(self.C_LAST_NAME, last_name)

    def fill_password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    def select_date_of_birth(self, day, month, year):
        self.select_values_from_dropdown(self.DAY, day)
        self.select_from_dropdown_by_value(self.MONTH, month)
        self.select_from_dropdown_by_value(self.YEAR, year)

    def tick_news_letter_box(self):
        self.select_checkbox(self.CHECK_BOX_NEWS_LETTER)

    def fill_address(self, address):
        self.do_send_keys(self.ADDRESS, address)

    def fill_city(self, city):
        self.do_send_keys(self.CITY, city)

    def select_state(self, state):
        self.select_from_dropdown_by_visible_text(self.STATE, state)

    def fill_zipcode(self, zipcode):
        self.do_send_keys(self.ZIP_CODE, zipcode)

    def select_country(self):
        self.select_from_dropdown_by_visible_text(self.COUNTRY, 'United States')

    def fill_mobile_num(self, mob):
        self.do_send_keys(self.MOBILE, mob)

    def click_register_button(self):
        self.do_click(self.REGISTER_BUTTON)

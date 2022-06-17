import re
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Config.config import TestData as TD
from Pages.UserRegistrationPage import UserRegistration
from Tests.test_base import BaseTest


class Test_User_Registration(BaseTest):
    """positive test case"""
    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'

    def test_page_title(self):
        try:
            self.user_registration = UserRegistration(self.driver)
            flag = self.user_registration.get_title(TD.LOGIN_PAGE_TITLE)
            assert flag
        except NoSuchElementException:
            time.sleep(2)

    def test_input_email_is_visible(self):
        self.user_registration = UserRegistration(self.driver)
        flag1 = self.user_registration.is_username_input_box_visible()
        assert flag1

    def test_valid_email_address_check(self):
        self.user_registration = UserRegistration(self.driver)
        try:
            self.user_registration.verify_email_new_user(TD.R_VALID_EMAIL)
            flag = self.user_registration.get_page_title(TD.TITLE)
            assert flag == TD.TITLE
        except TimeoutException:
            time.sleep(2)

    """negative test case"""

    @pytest.mark.parametrize(
        "email_address",
        [
            'abc@gmail.com',
            12345678,
            '!@#$%^&*',
            '',
            'ram@gmail.com',
            '    '
        ]
    )
    def test_Invalid_email_address_check(self, email_address):
        self.user_registration = UserRegistration(self.driver)
        try:
            self.user_registration.verify_email_new_user(email_address)
            if re.search(self.regex, str(email_address)):
                flag1 = self.user_registration.authenticate_user_existence()
                # self.user_registration.get_page_title(TestData.TITLE)
                assert flag1 == 'An account using this email address has already been registered. Please enter a valid password or request a new one.'
            else:
                flag2 = self.user_registration.authenticate_user_existence()
                assert flag2 == 'Invalid email address.'
        except TimeoutException:
            time.sleep(2)

    def test_gender(self):
        self.user_registration = UserRegistration(self.driver)
        self.test_valid_email_address_check()
        # time.sleep(5)
        # self.user_registration.select_gender(TD.GENDER)
        self.user_registration.select_date_of_birth(TD.DAY, TD.MONTH, TD.YEAR)

    def test_user_registration_form(self):
        try:
            self.user_registration = UserRegistration(self.driver)
            self.test_valid_email_address_check()
            self.user_registration.select_gender(TD.GENDER)
            self.user_registration.fill_first_name(TD.FIRST_NAME)
            self.user_registration.fill_last_name(TD.LAST_NAME)
            self.user_registration.fill_password(TD.R_PASSWORD)
            self.user_registration.select_date_of_birth(TD.DAY, TD.MONTH, TD.YEAR)
            self.user_registration.tick_news_letter_box()

            self.user_registration.fill_address(TD.ADDRESS)
            self.user_registration.fill_city(TD.CITY)
            self.user_registration.select_state(TD.STATE)
            self.user_registration.fill_zipcode(TD.ZIP_CODE)
            self.user_registration.select_country()
            self.user_registration.fill_mobile_num(TD.MOBILE_NO)
            self.user_registration.click_register_button()

        except TimeoutException:
            time.sleep(2)
        except NoSuchElementException:
            time.sleep(2)


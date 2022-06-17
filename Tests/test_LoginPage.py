import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    """positive test case"""
    def test_page_title(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert flag

    def test_user_details_input_box_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag1 = self.loginpage.is_username_input_box_visible()
        flag2 = self.loginpage.is_password_input_box_visible()
        assert flag1
        assert flag2

    """positive test case"""
    def test_login_button_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_signin_button_visible()
        assert flag

    """positive test case"""
    def test_login_correct_credentials(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_sign_in(TestData.USER_NAME, TestData.PASSWORD)

    """negative test case"""
    @pytest.mark.parametrize(
        "username, password",
        [
            ('abc@gmail.com', 'abc@123'),
            (123456789, 123456789),
            ('!@#$%^&*', '!@#%$^#@@#'),
            ('',''),
            ('ram@gmail.com',''),
            ('', 'absc')
        ]
    )
    def test_login_wrong_credentails(self, username, password):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_sign_in(username, password)
        flag2 = self.loginpage.get_authentication_error_message_text()
        assert flag2 == 'There is 1 error'

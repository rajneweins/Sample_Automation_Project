from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

"""This class is parent of all pages"""
"""This page contains all generic methods and utilities"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        wb = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        wb.send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located(by_locator)).text
        return element

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.title_is(title))
        return element

    def click_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def select_from_dropdown_by_value(self, by_locator, value):
        # wb = Select(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)))
        wb = self.driver.find_element(by_locator)
        # action_chains = ActionChains(self.driver)
        # action_chains.move_to_element(wb).perform()
        # Select(wb).select_by_value(value)
        for i in Select(wb).options:
            if i.text == value:
                i.click()

    def select_from_dropdown_by_visible_text(self, by_locator, value):
        # wb = Select(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)))
        wb = self.driver.find_elements(by_locator)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(wb).perform()
        Select(wb).select_by_visible_text(value)

    def select_values_from_dropdown(self, dropDownOptionList, value):
        options = self.driver.find_element(dropDownOptionList)
        for ele in dropDownOptionList:
            if ele.text == value:
                ele.click()
                break

    def select_checkbox(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def select_radiobutton(self, by_locator):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()
        self.driver.find_element(by_locator).click()

    def hover_and_click(self, by_locator_1, by_locator_2):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(by_locator_1).perform()
        action_chains.move_to_element(by_locator_2).click().perform()
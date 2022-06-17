import pytest
from selenium import webdriver

from Config.config import TestData


# service_obj1 = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH)
# service_obj2 = Service(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    # elif request.param == "firefox":
    #     web_driver = webdriver.Firefox(TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()

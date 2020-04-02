import time
from common.selenium_lib import element_attribute_contains_value
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.header_page import Header
#
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")



login_page = LoginPage(driver)

def get_num(driver, locator):
    for i in range(10):
        print(i)
        if i == 5:
            return True
    return False



login_page.wait_until(get_num('sds'))


driver.close()

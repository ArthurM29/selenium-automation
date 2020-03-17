from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dashboard import Dashboard


class LoginPage(BasePage):
    _name = 'Login Page'
    _url = 'https://opensource-demo.orangehrmlive.com/'

    # locators
    _username_input = (By.ID, 'txtUsername')
    _password_input = (By.ID, 'txtPassword')
    _login_button = (By.ID, 'btnLogin')
    _login_form = (By.ID, 'frmLogin')

    _page_identifier = _login_form

    def enter_username(self, username):
        self._driver.find_element(*self._username_input).send_keys(username)

    def enter_password(self, password):
        self._driver.find_element(*self._password_input).send_keys(password)

    def click_login_button(self):
        self._driver.find_element(*self._login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return Dashboard(self._driver)

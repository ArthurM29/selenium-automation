from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dashboard import DashboardComponent


class LoginPage(BasePage):
    _name = 'Login Page'
    _url = 'https://opensource-demo.orangehrmlive.com/'

    # locators
    _username_input = (By.ID, 'txtUsername')
    _password_input = (By.ID, 'txtPassword')
    _login_button = (By.ID, 'btnLogin')
    _login_form = (By.ID, 'frmLogin')
    _invalid_login_error_message = (By.ID, 'spanMessage')

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
        return DashboardComponent(self._driver)

    def invalid_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self

    def get_invalid_login_error(self):
        """Return error message that is displayed when one of the credentials is empty or invalid"""
        return self._driver.find_element(*self._invalid_login_error_message).text

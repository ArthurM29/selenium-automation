from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    url = 'https://opensource-demo.orangehrmlive.com/'

    # region locators
    _username_input = (By.ID, 'txtUsername')
    _password_input = (By.ID, 'txtPassword')
    _login_button = (By.ID, 'btnLogin')
    _login_form = (By.ID, 'frmLogin')
    _invalid_login_error_message = (By.ID, 'spanMessage')

    _page_identifier_element = _login_form

    # endregion

    # region private methods
    def _enter_username(self, username):
        self.enter_text(self._username_input, username)

    def _enter_password(self, password):
        self.enter_text(self._password_input, password)

    def _click_login_button(self):
        self.click_element_with_JS(self._login_button)

    # endregion

    # region public interface
    def login(self, username, password):
        self._enter_username(username)
        self._enter_password(password)
        self._click_login_button()
        return DashboardPage(self.driver)

    def invalid_login(self, username, password):
        self._enter_username(username)
        self._enter_password(password)
        self._click_login_button()
        return self

    def get_invalid_login_error(self):
        """Return error message that is displayed when one of the credentials is empty or invalid"""
        return self.get_text(self._invalid_login_error_message)
    # endregion

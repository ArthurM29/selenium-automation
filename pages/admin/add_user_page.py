from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddUserPage(BasePage):
    # region locators

    _add_user_form_container_div = (By.CSS_SELECTOR, 'div#systemUser')
    _user_role_dropdown = (By.ID, 'systemUser_userType')
    _employee_name_input = (By.ID, 'systemUser_employeeName_empName')
    _username_input = (By.ID, 'systemUser_userName')
    _status_dropdown = (By.ID, 'systemUser_status')
    _password_input = (By.ID, 'systemUser_password')
    _confirm_password_input = (By.ID, 'systemUser_confirmPassword')
    _save_button = (By.ID, 'btnSave')

    _page_identifier_element = _add_user_form_container_div

    # endregion

    # region private methods
    def _select_user_role(self, option_name):
        self.select_dropdown_option(self._user_role_dropdown, option_name)

    def _enter_employee_name(self, name):
        self.enter_text(self._employee_name_input, name)

    def _enter_username(self, username):
        self.enter_text(self._username_input, username, wait=5)

    def _select_status(self, option_name):
        self.select_dropdown_option(self._status_dropdown, option_name)

    def _enter_password(self, password):
        self.enter_text(self._password_input, password)

    def _enter_confirm_password(self, password):
        self.enter_text(self._confirm_password_input, password)

    def _click_save_button(self):
        self.click_element(self._save_button)
        from pages.admin.user_management_page import UserManagementPage
        return UserManagementPage(self.driver)

    # endregion

    # region public interface
    def add_user(self, user):
        self._select_user_role(user.user_role)
        self._enter_employee_name(user.employee_name)
        self._enter_username(user.username)
        self._select_status(user.status)
        self._enter_password(user.password)
        self._enter_confirm_password(user.confirm_password)


    # endregion

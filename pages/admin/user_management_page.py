from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserManagementPage(BasePage):
    # region locators

    _users_table = (By.ID, 'resultTable')
    _add_button = (By.ID, 'btnAdd')

    _page_identifier_element = _users_table

    # endregion

    # region private methods
    def click_add_button(self):
        self.click_element(self._add_button)
        from pages.admin.add_user_page import AddUserPage
        return AddUserPage(self.driver)

    # endregion

    # region public interface

    # endregion

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):
    # region locators
    _modal_container_div = (By.ID, 'displayAbout')
    _title = (By.CSS_SELECTOR, '#displayAbout h3')
    _close_icon = (By.CSS_SELECTOR, '#displayAbout .close')
    _company_name_p = (By.CSS_SELECTOR, '#frmSelectEmployees p:nth-of-type(1)')
    _version_p = (By.CSS_SELECTOR, '#frmSelectEmployees p:nth-of-type(2)')
    _active_employees_p = (By.CSS_SELECTOR, '#frmSelectEmployees p:nth-of-type(3)')
    _employees_terminated_p = (By.CSS_SELECTOR, '#frmSelectEmployees p:nth-of-type(4)')

    _page_identifier = _modal_container_div

    # endregion

    # region public interface
    def get_title(self):
        return self.get_text(self._title)

    def close(self):
        self.click_element(self._close_icon)

    # endregion

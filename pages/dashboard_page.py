from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardComponent(BasePage):
    # region locators
    _header_title_div = (By.CSS_SELECTOR, 'div.head')

    _page_identifier = _header_title_div

    # endregion

    # region public interface
    def get_title(self):
        return self.driver.find_element(*self._header_title_div).text

    # endregion

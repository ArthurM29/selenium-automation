from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # region locators
    _header_title_div = (By.CSS_SELECTOR, 'div.head')

    _page_identifier = _header_title_div

    # endregion

    # region public interface
    def get_title(self):
        return self.get_text(self._header_title_div)

    # endregion

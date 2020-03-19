from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardComponent(BasePage):
    _name = 'Dashboard'
    _header_title_div = (By.CSS_SELECTOR, 'div.head')
    _page_identifier = _header_title_div

    def get_title(self):
        return self._driver.find_element(*self._header_title_div).text

from selenium.webdriver.common.by import By
from common import selenium_lib
from pages.about_page import AboutPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.orange_hrm_prod_page import OrangeHRMPRODPage


class Header(BasePage):
    # region locators
    _logo_image = (By.CSS_SELECTOR, '#branding img')
    _welcome_link = (By.ID, 'welcome')
    _welcome_menu = (By.ID, 'welcome-menu')
    _welcome_menu_about_link = (By.ID, 'aboutDisplayLink')
    _welcome_menu_logout_link = (By.LINK_TEXT, 'Logout')
    _page_identifier = _logo_image

    # endregion

    # region private methods
    def _click_on_about_link(self):
        self.click_element_with_JS(self._welcome_menu_about_link, self._element_wait_timeout)

    def _click_on_logout_link(self):
        self.click_element_with_JS(self._welcome_menu_logout_link, wait=self._element_wait_timeout)

    # endregion

    # region public interface
    def is_logo_displayed(self):
        return self._is_element_displayed(self._logo_image)

    def get_welcome_text(self):
        return self.get_text(self._welcome_link)

    def open_welcome_menu(self):
        self.click_element_with_JS(self._welcome_link)
        self._wait_until_displayed(self._welcome_menu)
        return self

    def logout(self):
        self.open_welcome_menu()._click_on_logout_link()
        return LoginPage(self.driver)

    def open_about_modal(self):
        self.open_welcome_menu()._click_on_about_link()
        return AboutPage(self.driver)

    def click_on_logo(self):
        self.click_element_with_JS(self._logo_image)
        self.switch_to_new_tab()
        return OrangeHRMPRODPage(self.driver)

    # endregion

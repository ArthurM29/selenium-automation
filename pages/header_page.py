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
        about_link = self._wait_until_displayed(self._welcome_menu_about_link)
        selenium_lib.click_with_JS(self.driver, about_link)

    def _click_on_logout_link(self):
        logout_link = self._wait_until_displayed(self._welcome_menu_logout_link)
        selenium_lib.click_with_JS(self.driver, logout_link)

    # endregion

    def is_logo_displayed(self):
        return self._is_displayed(self._logo_image)

    def get_welcome_text(self):
        return self.driver.find_element(*self._welcome_link).text

    def open_welcome_menu(self):
        welcome_link = self.driver.find_element(*self._welcome_link)
        selenium_lib.click_with_JS(self.driver, welcome_link)
        self._wait_until_displayed(self._welcome_menu)
        return self

    def logout(self):
        self.open_welcome_menu()._click_on_logout_link()
        return LoginPage(self.driver)

    def open_about_modal(self):
        self.open_welcome_menu()._click_on_about_link()
        return AboutPage(self.driver)

    def click_on_logo(self):
        logo = self.driver.find_element(*self._logo_image)
        selenium_lib.click_with_JS(self.driver, logo)

        # switch to new tab
        new_opened_tab_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(new_opened_tab_handle)
        return OrangeHRMPRODPage(self.driver)

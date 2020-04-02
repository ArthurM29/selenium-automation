from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrangeHRMPRODPage(BasePage):
    # region locators
    _contact_sales_button = (By.CSS_SELECTOR, '.btn-orange.contact-ohrm')
    _page_identifier_element = _contact_sales_button

    # endregion

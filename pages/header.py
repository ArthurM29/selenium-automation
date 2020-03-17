from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    _name = 'Header'
    _logo_div = (By.ID, 'branding')
    _page_identifier = _logo_div


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.exceptions import PageNotLoadedException


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""
    _name = None
    _url = None
    _page_identifier = None

    def __init__(self, driver):
        self._driver = driver
        self._verify_page_is_loaded()

    def _verify_page_is_loaded(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            wait.until(EC.visibility_of_element_located(self._page_identifier))
        except TimeoutException:
            raise PageNotLoadedException(
                f"'{self._name}' was not loaded. Page identifier {self._page_identifier} was not visible during 10 seconds")

    def open(self):
        self._driver.get(self._url)

    # region Wait methods
    def _wait_until(self, condition, timeout=5):
        self.wait = WebDriverWait(self._driver, timeout)
        return self.wait.until(condition)

    def _wait_until_displayed(self, locator, timeout=5):
        return self._wait_until(EC.visibility_of_element_located(locator), timeout)
    # endregion

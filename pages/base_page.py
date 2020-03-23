from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.exceptions import PageNotLoadedException, ElementNotDisplayedException, ElementNotClickableException


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""
    url = None

    _page_identifier = None
    _page_load_timeout = 10  # seconds

    def __init__(self, driver):
        self.driver = driver
        self._verify_page_is_loaded()

    def _verify_page_is_loaded(self):
        """Wait until self._page_identifier element is displayed"""
        timeout = self._page_load_timeout
        try:
            self._wait_until_displayed(self._page_identifier, timeout=timeout)
        except TimeoutException:
            raise PageNotLoadedException(
                f"'{self.__class__.__name__}' was not loaded. Page identifier element {self._page_identifier} was not visible during {timeout} seconds.")

    def is_loaded(self):
        # TODO raises NoSuchElementException when cannot find element, should I handle and return False for not displayed - that may hide the fact that elemetn is not present
        return self.driver.find_element(*self._page_identifier).is_displayed()

    def is_not_loaded(self):
        return not self.driver.find_element(*self._page_identifier).is_displayed()

    def get_url(self):
        return self.driver.current_url

    # region Wait methods

    def _wait_until(self, condition, locator, timeout=5, **kwargs):
        wait = WebDriverWait(self.driver, timeout, **kwargs)
        return wait.until(condition(locator))

    def _wait_until_displayed(self, locator, timeout=5, **kwargs):
        try:
            return self._wait_until(EC.visibility_of_element_located, locator, timeout, **kwargs)
        except TimeoutException:
            raise ElementNotDisplayedException(f"Element {locator} was not displayed during {timeout} seconds.")

    def _wait_until_clickable(self, locator, timeout=5, **kwargs):
        try:
            return self._wait_until(EC.element_to_be_clickable, locator, timeout, **kwargs)
        except TimeoutException:
            raise ElementNotClickableException(f"Element {locator} was not clickable during {timeout} seconds.")

    # endregion

    def _is_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_not_displayed(self, locator):
        try:
            return not self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return True

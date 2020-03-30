from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.exceptions import PageNotLoadedException, ElementNotDisplayedException, ElementNotClickableException


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""
    url = None

    _page_identifier = None
    _page_identifier_timeout = 10  # seconds
    _element_wait_timeout = 5

    def __init__(self, driver):
        self.driver = driver
        self._verify_page_is_loaded()

    def _verify_page_is_loaded(self):
        """Wait until self._page_identifier element is displayed"""
        timeout = self._page_identifier_timeout
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
            raise ElementNotDisplayedException(
                f"{self.__class__.__name__} page: Element {locator} was not displayed during {timeout} seconds.")

    def _wait_until_clickable(self, locator, timeout=5, **kwargs):
        try:
            return self._wait_until(EC.element_to_be_clickable, locator, timeout, **kwargs)
        except TimeoutException:
            raise ElementNotClickableException(
                f"{self.__class__.__name__} page: Element {locator} was not clickable during {timeout} seconds.")

    # endregion

    def _is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_element_not_displayed(self, locator):
        try:
            return not self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return True

    # region driver public API
    def get_element(self, locator, wait=0, **kwargs):
        element = None
        try:
            if wait:
                element = self._wait_until_displayed(locator, timeout=wait, **kwargs)
            else:
                element = self.driver.find_element(*locator)
            # print(f"{self.__class__.__name__} page: Element with locator {locator} was found.")
        except NoSuchElementException:
            print(f"{self.__class__.__name__} page: Element with locator {locator} was not found.")
        return element

    def enter_text(self, locator, text, wait=0, **kwargs):
        self.get_element(locator, wait, **kwargs).send_keys(text)
        print(f"{self.__class__.__name__} page: Entered text '{text}' into element with locator {locator}.")

    def click_element(self, locator, wait=0, **kwargs):
        self.get_element(locator, wait, **kwargs).click()
        print(f"{self.__class__.__name__} page: Clicked on element with locator {locator}.")

    def click_element_with_JS(self, locator, wait=0, **kwargs):
        element = self.get_element(locator, wait, **kwargs)
        self.driver.execute_script("arguments[0].click();", element)
        print(f"{self.__class__.__name__} page: Clicked with JS on element with locator {locator}.")

    def get_text(self, locator, wait=0, **kwargs):
        element_text = self.get_element(locator, wait, **kwargs).text
        print(f"{self.__class__.__name__} page: Element with locator {locator} has text '{element_text}'.")
        return element_text

    def get_element_attribute(self, locator, attribute, wait=0, **kwargs):
        element_attr = self.get_element(locator, wait, **kwargs).get_attribute(attribute)
        print(
            f"{self.__class__.__name__} page: Element with locator {locator} has attribute '{attribute}' with value '{element_attr}'.")
        return element_attr

    def get_element_value(self, locator, wait=0, **kwargs):
        element_value = self.get_element(locator, wait, **kwargs).get_attribute('value')
        print(f"{self.__class__.__name__} page: Element with locator {locator} has value '{element_value}'.")
        return element_value

    def switch_to_new_tab(self):
        new_opened_tab_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(new_opened_tab_handle)

    # endregion

import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.exceptions import PageNotLoadedException, ElementNotDisplayedException, ElementNotClickableException
from selenium.webdriver.support.ui import Select
from common.selenium_lib import document_has_ready_state
from common.config.config import Config


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""
    url = None

    _page_identifier_element = None
    _page_load_timeout = Config().get('page_load_timeout')
    _element_wait_timeout = Config().get('element_wait_timeout')

    log = logging.getLogger('pretty_logger')

    def __init__(self, driver):
        self.driver = driver
        self.verify_page_is_loaded()

    def verify_page_is_loaded(self):
        try:
            self._is_page_identifier_element_displayed()
            self._is_document_in_ready_state()
        except TimeoutException:
            raise PageNotLoadedException(f"'{self.__class__.__name__}' was not loaded.")

    def _is_page_identifier_element_displayed(self):
        """Wait until self._page_identifier element is displayed"""
        try:
            self.wait_until(EC.visibility_of_element_located(self._page_identifier_element),
                            timeout=self._element_wait_timeout)
        except TimeoutException:
            raise TimeoutException(
                f"'{self.__class__.__name__}': Page identifier element {self._page_identifier_element} was not visible during {self._element_wait_timeout} seconds.")

    def _is_document_in_ready_state(self):
        self.wait_until(document_has_ready_state())

    def is_loaded(self):
        # TODO raises NoSuchElementException when cannot find element, should I handle and return False for not displayed - that may hide the fact that elemetn is not present
        return self.driver.find_element(*self._page_identifier_element).is_displayed()

    def is_not_loaded(self):
        return not self.driver.find_element(*self._page_identifier_element).is_displayed()

    def get_url(self):
        return self.driver.current_url

    # region Wait methods

    def wait_until(self, condition_method, timeout=5, **kwargs):
        """wait for the event in condition_method, log TimeoutException and re-raise"""
        wait = WebDriverWait(self.driver, timeout, **kwargs)
        try:
            return wait.until(condition_method)
        except TimeoutException:
            raise TimeoutException(
                f"Event '{condition_method.__class__.__name__}' did not occur during '{timeout}' seconds. Vars: {vars(condition_method)}")

    def wait_until_displayed(self, locator, timeout=5, **kwargs):
        try:
            return self.wait_until(EC.visibility_of_element_located(locator), timeout, **kwargs)
        except TimeoutException:
            raise ElementNotDisplayedException(
                f"{self.__class__.__name__} page: Element {locator} was not displayed during {timeout} seconds.")

    def wait_until_clickable(self, locator, timeout=5, **kwargs):
        try:
            return self.wait_until(EC.element_to_be_clickable(locator), timeout, **kwargs)
        except TimeoutException:
            raise ElementNotClickableException(
                f"{self.__class__.__name__} page: Element {locator} was not clickable during {timeout} seconds.")

    # endregion

    def _is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    # region driver public API
    def get_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            print(f"{self.__class__.__name__}: Element with locator {locator} was found.")
            return element
        except NoSuchElementException as e:
            print(f"{self.__class__.__name__}: Element with locator {locator} was not found.")
            raise e

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)
        self.log.info(f"{self.__class__.__name__}: Entered text '{text}' into element with locator {locator}.")

    def click_element(self, locator):
        self.get_element(locator).click()
        self.log.info(f"{self.__class__.__name__}: Clicked on element with locator {locator}.")

    def click_element_with_JS(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        self.log.info(f"{self.__class__.__name__}: Clicked with JS on element with locator {locator}.")

    def get_text(self, locator):
        element_text = self.get_element(locator).text
        self.log.info(f"{self.__class__.__name__}: Element with locator {locator} has text '{element_text}'.")
        return element_text

    def get_element_attribute(self, locator, attribute):
        element_attr = self.get_element(locator).get_attribute(attribute)
        self.log.info(
            f"{self.__class__.__name__}: Element with locator {locator} has attribute '{attribute}' with value '{element_attr}'.")
        return element_attr

    def get_element_value(self, locator):
        element_value = self.get_element(locator).get_attribute('value')
        self.log.info(f"{self.__class__.__name__}: Element with locator {locator} has value '{element_value}'.")
        return element_value

    def switch_to_new_tab(self):
        new_opened_tab_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(new_opened_tab_handle)

    def select_dropdown_option(self, locator, option_name):
        Select(self.get_element(locator)).select_by_visible_text(option_name)

    # endregion

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class element_attribute_contains_value(object):
    """ An expectation for checking if the given value is present in the
    specified element attribute.
    locator, attribute, value
    """

    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        try:
            element_attribute = EC._find_element(driver, self.locator).get_attribute(self.attribute)
            if element_attribute:
                return self.value in element_attribute
            else:
                return False
        except StaleElementReferenceException:
            return False


class document_has_ready_state(object):
    """ An expectation for checking if the web page document.readyState is complete """

    def __call__(self, driver):
        page_state = driver.execute_script('return document.readyState;')
        return page_state == 'complete'

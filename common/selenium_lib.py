from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_with_JS(driver, element):
    driver.execute_script("arguments[0].click();", element)


class element_attribute_contains_value(object):
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

# class text_to_be_present_in_element_value(object):
#     """
#     An expectation for checking if the given text is present in the element's
#     locator, text
#     """
#     def __init__(self, locator, text_):
#         self.locator = locator
#         self.text = text_
#
#     def __call__(self, driver):
#         try:
#             element_text = _find_element(driver,
#                                          self.locator).get_attribute("value")
#             if element_text:
#                 return self.text in element_text
#             else:
#                 return False
#         except StaleElementReferenceException:
#                 return False

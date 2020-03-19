from selenium.webdriver.support.wait import WebDriverWait


class SeleniumLibrary():
    # region Wait methods
    def _wait_until(self, condition, timeout=5):
        self.wait = WebDriverWait(self.driver, timeout)
        return self.wait.until(condition)

    def _wait_until_displayed(self, locator, timeout=5):
        return self._wait_until(EC.visibility_of_element_located(locator), timeout)
    # endregion

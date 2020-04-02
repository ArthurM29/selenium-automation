import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

_username_input = (By.ID, 'txtUsername')
_password_input = (By.ID, 'txtPassword')
_login_button = (By.ID, 'btnLogin')
_login_form = (By.ID, 'frmLogin')
_invalid_login_error_message = (By.ID, 'spanMessage')


class page_is_loaded(object):
    def __call__(self, driver_):
        page_state = driver_.execute_script('return document.readyState;')
        return page_state == 'complete'


start = time.time()

for i in range(1):
    driver.find_element(*_username_input).send_keys('Admin')
    driver.find_element(*_password_input).send_keys('admin123')
    driver.find_element(*_login_button).click()

    # WebDriverWait(driver, 10).until(page_is_loaded())
    driver.find_element(*(By.ID, 'menu_admin_viewAdminModule')).click()


    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(_username_input))
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(_password_input))
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(_login_button))


end = time.time()

print(f"Duration: {end - start}")




driver.close()

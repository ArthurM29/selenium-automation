import time
from common.selenium_lib import element_attribute_contains_value
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.header_page import Header

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")



# result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'txtUsername')))


login_page = LoginPage(driver)
dashboard = login_page.login('Admin', 'admin123')
driver = dashboard.driver

# time.sleep(1)

# wait = WebDriverWait(driver, 10)
#
# wait.until(element_attribute_contains_value((By.TAG_NAME, 'body'), 'cz-shortcut-listen', 'true'))



def click_with_JS(driver, element):
    driver.execute_script("arguments[0].click();", element)

element = driver.find_element(By.CSS_SELECTOR, '#branding img')
click_with_JS(driver, element)

def get_tab_by_title(driver, title):
    for handle in driver.window_handles:
        driver.switch_to.window(title)
        if driver.title == title:
            return handle
    raise ValueError(f"No tab found with title {title}")

tab_handle = get_tab_by_title('HR Management System | HR Management Software | OrangeHRM')



# driver.switch_to.window(driver.window_handles[1])
# print(driver.title)
# print(driver.current_url)

# wait.until(EC.presence_of_element_located((By.ID, 'welcome'))).click()
# driver.find_element(By.ID, 'welcome').click()
# header_page = Header(login_page.driver)
# new_loging_page = header_page.logout()
# new_loging_page.is_loaded()

# assign_link_xpath = (By.XPATH, '//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a/span')
#
# result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, assign_link_xpath)))
# result.click()
# _wait_until(assign_link_xpath, EC.visibility_of_element_located).click()
# _wait_until_displayed(assign_link_xpath).click()

# driver.close()

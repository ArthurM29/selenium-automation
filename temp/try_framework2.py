import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from models.user import User
from pages.admin.add_user_page import AddUserPage
from pages.admin.user_management_page import UserManagementPage
from pages.login_page import LoginPage
from pages.menu.firstlevelmenu import FirstLevelMenu

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'txtUsername')))
# print()

# login_page = LoginPage(driver)
# dashboard = login_page.login('Admin', 'admin123')
# driver = dashboard.driver

# time.sleep(1)

# wait = WebDriverWait(driver, 10)
#
# wait.until(element_attribute_contains_value((By.TAG_NAME, 'body'), 'cz-shortcut-listen', 'true'))


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


login_page = LoginPage(driver)
login_page._enter_username('Admin')
login_page._enter_password('admin123')
login_page._click_login_button()

menu = FirstLevelMenu(login_page.driver)
menu.select_menu_item('Admin')
menu.click_element((By.ID, 'menu_admin_UserManagement'))

user_management_page = UserManagementPage(menu.driver)

add_user_page = user_management_page.click_add_button()
add_user_page._select_user_role('Admin')


user = User()
add_user_page.add_user(user)


driver.close()

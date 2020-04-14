import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from models.user import User
from pages.admin.add_user_page import AddUserPage
from pages.admin.user_management_page import UserManagementPage
from pages.login_page import LoginPage
from pages.menu.main_menu import MainMenu

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

login_page = LoginPage(driver)
login_page._enter_username('Admin')
login_page._enter_password('admin123')
login_page._click_login_button()

menu = MainMenu(login_page.driver)
admin_menu = menu.hover_on('Maintenance').select('Access Records')
# organization_menu = admin_menu.hover_on('Organization')
# organization_menu.hover_on('Structure')
# organization_structure_page = organization_menu.select('Structure')
# organization_structure_page.click_edit_button()


driver.close()

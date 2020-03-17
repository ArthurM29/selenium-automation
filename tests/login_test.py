import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from conftest import create_driver


def test_valid_login(create_driver):
    driver = create_driver
    login_page = LoginPage(driver)
    dashboard = login_page.login('Admin', 'admin123')
    assert dashboard.get_title() == 'Dashboard'

# test_valid_login()
